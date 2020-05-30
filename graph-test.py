import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from IPython.display import display, clear_output


encodingSDR=np.empty((6, 8))
plt.subplot(7,2,1)
plt.imshow(encodingSDR, cmap = "Greens")
#plt.show()

sampleSDR=np.empty((24, 24))
plt.subplot(7,2,2)
plt.imshow(sampleSDR, cmap = "Blues")
#plt.show()

reshapeActiveCells =np.empty((24,8,24))
for j in range(24):
    plt.subplot(7,4,j+1)
    plt.imshow(reshapeActiveCells[j], cmap = "Purples")
plt.show()

reshapePredictCells =np.empty((24,8,24))

for j in range(24):
    plt.subplot(7,4,j+1)
    plt.imshow(reshapePredictCells[j], cmap = "Reds")
plt.show()