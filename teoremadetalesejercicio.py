def ingreso (v):
    x = float (input (f"Ingrese valor para {v}"))
    return x

def operacion():
    baseM = ingreso("Base mayor: ")
    basem = ingreso("Base menor: ")
    alturam = ingreso ("Altura menor: ")

    alturaM = (baseM/basem)*alturam

    return alturaM, baseM, basem, alturam

def main():
    AM,BM,Bm,Am = operacion()
    print(f"""
     {BM}
    ------ * {Am} = {AM}
     {Bm}
""")

main()