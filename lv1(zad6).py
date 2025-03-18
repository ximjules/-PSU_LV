#Plan
#Otvoriti i pročitati datoteku
#Razdvojiti svaku liniju na tip poruke (ham ili spam)
#Brojati broj riječi u ham i spam porukama te izračunati prosjek.
#Brojati koliko spam poruka završava uskličnikom
#Ispisati rezultate.


# Otvaramo datoteku SMSSpamCollection.txt
#"utf-8" je za slova koja su na hrv npr:ž,š,č,ć...
try:
    with open("SMSSpamCollection.txt", "r", encoding="utf-8") as datoteka:
        ukupno_ham = 0  # Broj riječi u ham porukama
        broj_ham = 0  # Broj ham poruka
        ukupno_spam = 0  # Broj riječi u spam porukama
        broj_spam = 0  # Broj spam poruka
        spam_s_usklicnikom = 0  # Broj spam poruka koje završavaju s '!'

        # Čitamo liniju po liniju
        for linija in datoteka:
            dijelovi = linija.split("\t")  # Razdvajamo tip poruke i tekst
            if len(dijelovi) < 2:
                continue  # Preskačemo neispravne linije

            tip_poruke = dijelovi[0]  # "ham" ili "spam"
            tekst_poruke = dijelovi[1].strip()  # Sam tekst poruke

            broj_rijeci = len(tekst_poruke.split())  # Broj riječi u poruci

            if tip_poruke == "ham":
                ukupno_ham += broj_rijeci
                broj_ham += 1
            elif tip_poruke == "spam":
                ukupno_spam += broj_rijeci
                broj_spam += 1
                if tekst_poruke.endswith("!"):  # Provjera završava li uskličnikom
                    spam_s_usklicnikom += 1

    # Računanje prosječnih brojeva riječi
    prosjek_ham = ukupno_ham / broj_ham if broj_ham > 0 else 0
    prosjek_spam = ukupno_spam / broj_spam if broj_spam > 0 else 0

    # Ispis rezultata
    print("Prosječan broj riječi u HAM porukama:", prosjek_ham)
    print("Prosječan broj riječi u SPAM porukama:", prosjek_spam)
    print("Broj spam poruka koje završavaju uskličnikom:", spam_s_usklicnikom)

except FileNotFoundError:
    print("Greška: Datoteka SMSSpamCollection.txt nije pronađena.")

