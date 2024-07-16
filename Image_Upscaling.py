import math
import os

import cv2


def upscale_images_nearest_neighbor(directory, min_size=512):
    if not os.path.exists(directory):
        print(f"Das Verzeichnis {directory} existiert nicht.")
        return

    output_directory = os.path.join(directory, "NEWDATASET")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            try:
                img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)

                height, width = img.shape[:2]

                scale_factor = max(min_size / width, min_size / height)

                new_width = math.ceil(width * scale_factor)
                new_height = math.ceil(height * scale_factor)

                upscaled_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_NEAREST)

                output_path = os.path.join(output_directory, filename)
                cv2.imwrite(output_path, upscaled_img)
                print(f"{filename} wurde erfolgreich hochskaliert und gespeichert.")
            except Exception as e:
                print(f"Fehler beim Verarbeiten der Datei {filename}: {e}")


if __name__ == "__main__":
    directory = "./NEWDATASET_CLEANED"
    upscale_images_nearest_neighbor(directory)
