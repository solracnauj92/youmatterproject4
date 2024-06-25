from PIL import Image
import io

def resize_image(image_file, width, height):
    """
    Resize an image to the specified dimensions (width, height).
    Returns the resized image file-like object.
    """
    try:
        img = Image.open(image_file)
        img = img.resize((width, height), Image.LANCZOS)
        
        # Save the resized image to a BytesIO object
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_byte_arr.seek(0)
        
        return img_byte_arr
    except Exception as e:
        raise RuntimeError(f"An error occurred while resizing the image: {str(e)}")
