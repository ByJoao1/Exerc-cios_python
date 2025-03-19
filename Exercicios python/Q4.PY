hora_atual = int(input("Digite a hora atual (em horas): "))
horas_espera = int(input("Digite o número de horas para o alarme tocar: "))

hora_alarme = (hora_atual + horas_espera) % 24


print(f"O alarme irá tocar às {hora_alarme} horas.")
