hora_atual = 2 
horas_espera = 51 


hora_alarme = hora_atual + horas_espera


if hora_alarme >= 24:
    hora_alarme = hora_alarme - 24 

print(f"O alarme irá tocar às {hora_alarme} horas.")
