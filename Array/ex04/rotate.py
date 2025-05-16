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

    grey = np.mean(square, axis=2, keepdims=True).astype(np.uint8)

    print(f"The shape of image is: {grey.shape} or {grey.squeeze().shape}")
    print(grey)

    grey = grey.squeeze()

    transpose = np.array([
        [
            grey[i][j] for i in range(grey.shape[0])
            ] for j in range(grey.shape[1])
        ])

    print(f"New shape after Transpose: ({transpose.shape[0]}, {transpose.shape[1]})")
    print(transpose)

    plt.imshow(transpose, cmap='grey')
    plt.axis('on')
    plt.show()

    return transpose


if __name__ == "__main__":
    rotate("animal.jpeg")
