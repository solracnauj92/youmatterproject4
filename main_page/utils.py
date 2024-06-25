from PIL import Image


def resize_image(image_path, width, height):
    """
    Resize an image located at image_path to the specified dimensions (width, height).
    Returns the resized image object.
    """
    try:
        img = Image.open(image_path)
        img = img.resize((width, height), Image.ANTIALIAS)
        return img
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{image_path}' was not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while resizing the image: {str(e)}")