import numpy as np
import matplotlib.pyplot as plt

# Učitavanje podataka iz mtcars.csv
data = np.loadtxt(open("mtcars.csv", "rb"), delimiter=",", skiprows=1, usecols=(1,2,3,4,5,6))

# Podjela podataka u zasebne varijable
mpg = data[:, 0]  # Potrošnja goriva (miles per gallon)
cyl = data[:, 1]  # Broj cilindara
disp = data[:, 2] # Radna zapremina motora (ne koristi se u ovom zadatku)
hp = data[:, 3]   # Konjske snage
wt = data[:, 4]   # Težina vozila
qsec = data[:, 5] # Vrijeme ubrzanja (ne koristi se u ovom zadatku)

print("Podaci uspješno učitani!")


plt.scatter(hp, mpg, color='blue', alpha=0.7)
plt.xlabel("Konjske snage (hp)")
plt.ylabel("Potrošnja goriva (mpg)")
plt.title("Ovisnost potrošnje goriva o konjskim snagama")
plt.show()


plt.scatter(hp, mpg, s=wt * 50, color='green', alpha=0.6)
plt.xlabel("Konjske snage (hp)")
plt.ylabel("Potrošnja goriva (mpg)")
plt.title("Ovisnost potrošnje goriva o konjskim snagama (veličina = težina vozila)")
plt.show()


print("Minimalna potrošnja goriva (mpg):", np.min(mpg))
print("Maksimalna potrošnja goriva (mpg):", np.max(mpg))
print("Prosječna potrošnja goriva (mpg):", np.mean(mpg))

mpg_6cyl = mpg[cyl == 6]  # Filtriramo mpg samo za automobile sa 6 cilindara

print("Minimalna potrošnja goriva (mpg, 6 cilindara):", np.min(mpg_6cyl))
print("Maksimalna potrošnja goriva (mpg, 6 cilindara):", np.max(mpg_6cyl))
print("Prosječna potrošnja goriva (mpg, 6 cilindara):", np.mean(mpg_6cyl))











