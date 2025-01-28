# Color-Detection-
color detection is an excellent data analytics project and an interactive application that will accurately identify the color in an image
import cv2
import numpy as np

def get_dominant_color(image_path):
    """Get the average RGB color of the image."""
    image = cv2.imread(image_path)
    image = cv2.resize(image, (300, 300))
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = image_rgb.reshape(-1, 3)
    average_color = np.mean(pixels, axis=0)
    return average_color
def get_color_name(rgb):
    """Find the closest color name based on the RGB values."""
    color_names = {
        "Red": [255, 0, 0],
        "Green": [0, 255, 0],
        "Blue": [0, 0, 255],
        "Yellow": [255, 255, 0],
        "Cyan": [0, 255, 255],
        "Magenta": [255, 0, 255],
        "Black": [0, 0, 0],
        "White": [255, 255, 255],
        "Gray": [169, 169, 169],
    }
    closest_color = None
    min_distance = float("inf")
    for color_name, color_rgb in color_names.items():
        distance = np.linalg.norm(np.array(rgb) - np.array(color_rgb))
        if distance < min_distance:
            min_distance = distance
            closest_color = color_name
    return closest_color
def main():
    image_path = 'images/sample_image.jpg'
    avg_color = get_dominant_color(image_path)
    color_name = get_color_name(avg_color)
    print(f"Average RGB Color: {avg_color}")
    print(f"Detected Color Name: {color_name}")
if __name__ == "__main__":
    main()
