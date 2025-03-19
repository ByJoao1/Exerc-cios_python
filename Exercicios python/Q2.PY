preco_capa = 24.95
desconto = 0.40
n_exemplares = 60


if n_exemplares <= 0:
    print("O número de exemplares deve ser positivo!")
else:
    preco_com_desconto = preco_capa * (1 - desconto)
    custo_transporte = 3 + (n_exemplares - 1) * 0.75
    custo_total = preco_com_desconto * n_exemplares + custo_transporte
    print(f"O custo total de atacado para {n_exemplares} cópias é R$ {custo_total:.2f}")
