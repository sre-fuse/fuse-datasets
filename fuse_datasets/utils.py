import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_data(data, target):
    plt.figure(figsize=(20,4))
    for index, (image, label) in enumerate(zip(data[0:5], target[0:5])):
        plt.subplot(1, 5, index + 1)
        image = np.reshape(image, (100,100,3))
        plt.imshow(image)
        plt.title(label, fontsize = 20)