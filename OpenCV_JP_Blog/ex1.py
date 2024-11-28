"""
参考：https://take-tech-engineer.com/category/python/opencv/
Web上のImageを活用する
"""
import requests
import cv2

url = "https://github.com/opencv/opencv/blob/master/samples/data/butterfly.jpg?raw=true"
file_name = "butterfly.jpg"

response = requests.get(url)
image = response.content

with open(file_name, "wb") as f:
    f.write(image) # Image Save

img = cv2.imread("butterfly.jpg") # Image Load
print(type(img))
# <class 'numpy.ndarray'>
print(img.shape)
# (356, 493, 3)

# # Check Image
# # cv2_imshow(img) # Google colabでない場合は、cv2.imshowを使う
# cv2.imshow('img',img) # Google colabでない場合は、cv2.imshowを使う
# cv2.waitKey(0)  # Wait for a key press to close the window
# cv2.destroyAllWindows()