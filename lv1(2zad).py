#Napišite program koji od korisnika zahtijeva upis 
# jednog broja koji predstavlja nekakvu ocjenu i nalazi se između 0.0 i
#1.0. Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih uvjeta:
#>= 0.9 A >= 0.8 B >= 0.7 C >= 0.6 D < 0.6 F

ocjena = float(input("Unesi ocjenu izmedju 0.0 i 1.0: "))

#petlja za ono sto trazimo za unos

while True:  #petlja koja se izvrsava dok korisnik ne unese tocno!
    try:
        ocjena
        if 0.0<=ocjena<=1.0:
            break #zavrsava petlja
        else:
            print("Pogresno uneseno!")

    except ValueError:   #ValueEror je vec zadano
        print("GRESKA!")


#petlja za provjeru ocjene

if ocjena>=0.9:
    print("A")
elif ocjena>=0.8:
    print("B")
elif ocjena>=0.7:
    print("C")
elif ocjena>=0.6:
    print("D")
else:
    print("F")            

