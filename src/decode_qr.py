from pyzbar.pyzbar import decode
from PIL import Image

# Load the image
img = Image.open('generated_qrcodes/python_01.png')

# Decode the QR code
decoded_objects = decode(img)

for obj in decoded_objects:
    # Print the data (it returns bytes, so we decode it to a string)
    print(f"Type: {obj.type}")
    print(f"Data: {obj.data.decode('utf-8')}")