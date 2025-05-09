### 1️⃣ Desafio Classificador de nível de Herói

while True: 
  NomeHeroi = input("Digite o nome do Heroi: ") 

  try:
    xp = int(input(" Digite o Nível do Heroi: "))
  except ValueError:
    print("Por favor, digite um número Valido")
    continue

if xp < 1.000:
    Nivel = "Ferro"
elif xp <= 2.000:
      Nivel = " Bronze"
elif xp <= 5.000:
     Nivel = "Prata"
elif xp <= 7.000:
     Nivel = "Ouro"
elif xp <= 8.000:
     Nivel = "Platina"
elif xp <= 9.000:
     Nivel = "Ascendente"
elif xp  <= 10.000:
     Nivel = "Imortal"
else:
    Nivel = "Radiante"

print(f"O Herói de nome  {NomeHeroi} está no nível{NivelHeroi}")