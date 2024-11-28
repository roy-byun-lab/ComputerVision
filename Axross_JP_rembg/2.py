"""一般"""
# pip install onnxruntime
# u2net.onnx Model 自動DL
    # Path C:\Users\PCName\.u2net\u2net.onnx

from rembg import remove
from PIL import Image
import io

# Set Path
input_path = 'test.png'
output_path = 'output_image.png'

# Open Image File
with open(input_path, 'rb') as input_file:
    input_image = input_file.read()

# Remove Background
output_image = remove(input_image)

# Save Output
with open(output_path, 'wb') as output_file:
    output_file.write(output_image)

# Check
img = Image.open(io.BytesIO(output_image))
img.show()
