# Calculateur de Score QTBG

Ce petit outil permet de calculer le **Score'** d'un joueur à partir de ses statistiques de jeu (Kills, Assists, Dégâts, Morts), basé sur la formule suivante :

$$ Score' = 4K + A + 2 \left\lfloor \frac{DMG}{10000} \right\rfloor - 2D $$

Où :
- **K** : Kills
- **A** : Assists
- **DMG** : Dégâts infligés
- **D** : Morts (Deaths)

## Prérequis

- Python 3.10 ou supérieur
- [uv](https://github.com/astral-sh/uv) (Optionnel, mais recommandé pour la gestion du projet)

## Utilisation

### Avec `uv` (Recommandé)

Si vous avez `uv` installé, vous pouvez simplement lancer le script sans vous soucier de l'environnement virtuel :

```bash
uv run main.py
```

### Avec Python standard

Vous pouvez également lancer le script directement avec votre installation Python :

```bash
python main.py
```

## Exemple

```text
=== Calculateur de Score QTBG ===

Veuillez entrer les statistiques du joueur :
Kills (K) : 10
Assists (A) : 5
Dégâts (DMG) : 25000
Morts (D) : 3

--------------------------
Résultat du calcul :
Score' = 43
--------------------------
```

### Détail du calcul de l'exemple
- $4 \times 10 = 40$
- $+ 5$
- $+ 2 \times \lfloor 25000 / 10000 \rfloor = 2 \times 2 = 4$
- $- 2 \times 3 = -6$
- **Total : 40 + 5 + 4 - 6 = 43**
