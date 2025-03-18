#1.zad

#Napišite program koji od korisnika zahtijeva unos radnih sati te
#  koliko je plaćen po radnom satu. Koristite ugrađenu
#Python metodu input(). Nakon toga izračunajte koliko je korisnik 
#zaradio i ispišite na ekran. Na kraju prepravite
#rješenje na način da ukupni iznos izračunavate u zasebnoj 
#funkciji naziva total_euro.


broj_sati = int(input("Unesite broj radnih sati: "))
iznosPoSatu = float(input("Unesite iznos placen po satu rada: "))

#ukupanIznos = broj_sati*iznosPoSatu

#ovo je obican ispis
#print("Ukupan iznos je: ",ukupanIznos)

#ispis pomocu funkcije
def total_euro(sati, satnica):
    return sati*satnica

ukupanIznos = total_euro(broj_sati, iznosPoSatu)
print("Ukupan iznos je: ", ukupanIznos)

