from PIL import Image
import os
import math

MOSAIC_SIZE = 10
IMAGE_FILE_TYPE_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def get_avg_color(image):
    avg_r, avg_g, avg_b = 0, 0, 0

    count = 0
    for t in image.getdata():
        r = t[0]
        g = t[1]
        b = t[2]
        count += 1
        avg_r += r
        avg_g += g
        avg_b += b

    avg_r = avg_r // count
    avg_g = avg_g // count
    avg_b = avg_b // count
    return avg_r, avg_g, avg_b


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


def find_nearest_image(avg_color, images):
    nearest_color = None
    nearest_image = None

    for image, image_avg_color in images:
        diff = math.sqrt(pow(image_avg_color[0] - avg_color[0], 2) +
                         pow(image_avg_color[1] - avg_color[1], 2) +
                         pow(image_avg_color[2] - avg_color[2], 2))
        if nearest_color is None or diff < nearest_color:
            nearest_color = diff
            nearest_image = image

    return nearest_image


def get_pixelated_image(image):
    height, width = image.size

    pixelated_image = Image.new("RGB", (width, height))
    for y in range(0, height, MOSAIC_SIZE):
        for x in range(0, width, MOSAIC_SIZE):
            # Take the current square of the image
            current_region = image.crop((x, y, x + MOSAIC_SIZE, y + MOSAIC_SIZE))
            avg_color = get_avg_color(current_region)

            pixelated_image.paste(avg_color, (x, y, x + MOSAIC_SIZE, y + MOSAIC_SIZE))
    pixelated_image.show()


if __name__ == "__main__":
    input_image = Image.open("input.jpg")
    print('Loaded input image')
    source_images = load_source_images()
    print('Loaded source images')

    source_images_avg_color = []

    for source_image in source_images:
        avg_color = get_avg_color(source_image)
        source_images_avg_color.append((source_image, avg_color))

    width, height = input_image.size

    output_image = Image.new("RGB", (width, height))
    for y in range(0, height, MOSAIC_SIZE):
        for x in range(0, width, MOSAIC_SIZE):
            # Take the current square of the image
            current_region = input_image.crop((x, y, x + MOSAIC_SIZE, y + MOSAIC_SIZE))
            avg_color = get_avg_color(current_region)
            nearest_image = find_nearest_image(avg_color, source_images_avg_color)
            nearest_image = nearest_image.resize((MOSAIC_SIZE, MOSAIC_SIZE))
            output_image.paste(nearest_image, (x, y, x + MOSAIC_SIZE, y + MOSAIC_SIZE))
    output_image.save("output.jpg")
