import cv2
import os
import numpy as np
import pandas as pd

input_folder = "./lot0"
data = "./lot0/labels.csv"

labels_df = pd.read_csv(data).set_index("filename")
label_columns = labels_df.columns.tolist()

images = []
labels = []
filenames = []

for filename in sorted(os.listdir(input_folder)):
    if not filename.endswith(".png"):
        continue

    if filename not in labels_df.index:
        print(f"No label for {filename}, skipped")
        continue

    image_path = os.path.join(input_folder, filename)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Could not read {filename}, skipped")
        continue

    images.append(image)
    labels.append(labels_df.loc[filename].values)
    filenames.append(filename)

X = np.array(images)
y = np.array(labels)

print(X.shape, y.shape)
print(filenames[0], dict(zip(label_columns, y[0])))