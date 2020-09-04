def carga_eletrica_diferença(numero_protons,numero_eletrons):
    e = 1.6 * (10 ** (-19))
    unidade="C"
    tipo_unidade = int(input("defina a unidade (1) - columb(C), (2) - miliculumb(mC),"
                      "(3) - microcolumb(uC), (4) -nanocolumb(nC): "))
    if tipo_unidade == 1:
        unidade = "C"
        e = 1.6 * (10 ** (-19))
    elif tipo_unidade == 2:
        unidade = "mC"
        e=e/(10**(-3))
    elif tipo_unidade == 3:
        unidade = "uC"
        e = e / (10 ** (-6))
    elif tipo_unidade == 4:
        unidade = "nC"
        e = e / (10 ** (-9))


    carga=-numero_protons+numero_eletrons
    carga_eletrica=carga*e


    print(carga_eletrica, unidade )

def numero_de_eletrons():
    e = 1.6 * (10 ** (-19))
    unidade = "C"
    carga_eletrica = int(input("defina a carga eletrica"))
    tipo_unidade = int(input("defina a unidade (1) - columb(C), (2) - miliculumb(mC),"
                             "(3) - microcolumb(uC), (4) -nanocolumb(nC): "))
    if tipo_unidade == 1:
        unidade = "C"
        e = 1.6 * (10 ** (-19))
    elif tipo_unidade == 2:
        unidade = "mC"
        e = e / (10 ** (-3))
    elif tipo_unidade == 3:
        unidade = "uC"
        e = e / (10 ** (-6))
    elif tipo_unidade == 4:
        unidade = "nC"
        e = e / (10 ** (-9))
    numero_de_eletrons=carga_eletrica/e
    if carga_eletrica>0:
        print("numero de eletrons em execesso ",numero_de_eletrons)




protons=0
eletrons=0
carga_eletrica_diferença(protons, eletrons)

