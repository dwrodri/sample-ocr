import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pprint import pprint
from PIL import Image
import json


def bounding_box_from_query(points):
    xs = []
    ys = []
    for elem in points:
        xs.append(elem["x"])
        ys.append(elem["y"])
    upper_left = (min(xs), min(ys))
    width = max(xs) - min(xs)
    height = max(ys) - min(ys)
    return patches.Rectangle(
        upper_left, width, height, linewidth=1, edgecolor="r", facecolor="none"
    )


if __name__ == "__main__":
    cookbook_photo = np.array(Image.open("cookbook.png"), dtype=np.uint8)
    fig, ax = plt.subplots(1)
    ax.imshow(cookbook_photo)
    with open("sample_output.json") as file_handle:
        google_vision_response = json.load(file_handle)
        master_text = google_vision_response["responses"][0]["textAnnotations"][0][
            "description"
        ]
        print(master_text)
        # for i in range(len(master_text.split())):
        #     if master_text.split()[i] == "cup":
        #         print("Found cup at {}".format(i))
        #         rect = bounding_box_from_query(
        #             google_vision_response["responses"][0]["textAnnotations"][i+1][
        #                 "boundingPoly"
        #             ]["vertices"]
        #         )
        #         ax.add_patch(rect)

    # plt.show()
