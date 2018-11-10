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


def get_square_image(image):
    width, height = image.size
    final_size = min(width, height, 500)
    return image.resize((final_size, final_size))


def save_output_image(image, filename):
    cropped_images_dir_name = "cropped_images"
    file_path = os.path.join(cropped_images_dir_name, os.path.split(filename)[-1])
    image.save(file_path)


if __name__ == "__main__":
    source_images = load_source_images()
    for source_image in source_images:
        print(source_image.filename)
        square_image = get_square_image(source_image)
        save_output_image(square_image, source_image.filename)

