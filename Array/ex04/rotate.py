from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def rotate(path: str) -> np.ndarray:
    if not (path.lower().endswith(".jpg") or path.lower().endswith(".jpeg")):
        print("Error: file does not have JPEG or JPG format.")
        return np.array([])

    image = ft_load(path)
    if image.size == 0:
        return np.array([])

    square = image[:400, :400]

    gray = np.mean(square, axis=2, keepdims=True).astype(np.uint8)

    print(f"The shape of image is: {gray.shape} or {gray.squeeze().shape}")
    print(gray)

    transposed = np.array([[gray[i][j] for i in range(gray.shape[0])] for j in range(gray.shape[1])])


    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)

    plt.imshow(transposed, cmap='gray')
    plt.axis('on')
    plt.show()

    return transposed

if __name__ == "__main__":
    rotate("animal.jpeg")
