import tkinter as tk
from tkinter import filedialog, messagebox
import os
import qrcode
from PIL import Image 

def generar_qr():
    url = entrada_url.get().strip()
    nombre_imagen = entrada_nombre.get().strip()
    nombre_carpeta = entrada_carpeta.get().strip()

    # URL Validation
    if not url.startswith(('http://', 'https://')):
        messagebox.showerror("Error", "La URL debe comenzar con http:// o https://")
        return
    
    # Image name validation
    if not nombre_imagen.replace('.jpg', '').isalnum():
        messagebox.showerror("Error", "El nombre solo puede contener letras y números")
        return

    if not url or not nombre_imagen or not nombre_carpeta:
        messagebox.showerror("Error", "Por favor, completa todos los campos para crear el código QR.")
        return

    if not nombre_imagen.lower().endswith('.jpg'):
        nombre_imagen += '.jpg'

    try:
        if not os.path.exists(nombre_carpeta):
            os.makedirs(nombre_carpeta)

        ruta = os.path.join(nombre_carpeta, nombre_imagen)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=12,
            border=2,
        )
        qr.add_data(url)
        qr.make(fit=True)
        imagen = qr.make_image(fill_color="black", back_color="white")
        imagen.save(ruta)

        if os.path.exists(ruta):
            messagebox.showinfo("Éxito", f"Código QR guardado en:\n{ruta}")
        else:
            messagebox.showerror("Error", "La imagen no se guardó correctamente.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error:\n{e}")

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    if carpeta:
        entrada_carpeta.delete(0, tk.END)
        entrada_carpeta.insert(0, carpeta)

ventana = tk.Tk()
ventana.title("QR Generator")
ventana.geometry("600x250")
ventana.resizable(False, False)

fuente = ("Segoe UI", 12)

tk.Label(ventana, text="URL:", font=fuente).grid(row=0, column=0, sticky='e', padx=10, pady=10)
entrada_url = tk.Entry(ventana, width=50, font=fuente)
entrada_url.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

tk.Label(ventana, text="Nombre del archivo:", font=fuente).grid(row=1, column=0, sticky='e', padx=10, pady=10)
entrada_nombre = tk.Entry(ventana, width=50, font=fuente)
entrada_nombre.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

tk.Label(ventana, text="Carpeta de destino:", font=fuente).grid(row=2, column=0, sticky='e', padx=10, pady=10)
entrada_carpeta = tk.Entry(ventana, width=40, font=fuente)
entrada_carpeta.grid(row=2, column=1, padx=10, pady=10)

tk.Button(ventana, text="Seleccionar", command=seleccionar_carpeta, font=fuente).grid(row=2, column=2, padx=10)

tk.Button(ventana, text="Generar", command=generar_qr,
          font=("Segoe UI", 13, "bold"), bg="#4CAF50", fg="black").grid(row=3, column=1, columnspan=2, pady=20)

ventana.mainloop()
