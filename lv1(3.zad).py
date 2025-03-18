#Napišite program koji od korisnika zahtijeva unos 
# brojeva u beskonačnoj petlji sve dok korisnik ne upiše „Done“
#  (bez
#navodnika). Pri tome brojeve spremajte u listu.
#Nakon toga potrebno je ispisati koliko brojeva
#je korisnik unio, njihovu
#srednju, minimalnu i maksimalnu vrijednost.
#Sortirajte listu i ispišite je na ekran.
#Dodatno: osigurajte program od pogrešnog unosa 
#(npr. slovo umjesto brojke) na način da program zanemari taj unos i
#ispiše odgovarajuću poruku.

brojevi = []  #lista

while True:
    unosBrojeva=input("Unesi niz brojeva te napisi done kad je niz gotov: ")
    
    if unosBrojeva.lower()=="done":
        break

    try:
        broj=float(unosBrojeva)
        brojevi.append(broj)
    except ValueError:
        print("GRESKA!")


if brojevi:  # Podaci o dobivenoj listi
    print(f"Unio si {len(brojevi)} brojeva.")  #koliko ih ima len=duzina
    print(f"Srednja vrijednost: {sum(brojevi) / len(brojevi)}")  #srednja vrijednst
    print(f"Minimalna vrijednost: {min(brojevi)}")
    print(f"Maksimalna vrijednost: {max(brojevi)}")
    brojevi.sort()  #sortiramo brojeve
    print(f"Sortirani brojevi: {brojevi}")  
else:
    print("Nisi unio nijedan broj.")



                      