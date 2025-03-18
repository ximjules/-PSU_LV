import numpy as np
import matplotlib.pyplot as plt

def napravi_sahovnicu(velicina_kvadrata, broj_kvadrata_visina, broj_kvadrata_sirina):
    """
    Funkcija stvara sliku šahovnice s crno-bijelim kvadratima.
    
    Argumenti:
    - velicina_kvadrata: veličina jednog kvadrata u pikselima
    - broj_kvadrata_visina: broj kvadrata po visini slike
    - broj_kvadrata_sirina: broj kvadrata po širini slike

    Povratna vrijednost:
    - img: numpy polje koje predstavlja sliku šahovnice
    """

    # 1. Kreiramo osnovni crno-bijeli blok (jedan crni i jedan bijeli kvadrat)
    blok = np.array([[0, 255], [255, 0]])  # 0 = crno, 255 = bijelo

    # 2. Ponovimo blok vodoravno i okomito da dobijemo punu šahovnicu
    uzorak = np.tile(blok, (broj_kvadrata_visina, broj_kvadrata_sirina))

    # 3. Skaliramo svaki kvadrat na zadanu veličinu (proširujemo sliku)
    img = np.kron(uzorak, np.ones((velicina_kvadrata, velicina_kvadrata)))

    return img

# Definiramo parametre slike
velicina_kvadrata = 50  # Veličina kvadrata u pikselima
broj_kvadrata_visina = 4  # Broj kvadrata po visini
broj_kvadrata_sirina = 4  # Broj kvadrata po širini

# Generiramo sliku
img_sahovnica = napravi_sahovnicu(velicina_kvadrata, broj_kvadrata_visina, broj_kvadrata_sirina)

# Prikaz slike
plt.imshow(img_sahovnica, cmap='gray', vmin=0, vmax=255)
plt.title("Šahovnica")
plt.xlim(0,300)
plt.ylim(0,200)
plt.show()
