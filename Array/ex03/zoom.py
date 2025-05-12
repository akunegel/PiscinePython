from PIL import Image
import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt

def zoom(path: str) -> np.ndarray:
	if not (path.lower().endswith(".jpg") or path.lower().endswith(".jpeg")):
		print("Error: file does not have JPEG or JPG format.")
		return np.array([])
	

	image = ft_load("zoom.jpeg")
	print(image)
	zoomed_img = image[:400, :400]

	print(f"New shape after slicing: {zoomed_img.shape}")
	print(zoomed_img)

	plt.imshow(zoomed_img, cmap='gray' if zoomed_img.ndim == 2 else None)
	plt.axis('on')
	plt.show()
	
if __name__ == "__main__":
	zoom("zoom.jpeg")