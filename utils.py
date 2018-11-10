from PIL import Image
import os

IMAGE_FILE_TYPE_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def load_source_images():
    source_images_dir_name = "source_images"
    files = os.listdir(source_images_dir_name)
    source_images = []
    for file in files:
        file_name, file_ext = os.path.splitext(file)
        if file_ext.lower() in IMAGE_FILE_TYPE_EXTENSIONS:
            file_path = os.path.join(source_images_dir_name, file)
            source_images.append(Image.open(file_path))
    return source_images

