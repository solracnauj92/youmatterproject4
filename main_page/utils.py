import cloudinary.uploader
from .models import Post
from django.core.files.uploadedfile import InMemoryUploadedFile
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

def handle_image_upload(instance, image_file):
    """
    Handle image upload, resize if necessary, and upload to Cloudinary.
    Updates the instance with the Cloudinary URL.
    """
    try:
        # Check if a new image is uploaded
        if isinstance(image_file, InMemoryUploadedFile):
            if image_file.size > 10 * 1024 * 1024:  # 10 MB limit
                raise RuntimeError("File size is too large. Please upload a picture less than 10MB.")
            
            # Resize the image
            resized_image = resize_image(image_file, 800, 600)
            
            # Upload the resized image to Cloudinary
            uploaded_image = cloudinary.uploader.upload(resized_image, folder="uploads")
            
            # Update the instance with the Cloudinary URL
            instance.featured_image = uploaded_image['secure_url']
    
    except Exception as e:
        raise RuntimeError(f"Error uploading image to Cloudinary: {str(e)}")