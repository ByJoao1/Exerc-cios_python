pi = 3.14159
r = 5  

if r <= 0:
    print("O raio deve ser um número positivo!")
else:
    volume = (4/3) * pi * r**3
    print(f"O volume da esfera com raio {r} é {volume:.2f}")
