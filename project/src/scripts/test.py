import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def visualize(image_path, prediction):
    """
    Visualizes the original image alongside its predicted segmentation mask.

    Parameters:
    -----------
    image_path : str
        Path to the original input image.

    prediction : np.ndarray
        2D array of predicted class indices for each pixel.

    Behavior:
    ---------
    - Loads and displays the original image.
    - Maps predicted class indices to RGB colors using a predefined palette.
    - Displays the color-coded segmentation mask side-by-side with the original image.

    Notes:
    ------
    - The palette can be extended to support multiple classes.
    - Assumes `prediction` contains integer class labels matching the palette indices.

    Example:
    --------
    visualize("path/to/image.png", predicted_mask_array)
    """
    image = Image.open(image_path).convert("RGB")

    # Optional: define color palette
    palette = np.array([
        [0, 0, 0],         # class 0: background
        [255, 0, 0],       # class 1: your object (e.g., red)
        # Add more colors if more classes
    ])

    # Create RGB segmentation map
    color_mask = palette[prediction]

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Predicted Segmentation")
    plt.imshow(color_mask)
    plt.axis('off')

    plt.show()