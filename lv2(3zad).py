import numpy as np
import matplotlib.pyplot as plt

# Učitavanje slike
img = plt.imread("tiger.png")

# Ako je slika u boji, pretvori je u grayscale
if len(img.shape) == 3:  
    img = img[:, :, 0].copy()

# Posvjetljivanje
img_bright = np.clip(img * 1.5, 0, 1)

# Rotacija
img_rotated = np.rot90(img, k=-1)

# Zrcaljenje
img_flipped = np.flip(img, axis=1)

# Smanjenje rezolucije
img_resized = img[::10, ::10]

# Druga četvrtina slike
img_quarter = np.zeros_like(img)
sirina = img.shape[1]
img_quarter[:, sirina//4:sirina//2] = img[:, sirina//4:sirina//2]

# Prikaz svih slika
plt.figure(figsize=(12, 6))
plt.subplot(231), plt.imshow(img, cmap="gray"), plt.title("Original")
plt.subplot(232), plt.imshow(img_bright, cmap="gray"), plt.title("Posvijetljena")
plt.subplot(233), plt.imshow(img_rotated, cmap="gray"), plt.title("Rotirana 90°")
plt.subplot(234), plt.imshow(img_flipped, cmap="gray"), plt.title("Zrcaljena")
plt.subplot(235), plt.imshow(img_resized, cmap="gray"), plt.title("Smanjena rezolucija")
plt.subplot(236), plt.imshow(img_quarter, cmap="gray"), plt.title("Druga četvrtina slike")
plt.show()













