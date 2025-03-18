#Plan:
#Zatražiti unos imena datoteke od korisnika.
#Otvoriti i pročitati datoteku (koristeći open()).
#Pronaći linije koje sadrže "X-DSPAM-Confidence:".
#Izdvojiti broj koji dolazi nakon tog teksta.
#Izračunati srednju vrijednost svih pronađenih brojeva.
#Ispisati rezultat.

#Trazimo ime datoteke
ime_datoteke = input("Unesite ime datoteke: ")

try:
    # Otvaramo datoteku 
    #"r" znaci da otvaramo u nacinu citanja
    with open(ime_datoteke, "r") as datoteka:
        zbroj = 0  # Ukupna suma pronadjenih vrijednosti
        broj_linija = 0  # Brojac koliko smo vrijednosti pronasli

        # itamo datoteku liniju po liniju
        for linija in datoteka:
            # Provjeravamo pocinje li linija s trazenim tekstom
            if linija.startswith("X-DSPAM-Confidence:"):
                # Razdvajamo liniju na dijelove
                dijelovi = linija.split(":")
                try:
                    vrijednost = float(dijelovi[1].strip())  # Pretvaramo u decimalni broj
                    zbroj += vrijednost  # Dodajemo vrijednost u ukupni zbroj
                    broj_linija += 1  # Povecavamo brojac pronadjenih linija
                except ValueError:
                    continue  # Ako broj nije ispravan idemo dalje
        
        # Racunamo i ispisujemo prosjek
        if broj_linija > 0:
            prosjek = zbroj / broj_linija
            print("Prosječna X-DSPAM-Confidence vrijednost:", prosjek)
        else:
            print("Nema pronađenih vrijednosti u datoteci.")

except FileNotFoundError:
    print("Greška: Datoteka nije pronađena.")
     




