  ### 1️⃣ Desafio Classificador de nível de Herói

while True:
    try:
      NomeHeroi = input("Digite o nome do Heroi: ").strip().lower()
    except ValueError:
      print("XP deve ser Letras!")
    try:
      xp = int(input(" Digite o Nível do Heroi: "))
    except ValueError:
     print("XP deve ser números!")

    if xp < 1000:
      Nivel = "Ferro"
    elif xp <= 2000:
      Nivel = "Bronze"
    elif xp <= 5000:
        Nivel = "Prata"
    elif xp <= 7000:
      Nivel = "Ouro"
    elif xp <= 8000:
      Nivel = "Platina"
    elif xp <= 9000:
      Nivel = "Ascendente"
    elif xp <= 10000:
      Nivel = "Imortal"
    else:
      Nivel = "Radiante"

    print(f"O Herói de nome {NomeHeroi} está no nível {Nivel}")
    break 

