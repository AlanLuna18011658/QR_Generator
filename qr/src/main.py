import os
import qrcode

nombre_imagen = 'name_qr.jpg'
nombre_carpeta = 'img'

if not os.path.exists(nombre_carpeta):
    os.makedirs(nombre_carpeta)

ruta = os.path.join(nombre_carpeta, nombre_imagen)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,  
    border=2,     
)
url = 'URL'
qr.add_data(url)
qr.make(fit=True)
imagen = qr.make_image()
imagen.save(ruta)
