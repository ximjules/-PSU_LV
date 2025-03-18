#Plan:
#Otvoriti i pročitati datoteku song.txt.
#Podijeliti tekst na riječi,
#ignorirajući interpunkciju i pretvarajući ih u mala slova.
#Brojati pojavljivanja svake riječi pomoću rječnika.
#Pronaći riječi koje se pojavljuju samo jednom i ispisati ih.


# Otvaramo datoteku song.txt
try:
    with open("song.txt", "r", encoding="utf-8") as datoteka:
        rijeci = {}  # Rječnik za brojanje riječi

        # Čitamo liniju po liniju
        for linija in datoteka:
            linija = linija.lower()  # Pretvaramo u mala slova
            rijeci_u_liniji = linija.split()  # Razdvajamo tekst na riječi

            # Brojimo pojavljivanja riječi
            for rijec in rijeci_u_liniji:
                if rijec in rijeci:
                    rijeci[rijec] += 1
                else:
                    rijeci[rijec] = 1

    # Pronalazimo riječi koje se pojavljuju samo jednom
    rijeci_jednom = []
    for rijec in rijeci:
        if rijeci[rijec] == 1:
            rijeci_jednom.append(rijec)

    # Ispisujemo rezultat
    print("Broj riječi koje se pojavljuju samo jednom:", len(rijeci_jednom))
    print("Te riječi su:", rijeci_jednom)

except FileNotFoundError:
    print("Greška: Datoteka song.txt nije pronađena.")


