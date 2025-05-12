import numpy as np
import matplotlib.pyplot as plt
from load_image import display_image

def ft_invert(array):
    """
    Inverts the color of the image received.
    """
    result = 255 - array  
    print(result)
    display_image("Figure VIII.2: Invert", result)
    return result

def ft_red(array):
    """
    Keeps only the red channel.
    """
    result = array * [1, 0, 0]  
    print(result)
    display_image("Figure VIII.3: Red", result)
    return result

def ft_green(array):
    """
    Keeps only the green channel.
    """
    result = np.copy(array)
    height, width, _ = array.shape

    for i in range(height):
        for j in range(width):
            result[i][j][0] = result[i][j][0] - result[i][j][0]
            result[i][j][2] = result[i][j][2] - result[i][j][2]

    print(result)
    display_image("Figure VIII.4: Green", result)
    return result

def ft_blue(array):
    """
    Keeps only the blue channel.
    """
    result = np.zeros_like(array)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            result[i][j][2] = array[i][j][2]
    print(result)
    display_image("Figure VIII.5: Blue", result)
    return result

def ft_grey(array):
    """
    Converts image to grayscale using average of channels.
    """
    h, w, _ = array.shape
    result = np.zeros_like(array)
    for i in range(h):
        for j in range(w):
            gray = (array[i][j][0] / 3 + array[i][j][1] / 3 + array[i][j][2] / 3)
            val = int(gray)
            result[i][j] = [val, val, val]
    print(result)
    display_image("Figure VIII.6: Grey", result)
    return result
