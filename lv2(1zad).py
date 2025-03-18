import numpy as np
import matplotlib.pyplot as plt

# Koordinate točaka (pravokutnik)
pravokutnik = np.array([[1, 1], [3, 1], [3, 2], [2, 2], [1, 1]])


# Crtanje slike
plt.plot(pravokutnik[:, 0], pravokutnik[:, 1], 'b-', linewidth=2)  # Plavi pravokutnik


# Postavljanje granica i prikaz
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.grid()
plt.show()
