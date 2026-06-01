"""
╔══════════════════════════════════════════════════════════════╗
║         FILTRO DE BLOOM — CONTROL DE ACCESO IoT              ║
║         Raspberry Pi 3 · n=500 estudiantes · m=4000 bits     ║
╚══════════════════════════════════════════════════════════════╝

PARÁMETROS DEL EJERCICIO:
    n = 500   → cantidad de estudiantes a registrar
    m = 4000  → bits disponibles en la placa (memoria RAM limitada)
    k = ?     → lo calculamos con la fórmula óptima

IDEA GENERAL:
    En lugar de guardar los 500 IDs completos en memoria,
    solo guardamos un arreglo de 4000 bits (500 bytes = 0.5 KB).
    Cada ID "enciende" k bits. Para verificar, revisamos esos bits.
"""

import math       # para ln(2) y e, usados en las formulas
import hashlib    # para SHA-256, nuestra funcion hash base


# =====================================================================
# PASO 1: CALCULAR k_optimo
#
# La formula viene del calculo diferencial: se minimiza la
# probabilidad de falso positivo respecto a k.
#
#   k_optimo = (m / n) x ln(2)
#
# Con nuestros valores:
#   k = (4000 / 500) x 0.6931 = 8 x 0.6931 = 5.545
#   Redondeado al entero mas cercano → k = 6
# =====================================================================

m = 4000   # total de bits en el arreglo
n = 500    # cantidad de elementos que vamos a insertar

k_exacto = (m / n) * math.log(2)   # math.log(2) = ln(2) = 0.6931...
k_optimo = round(k_exacto)          # round() redondea al entero mas cercano

print("=" * 60)
print("  FILTRO DE BLOOM - CONTROL DE ACCESO IoT")
print("=" * 60)

print(f"\n[1] Calculo de k_optimo:")
print(f"    k = (m/n) x ln(2)")
print(f"    k = ({m}/{n}) x {math.log(2):.4f}")
print(f"    k = {k_exacto:.4f}  =>  redondeado: k = {k_optimo}")


# =====================================================================
# PASO 2: LA CLASE BloomFilter
#
# Encapsulamos toda la logica en una clase para que sea
# reutilizable y facil de entender.
# =====================================================================

class BloomFilter:
    """
    Filtro de Bloom optimizado para hardware con RAM limitada.

    Atributos:
        m          -> tamano del arreglo en bits
        k          -> numero de funciones hash
        bit_array  -> el arreglo de bytes donde guardamos los bits
    """

    def _init_(self, m: int, k: int):
        """
        Constructor — se ejecuta al crear el objeto con BloomFilter(m, k).

        Parametros:
            m: cantidad de bits del arreglo
            k: cantidad de funciones hash a usar

        Detalle tecnico:
            No guardamos m bits individuales (Python no tiene tipo 'bit').
            Usamos bytearray: cada elemento es 1 byte = 8 bits.
            Para m=4000 bits necesitamos ceil(4000/8) = 500 bytes.
            Eso es MUCHO mas eficiente que una lista de 4000 enteros.
        """
        self.m = m
        self.k = k

        # math.ceil(m/8) redondea hacia arriba
        # Si m=4000 -> 4000/8 = 500.0 -> ceil = 500 bytes
        # Si m=4001 -> 4001/8 = 500.125 -> ceil = 501 bytes (no pierde bits)
        self.bit_array = bytearray(math.ceil(m / 8))

        # Contador para saber cuantos elementos se han insertado
        self.elementos_insertados = 0


    # ------------------------------------------------------------------
    # FUNCION PRIVADA: _hashes
    #
    # Genera k numeros de posicion para un elemento dado.
    # Usamos SHA-256 con k semillas distintas para simular
    # k funciones hash independientes.
    #
    # Por que SHA-256?
    #   Es parte de la biblioteca estandar de Python (hashlib),
    #   no necesita instalacion y funciona igual en Raspberry Pi.
    #
    # Que es una "semilla"?
    #   Concatenamos "semilla_0:", "semilla_1:", etc. al inicio
    #   del texto antes de hashear. Asi la misma entrada
    #   produce salidas diferentes con cada semilla.
    # ------------------------------------------------------------------
    def _hashes(self, elemento: str) -> list:
        """
        Retorna una lista de k indices (posiciones en el arreglo).

        Ejemplo para elemento="EST-001" y k=6:
            semilla_0:EST-001 -> SHA-256 -> numero -> % m -> posicion 0
            semilla_1:EST-001 -> SHA-256 -> numero -> % m -> posicion 1
            ...
            semilla_5:EST-001 -> SHA-256 -> numero -> % m -> posicion 5
        """
        indices = []

        for i in range(self.k):
            # Paso a: construir el texto con la semilla
            texto = f"semilla_{i}:{elemento}"

            # Paso b: convertir a bytes (SHA-256 trabaja con bytes, no texto)
            datos_bytes = texto.encode("utf-8")

            # Paso c: aplicar SHA-256 y obtener el resultado en hexadecimal
            # hexdigest() devuelve algo como "a3f8b2..." (64 caracteres hex)
            digest_hex = hashlib.sha256(datos_bytes).hexdigest()

            # Paso d: convertir el hexadecimal a entero
            # int("a3f8b2...", 16) convierte base 16 -> base 10
            numero_grande = int(digest_hex, 16)

            # Paso e: reducir al rango [0, m-1] con modulo
            # Si m=4000, % 4000 da un numero entre 0 y 3999
            posicion = numero_grande % self.m

            indices.append(posicion)

        return indices


    # ------------------------------------------------------------------
    # FUNCION PRIVADA: _set_bit
    #
    # Enciende (pone en 1) el bit en la posicion dada.
    #
    # El truco: trabajamos con bytes, asi que necesitamos
    # encontrar en que byte y en que posicion dentro del byte
    # esta el bit que queremos cambiar.
    #
    # Ejemplo: posicion = 17
    #   byte_idx = 17 // 8 = 2  (el byte numero 2)
    #   bit_idx  = 17 % 8  = 1  (el bit 1 dentro de ese byte)
    #   Para encender ese bit: byte |= (1 << bit_idx)
    #   1 << 1 = 0b00000010
    #   byte = byte | 0b00000010  => enciende el bit 1
    # ------------------------------------------------------------------
    def _set_bit(self, pos: int):
        """Enciende el bit en la posicion pos del arreglo."""
        byte_idx = pos // 8    # division entera -> numero del byte
        bit_idx  = pos % 8     # resto -> posicion dentro del byte

        # El operador |= es OR bit a bit: enciende el bit sin apagar los demas
        # (1 << bit_idx) crea una "mascara" con solo ese bit en 1
        self.bit_array[byte_idx] |= (1 << bit_idx)


    # ------------------------------------------------------------------
    # FUNCION PRIVADA: _get_bit
    #
    # Lee si el bit en la posicion dada esta en 1 o en 0.
    #
    # Misma logica de byte_idx y bit_idx que _set_bit,
    # pero en vez de escribir, leemos con AND (&).
    # Si el resultado es distinto de 0, el bit esta encendido.
    # ------------------------------------------------------------------
    def _get_bit(self, pos: int) -> bool:
        """Retorna True si el bit en la posicion pos esta en 1."""
        byte_idx = pos // 8
        bit_idx  = pos % 8

        # & es AND bit a bit: si el bit esta en 1, el resultado es != 0
        # bool() convierte: 0 -> False, cualquier otro numero -> True
        return bool(self.bit_array[byte_idx] & (1 << bit_idx))


    # ------------------------------------------------------------------
    # METODO PUBLICO: insertar
    #
    # Registra un nuevo elemento en el filtro.
    # Solo enciende k bits — no guarda el texto.
    # ------------------------------------------------------------------
    def insertar(self, elemento: str):
        """
        Registra un elemento en el filtro de Bloom.

        Pasos:
            1. Calcular las k posiciones hash del elemento
            2. Encender esos k bits en el arreglo
        """
        posiciones = self._hashes(elemento)   # lista de k posiciones

        for pos in posiciones:
            self._set_bit(pos)                 # encender cada bit

        self.elementos_insertados += 1


    # ------------------------------------------------------------------
    # METODO PUBLICO: consultar
    #
    # Verifica si un elemento probablemente fue insertado.
    # Retorna True  -> probablemente si (puede ser falso positivo)
    # Retorna False -> definitivamente NO fue insertado
    # ------------------------------------------------------------------
    def consultar(self, elemento: str) -> bool:
        """
        Verifica si el elemento probablemente esta en el filtro.

        Logica:
            Si ALGUN bit esta en 0 -> imposible que este registrado -> False
            Si TODOS los bits estan en 1 -> probablemente registrado -> True

        all() en Python retorna True solo si todos los elementos son True.
        Es equivalente a: bit1 and bit2 and bit3 and ... and bitK
        """
        posiciones = self._hashes(elemento)
        return all(self._get_bit(pos) for pos in posiciones)


    # ------------------------------------------------------------------
    # METODO AUXILIAR: bits_encendidos
    #
    # Cuenta cuantos bits estan en 1. Util para medir
    # que tan "lleno" esta el filtro (tasa de saturacion).
    # ------------------------------------------------------------------
    def bits_encendidos(self) -> int:
        """Cuenta los bits en 1 en todo el arreglo."""
        # bin(byte) convierte un numero a binario: 6 -> '0b110'
        # .count("1") cuenta cuantos unos tiene
        # sum() suma los conteos de todos los bytes
        return sum(bin(byte).count("1") for byte in self.bit_array)


    def tasa_saturacion(self) -> float:
        """Porcentaje de bits que estan en 1 (0.0 a 1.0)."""
        return self.bits_encendidos() / self.m


# =====================================================================
# PASO 3: CREAR EL FILTRO E INSERTAR 500 IDs VALIDOS
# =====================================================================

print(f"\n[2] Creando el filtro con m={m} bits y k={k_optimo} hashes...")
print(f"    Memoria RAM utilizada: {math.ceil(m/8)} bytes")

# Crear la instancia del filtro con los parametros del ejercicio
filtro = BloomFilter(m=m, k=k_optimo)

# Generar los 500 IDs validos: EST-001, EST-002, ..., EST-500
# f"EST-{i:03d}" formatea el numero con 3 digitos -> EST-001, no EST-1
ids_validos = [f"EST-{i:03d}" for i in range(1, n + 1)]

print(f"\n[3] Insertando {n} IDs validos (EST-001 a EST-{n:03d})...")

for id_estudiante in ids_validos:
    filtro.insertar(id_estudiante)

# Mostrar estadisticas del filtro tras la insercion
print(f"    Bits encendidos : {filtro.bits_encendidos()} de {m}")
print(f"    Saturacion      : {filtro.tasa_saturacion()*100:.1f}%")
print(f"    (Saturacion ideal con k optimo: ~50%)")


# =====================================================================
# PASO 4: PRUEBA DE ESTRES — 200 TARJETAS NO REGISTRADAS
#
# El ejercicio pide probar IDs FALSO-001 a FALSO-200.
# Contamos cuantas veces el filtro dice "si" cuando deberia
# decir "no" -> esos son los falsos positivos.
# =====================================================================

print(f"\n[4] Prueba de estres: 200 tarjetas NO registradas...")

ids_falsos = [f"FALSO-{i:03d}" for i in range(1, 201)]

falsos_positivos = 0   # contador de veces que el filtro se equivoca

for id_falso in ids_falsos:
    resultado = filtro.consultar(id_falso)

    if resultado:
        # El filtro dijo "si" para un ID que NUNCA fue insertado
        falsos_positivos += 1

# Calcular la tasa empirica (lo que realmente ocurrio en la prueba)
tasa_fp_empirica = falsos_positivos / len(ids_falsos)

# Calcular la tasa teorica esperada con la formula:
# p = (1 - e^(-k x n / m))^k
# Esto es lo que predice la matematica — comparamos con lo real
tasa_fp_teorica = (1 - math.exp(-k_optimo * n / m)) ** k_optimo

print(f"    Total probados       : {len(ids_falsos)}")
print(f"    Falsos positivos     : {falsos_positivos}")
print(f"    Tasa FP empirica     : {tasa_fp_empirica*100:.2f}%")
print(f"    Tasa FP teorica      : {tasa_fp_teorica*100:.2f}%")


# =====================================================================
# PASO 5: VERIFICAR QUE NO HAY FALSOS NEGATIVOS
#
# Garantia matematica: si un elemento fue insertado,
# el filtro SIEMPRE lo detecta. Nunca falla hacia ese lado.
# Verificamos que los 500 IDs validos son reconocidos.
# =====================================================================

print(f"\n[5] Verificando que los 500 IDs validos son reconocidos...")

falsos_negativos = 0

for id_valido in ids_validos:
    if not filtro.consultar(id_valido):
        # Esto NO deberia ocurrir NUNCA — es un error si sucede
        falsos_negativos += 1
        print(f"    ERROR: {id_valido} no fue reconocido (falso negativo)")

if falsos_negativos == 0:
    print(f"    Los 500 IDs validos fueron reconocidos correctamente.")
    print(f"    (Los falsos negativos son matematicamente imposibles.)")


# =====================================================================
# RESUMEN FINAL
# =====================================================================

print("\n" + "=" * 60)
print("  RESUMEN FINAL")
print("=" * 60)
print(f"  Parametros del ejercicio : m={m} bits, n={n}, k={k_optimo}")
print(f"  k_optimo teorico exacto  : {k_exacto:.4f} -> redondeado a {k_optimo}")
print(f"  RAM consumida            : {math.ceil(m/8)} bytes (de ~1 GB disponibles)")
print(f"  Saturacion del filtro    : {filtro.tasa_saturacion()*100:.1f}%")
print(f"  Tasa FP teorica          : {tasa_fp_teorica*100:.2f}%")
print(f"  Tasa FP empirica         : {tasa_fp_empirica*100:.2f}%")
print(f"  Falsos negativos         : 0 (garantia matematica)")
print("=" * 60)
print("\nEjecutar con: python3 bloom_filter_iot.py")