def calculate_score(k: int, a: int, dmg: int, d: int) -> int:
    """
    Calcule le score selon la formule :
    Score' = 4K + A + 2 * floor(DMG / 10000) - 2D
    """
    # Le double slash // effectue une division entière (équivalent à floor pour des positifs)
    dmg_factor = dmg // 10000
    score = (4 * k) + a + (2 * dmg_factor) - (2 * d)
    return score

def get_valid_input(prompt: str) -> int:
    """Demande une entrée utilisateur jusqu'à obtenir un entier valide."""
    while True:
        try:
            value = input(prompt)
            return int(value)
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

def main():
    print("=== Calculateur de Score QTBG ===\n")
    print("Veuillez entrer les statistiques du joueur :")
    
    try:
        k = get_valid_input("Kills (K) : ")
        a = get_valid_input("Assists (A) : ")
        dmg = get_valid_input("Dégâts (DMG) : ")
        d = get_valid_input("Morts (D) : ")

        score = calculate_score(k, a, dmg, d)
        
        print("\n--------------------------")
        print(f"Résultat du calcul :")
        print(f"Score' = {score}")
        print("--------------------------")
        
    except KeyboardInterrupt:
        print("\n\nCalcul annulé.")

if __name__ == "__main__":
    main()

