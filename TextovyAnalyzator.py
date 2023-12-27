"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Václav Mrkvička
email: vasek.mrkvicka@gmail.com
discord: spectra111
"""

import re
TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]
cara = "-" * 40
# Spojení jmena a hesla
regusers = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Zadání uživ. jmena a hesla
uzivatelske_jmeno = input("Zadejte přihlašovací jméno: ")
heslo = input("Zadejte heslo: ")

# Ověření přihlašovacích údajů
if uzivatelske_jmeno in regusers and regusers[uzivatelske_jmeno] == heslo:
    print(f"Vítejte, {uzivatelske_jmeno}!")
    print("Máme 3 texty k analyzování.")
    print(cara)
else:
    print("Neregistrovany uživatel, ukončuji program.")
    quit()
# Výběr textu
vyber_text = input("Zadejte číslo od 1 do 3 pro výber textu: ")
print(cara)

def analyze_text_statistics(text):
    # Získání seznamu slov z textu
    words = re.findall(r'\b\w+\b', text)

    # Inicializace proměnných pro statistiky
    pocet_slov = len(words)
    pocet_slov_velke_pismeno = 0
    pocet_slov_velkymi_pismeny = 0
    pocet_slov_malymi_pismeny = 0
    pocet_cisel = 0
    suma_cisel = 0

    # Procházení slov a aktualizace statistik
    for word in words:
        if word[0].isupper() :
            pocet_slov_velke_pismeno += 1
        if word.isupper() and not any(char.isdigit() for char in word): # Kontrola, zda slovo začíná velkým písmenem a neobsahuje číslice
            pocet_slov_velkymi_pismeny += 1
        elif word.islower():
            pocet_slov_malymi_pismeny += 1
        elif word.isdigit():
            pocet_cisel += 1
            suma_cisel += int(word)

    # Výpis statistik
    print(f"Počet slov: {pocet_slov}")
    print(f"Počet slov začínajících velkým písmenem: {pocet_slov_velke_pismeno}")
    print(f"Počet slov psaných velkými písmeny: {pocet_slov_velkymi_pismeny}")
    print(f"Počet slov psaných malými písmeny: {pocet_slov_malymi_pismeny}")
    print(f"Počet čísel (ne cifer): {pocet_cisel}")
    print(f"Suma všech čísel (ne cifer) v textu: {suma_cisel}")

    # Vytvoření slovníku s četností délek slov
    cetnost_delky_slov = {}
    for delka in [len(word) for word in words]:
        cetnost_delky_slov[delka] = cetnost_delky_slov.get(delka, 0) + 1

    # Vytvoření grafické reprezentace
    print(cara)
    print("LEN | OCCURRENCES | NR.")
    print(cara)
    for delka, pocet in sorted(cetnost_delky_slov.items()):
        print(f"{delka:3} |{'*' * pocet:18} | {pocet:2}") #cisla v zavorkách zarovnání
    print(cara)

# Analýza textu
if vyber_text.isdigit():
    vyber_text = int(vyber_text)
    if 1 <= vyber_text <= len(TEXTS):
        vybrany_text = TEXTS[vyber_text - 1]
        print(vybrany_text)
        analyze_text_statistics(vybrany_text)
    else:
        print("Špatny vstup, ukončuji program.")
        quit()
else:
    print("Špatný vstup, zadáno není číslo. Ukončuji program.")
    quit()
