import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Version 1 is a 21x21 matrix
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,  # Size of each "box" in the QR code
    border=10,    # Border size (adjust as needed)
)

# Provide the data you want to encode
data_to_encode = "Hello, QR Code!"

# Step 5: Add data to the QR code
qr.add_data(data_to_encode)
qr.make(fit=True)

#Create an Image object from the QR code instance
img = qr.make_image(fill_color="black", back_color="pink")

#Save or display the QR code
img.save("my_qr_code.png")  # Save the QR code to a file
img.show()  # Display the QR code using the default image viewer
