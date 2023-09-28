casos_teste = int(input("quantos casos de teste serao digitados?"))

contador = 0
quant_cobaia = 0
total_R = 0
total_C = 0
total_S = 0

while contador < casos_teste:

    contador += 1

    quant_cobaia = int(input("quantidade de cobaias: "))

    tipo_cobaia = input("tipos de cobaia: ")

    if tipo_cobaia == "R":
        total_R += quant_cobaia
    elif tipo_cobaia == "S":
        total_S += quant_cobaia
    elif tipo_cobaia == "C":
        total_C += quant_cobaia
    else:
        print("tipo invalido")

total_cobaia = total_R + total_S + total_C

percen_R = (total_R /total_cobaia) * 100
percen_S = (total_S/ total_cobaia) * 100
percen_C = (total_C /total_cobaia) * 100

print("RELATORIO FINAL:")

print("total de cobaias usadas:", total_cobaia)
print("total de ratos:", total_R)
print("total de sapos:", total_S)
print("total de coelho:", total_C)
print("percen de rato: {:.2f}".format(percen_R))
print("percen de sapo: {:.2f}".format(percen_S))
print("percen de coelho: {:.2f}".format(percen_C))