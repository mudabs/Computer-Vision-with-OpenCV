import os
import cv2
import numpy as np

script_dir = os.path.dirname(__file__)
#natural image
img1_color = cv2.imread(os.path.join(script_dir, "bird.jpg"))   
#text image    
img2_color = cv2.imread(os.path.join(script_dir, "thresh_text.png"))

img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)

smooth_kernel = np.ones((3,3), np.float32) / 9

sharp_kernel = np.array([[0,-1,0],
                         [-1,5,-1],
                         [0,-1,0]])

sobel_x = np.array([[-1,0,1],
                    [-2,0,2],
                    [-1,0,1]])

output_dir = os.path.join(script_dir, "outputs")
os.makedirs(output_dir, exist_ok=True)

def apply(img, kernel):
    return cv2.filter2D(img, -1, kernel)

for (color, gray, name) in [(img1_color, img1, "Natural"),
                            (img2_color, img2, "Edges")]:

    smooth = apply(gray, smooth_kernel)
    sharp = apply(gray, sharp_kernel)
    edge = apply(gray, sobel_x)

    name_slug = name.lower().replace(" ", "_")
    out_original = os.path.join(output_dir, f"{name_slug}_original.png")
    out_smooth = os.path.join(output_dir, f"{name_slug}_smooth.png")
    out_sharpen = os.path.join(output_dir, f"{name_slug}_sharpen.png")
    out_edge = os.path.join(output_dir, f"{name_slug}_edge.png")

    cv2.imwrite(out_original, color)
    cv2.imwrite(out_smooth, smooth)
    cv2.imwrite(out_sharpen, sharp)
    cv2.imwrite(out_edge, edge)