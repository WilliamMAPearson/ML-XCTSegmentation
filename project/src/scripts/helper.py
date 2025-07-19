import torch

from scripts.train import *
from scripts.test import *

from PIL import Image


def pre_process(image_path):
    """
    Loads an image from the specified path, applies preprocessing transformations,
    and returns a batch-ready tensor suitable for model input.

    Parameters:
    -----------
    image_path : str
        Path to the input image file.

    Returns:
    --------
    torch.Tensor
        Preprocessed image tensor with shape (1, 3, H, W), where 1 is the batch size,
        3 is the number of color channels (RGB), and H, W are the height and width.

    Notes:
    ------
    - Assumes 'input_transform' is defined elsewhere and applies the necessary
      normalization, resizing, and tensor conversion.
    - Converts the image to RGB before applying the transform.
    """
    image = Image.open(image_path).convert("RGB")  # Ensure the image is in RGB format
    return input_transform(image).unsqueeze(0)     # Add a batch dimension (required by most models)


def segment_image_with_model(image_path, model, device):
    """
    Performs semantic segmentation on a single image using the provided model,
    then visualizes the segmentation result.

    Parameters:
    -----------
    image_path : str
        Path to the input image to segment.

    model : torch.nn.Module
        Trained segmentation model.

    device : torch.device
        Device on which to run the model (e.g., 'cpu' or 'cuda').

    Behavior:
    ---------
    - Sets the model to evaluation mode.
    - Loads and preprocesses the image, then moves it to the specified device.
    - Runs the model inference without gradient calculation.
    - Extracts the predicted segmentation mask by taking the argmax over output classes.
    - Converts the predicted mask to a NumPy array.
    - Calls `visualize_after_training` to display the original image and segmentation.

    Note:
    -----
    The function assumes that `pre_process` and `visualize_after_training` are
    defined elsewhere in the codebase.

    Example:
    --------
    segment_image_with_model("test_images/example.png", trained_model, torch.device('cuda'))
    """
    #Force model into eval
    model.eval()

    # Read in an Example Image
    input_tensor = pre_process(image_path).to(device)

    #Attempt to analyse the example image
    with torch.no_grad():
        output = model(input_tensor)['out']
        predicted = output.argmax(1).squeeze(0).cpu().numpy()

    #Visualise the sementation
    visualize(image_path, predicted)