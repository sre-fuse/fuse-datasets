import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_data(data, target):
    plt.figure(figsize=(20,4))
    for index, (image, label) in enumerate(zip(data[0:5], target[0:5])):
        plt.subplot(1, 5, index + 1)
        image = np.reshape(image, (100,100,3))
        img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        plt.imshow(img)
        plt.title(label, fontsize = 20)