results = {1:"Pedra",2:"Papel",3:"Tesoura"}

answer = 0

while answer != 4:
  players = {}

  print("Pedra(1) papel(2) ou tesoura(3)? (P1)")
  players["1"] = int(input())

  print("Pedra(1) papel(2) ou tesoura(3)? (P2)")
  players["2"] = int(input())

  p1 = players["1"]
  p2 = players["2"]

  if p1 == p2:
    print("Empate tecnico")
  else:
    if (p2 + p1) == 4:  
      if p1 > p2 : ganhador = "1"
      else: ganhador = "2"
      print(f"P{ganhador} Ganhou com {results[3]}")
    else:
      if p1 > p2 : ganhador = "1"
      else: ganhador = "2"
      print(f"P{ganhador} Ganhou com {results[players[ganhador]]}")

  print("Continuar?")
  answer = int(input())


