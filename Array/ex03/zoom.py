import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def zoom(path: str) -> np.ndarray:
    """
    Loads a JPEG image, prints its original shape, number of channels,
    and pixel content. Converts to grayscale, crops to 400x400, and displays.
    """

    phrase = "New shape after slicing:"

    if not (path.lower().endswith(".jpg") or path.lower().endswith(".jpeg")):
        print("Error: file does not have JPEG or JPG format.")
        return np.array([])

    image = ft_load(path)
    if image is None or not isinstance(image, np.ndarray):
        print("Error: Failed to load image.")
        return np.array([])

    print(image)

    if image.ndim == 3 and image.shape[2] == 3:
        gray = np.mean(image, axis=2).astype(np.uint8)
    else:
        gray = image

    z_img = gray[:400, :400]

    print(
        f"{phrase} {(z_img.shape[0], z_img.shape[1], 1)} or {z_img.shape}"
        )
    print(z_img)

    plt.imshow(z_img, cmap='gray' if z_img.ndim == 2 else None)
    plt.axis('on')
    plt.show()


if __name__ == "__main__":
    zoom("zoom.jpeg")
