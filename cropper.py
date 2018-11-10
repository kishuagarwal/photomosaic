import os
from utils import load_source_images
from constants import MAX_CROP_DIMENSION, CROPPED_IMAGES_DIR_NAME


def get_square_image(image):
    """
    Given an image, resize an image to get an square image.
    Resizing is done by taking the smallest dimension of width and height of the image
    along with a Max limit
    :param image:
    :return:
    """
    width, height = image.size
    final_size = min(width, height, MAX_CROP_DIMENSION)
    return image.resize((final_size, final_size))


def save_output_image(image, filename):
    file_path = os.path.join(CROPPED_IMAGES_DIR_NAME, os.path.split(filename)[-1])
    image.save(file_path)


def clean_output_dir():
    output_dir = os.path.abspath(CROPPED_IMAGES_DIR_NAME)
    print(output_dir)
    if os.path.exists(output_dir):
        for file in os.listdir(output_dir):
            file_path = os.path.join(output_dir, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    source_images = load_source_images()
    clean_output_dir()

    if len(source_images) == 0:
        print("Add some source images")
        exit(0)

    for source_image in source_images:
        square_image = get_square_image(source_image)
        save_output_image(square_image, source_image.filename)

