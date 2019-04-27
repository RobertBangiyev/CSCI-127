import matplotlib.pyplot as plt
import numpy as np
img=np.ones((10,10,3))
img[:,:3,1]
img[:,:-3,1]
img[4:6,:,1]
plt.imsave("logo.png",img)
