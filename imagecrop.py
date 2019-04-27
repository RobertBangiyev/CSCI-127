#Name: RObert Bangiyev
#Date: 23 October, 2018
#This program crops the imzge
import matplotlib.pyplot as plt
import numpy as np
imName=input("Enter image file name: ")
outputname=input("Enter output file: ")

img=plt.imread(imName)
height=img.shape[0]
width=img.shape[1]
outimg=img[height//2:, :width//2]
plt.imsave(outputname, outimg)
