# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "D:\Grocery Billing System\mypdf.pdf"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.png('myqrnew.png', scale = 6)