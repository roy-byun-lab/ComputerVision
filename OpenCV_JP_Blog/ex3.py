"""
参考：https://take-tech-engineer.com/category/python/opencv/
ex1とex2の引継ぎ
Resize
"""
import cv2
# RGB to RGR
image = cv2.cvtColor(cv2.imread("butterfly.jpg"), cv2.COLOR_BGR2RGB)
# Check size
print(image.shape)

# Resize
image_re = cv2.resize(src=image, dsize=(100, 200))
# Check size
print(image_re.shape)
# # check Image
# cv2.imshow('image',image)
# cv2.imshow('image_re',image_re) # Google colabでない場合は、cv2.imshowを使う
# cv2.waitKey(0)  # Wait for a key press to close the window
# cv2.destroyAllWindows()

# 倍率でリサイズ
image_re2 = cv2.resize(src=image, dsize=None, fx=2, fy=1)
# Check size
print(image_re2.shape)
# check Image
# cv2.imshow('image',image)
# cv2.imshow('image_re2',image_re2) # Google colabでない場合は、cv2.imshowを使う
# cv2.waitKey(0)  # Wait for a key press to close the window
# cv2.destroyAllWindows()