varor = [
  ["MONSTER", 20],
  ["GIFFLAR", 24],
  ["MUNKAR", 5],
  ["KEXCHOKLAD", 8],
  ["VITLÖKS BRÖD", 20],
  ["Cola", 16],
  ["S-märke", 1],
  ["Ölkorv", 40]
]

print("Det är rast, dax för coop rundan: ")

budget = int(input("Vad är din budget i kronor: "))

import random, time

shoppinglista = []

print("Du går runt och plockar på dig varor")
time.sleep(2)


while budget > 5:
    vara = varor[random.randint(0, len(varor)-1)]
    if budget > vara[1]:
        shoppinglista.append(vara)
        budget = budget - vara[1]
        print(budget)

print("dagens köp: ")

for vara in shoppinglista:
  print(f"{vara[0]}")

print(f"Kvar i din ficka ligger {budget:0} kronor.")

