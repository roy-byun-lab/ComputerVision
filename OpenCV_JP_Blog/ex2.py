"""
参考：https://take-tech-engineer.com/category/python/opencv/
ex1の引継ぎ
    グレースケール活用
"""
import cv2
# from google.colab.patches import cv2_imshow # Google colab用

img = cv2.imread("butterfly.jpg", cv2.IMREAD_GRAYSCALE)

print(type(img))
# <class 'numpy.ndarray'>
print(img.shape)
# (356, 493)

# # Check Image
# # cv2_imshow(img) # Google colabでない場合は、cv2.imshowを使う
# cv2.imshow('img',img) # Google colabでない場合は、cv2.imshowを使う
# cv2.waitKey(0)  # Wait for a key press to close the window
# cv2.destroyAllWindows()

# save
cv2.imwrite("butterfly_gray.jpg", img)