from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    if not (path.lower().endswith(".jpg") or path.lower().endswith(".jpeg")):
        print("Error: file does not have JPEG or JPG format.")
        return np.array([])
    try:
        with Image.open(path) as img:
            img = img.convert('RGB')
            arr = np.array(img)
            return arr
    except Exception as e:
        print(f"Error: could not open file. {e}")
        return np.array([])
