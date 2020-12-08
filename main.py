import numpy as np
import matplotlib.pyplot as plt
from PIL import Imagegit init

t = np.linspace(0, 2 * np.pi)
x = 2 * ((np.sin(t))**3)
y = 2 * ((np.cos(t))**3)

fig = plt.figure(figsize=(5, 5))
plt.plot(x, y,)

plt.savefig('img.png')

img = Image.open('img.png')
img = img.convert('L')
img = img.save('result.bmp')

plt.show()