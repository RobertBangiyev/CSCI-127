#Name: Robert Bangiyev
#Date: September 24, 2018
#This program makes an image blue
import matplotlib.pyplot as plt
import numpy as np
image=input("Enter name of the input file: ")
img=plt.imread(image)
img2=img.copy()
img2[:,:,0]=0
img2[:,:,1]=0
image2=input("Enter name of the output file: ")
plt.imsave(image2, img2)
