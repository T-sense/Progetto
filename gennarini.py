def mostra_menu():
    print("Benvenuto al Mc Donegani!")
    print("Scegli un panino:")
    print("1. Crispy - 5 euro")
    print("2. Cheeseburger - 5 euro")
    print("3. Big Mac - 5 euro")

    print("\nScegli un secondo:")
    print("4. Alette - 3 euro")
    print("5. Panzerotti - 3 euro")
    print("6. Nuggets - 3 euro")

    print("\nScegli un dessert:")
    print("7. McFlurry - 4 euro")
    print("8. Sunday - 4 euro")
    print("9. Gelato - 4 euro")

def calcola_totale(scelte):
    prezzi = {
        1: 5, 2: 5, 3: 5, 4: 3, 5: 3, 6: 3, 7: 4, 8: 4, 9: 4
    }
    totale = sum(prezzi[scelta] for scelta in scelte)
    return totale

def verifica_gadget(scelte):
    ha_panino = any(scelta in [1, 2, 3] for scelta in scelte)
    ha_secondo = any(scelta in [4, 5, 6] for scelta in scelte)
    ha_dessert = any(scelta in [7, 8, 9] for scelta in scelte)
    return ha_panino and ha_secondo and ha_dessert

def main():
    mostra_menu()
    scelte = []

    for _ in range(3):
        scelta = int(input("Inserisci il numero della tua scelta: "))
        scelte.append(scelta)

    totale = calcola_totale(scelte)
    print(f"Il totale è: {totale} euro")

    if verifica_gadget(scelte):
        print("Hai diritto al gadget che potrai ritirare gratuitamente")

if __name__ == "__main__":
    main()
