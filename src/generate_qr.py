import qrcode
import os
import qrcode.image.svg

# 1. Define your folder and file name
folder_name = "generated_qrcodes"
file_name = "custom_qr.png"

# 2. Combine them into a full path safely
full_path = os.path.join(folder_name, file_name)

# 3. Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

# 1. Create a QRCode object
qr = qrcode.QRCode(
    version=None, # Controls the size of the QR Code (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H, # High error correction
    box_size=10, # How many pixels each "box" of the QR code is
    border=4,  # Thickness of the border (quiet zone) in boxes
)

# 2. Add data
qr.add_data('https://www.python.org')
qr.make(fit=True) # 'fit=True' automatically figures out the best size

# 3. Create an image from the QR Code instance
# You can change the colors here!
img = qr.make_image(fill_color="black", back_color="lightyellow")

# 4. Save the image
img.save(full_path)

print(f"QR code saved successfully to: {os.path.abspath(full_path)}")

# Generate the SVG
# Use the SvgPathImage factory for better scaling
# factory = qrcode.image.svg.SvgPathImage
# img = qr.make_image(image_factory=factory)
# img.save(full_path)
# print(f"QR code saved successfully to: {os.path.abspath(full_path)}")