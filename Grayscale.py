import cv2
import os

input_folder = "./lot0"
output_folder = "./lot0_grayscale"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        image_path = os.path.join(input_folder, filename)

        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.imwrite(os.path.join(output_folder, filename), gray_image)