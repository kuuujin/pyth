ship1 = {"SHIP_NAME":"N2 Bomber","CLASS":"Heavy Fighter","DEPLOYMENT":"Limited","IN SERVICE":21}
ship2 = {"SHIP_NAME":"J-Type 327","CLASS":"Light Combat","DEPLOYMENT":"Unlimited","IN SERVICE":1}
ship3 = {"SHIP_NAME":"NX Cruiser","CLASS":"Medium Fighter","DEPLOYMENT":"Limited","IN SERVICE":18}
ship4 = {"SHIP_NAME":"N1 Starfighter","CLASS":"Medium Fighter","DEPLOYMENT":"Unlimited","IN SERVICE":25}
ship5 = {"SHIP_NAME":"Royal Cruiser","CLASS":"Light Combat","DEPLOYMENT":"Limited","IN SERVICE":4}
all_ships = [ship1,ship2,ship3,ship4,ship5]
print(f"{'SHIP NAME':<15}{'CLASS':<15}{'DEPLOYMENT':<11}{'IN SERVICE':<10}")
for ship in all_ships:
    print(f"{ship['SHIP_NAME']:<15}{ship['CLASS']:<15}{ship['DEPLOYMENT']:<11}{ship['IN SERVICE']:<10}")