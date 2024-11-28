"""Colab用"""

# 1. Image Open
from google.colab import files
from PIL import Image

# ファイルアップロード
uploaded_file = files.upload()
input_path = next(iter(uploaded_file))

# pillow形式で画像読み込み
image = Image.open(input_path)
image

# 2.背景削除
from rembg import remove

# 背景除去
result = remove(image)
result
