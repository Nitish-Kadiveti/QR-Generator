import tkinter as tk
from tkinter import messagebox
import qrcode


def generate_qr_code():
    # Get the data from the entry fields
    data = entry_data.get()
    name = entry_name.get()

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image with the given name
    qr_img.save(name + ".png")

    # Show a success message
    messagebox.showinfo(
        "Success", "QR code generated and saved as " + name + ".png")


# Create the main window
window = tk.Tk()
window.title("QR Code Generator")

# Create a label and an entry field for the data
label_data = tk.Label(window, text="Data:")
label_data.pack()
entry_data = tk.Entry(window, width=30)
entry_data.pack(pady=5)

# Create a label and an entry field for the QR code name
label_name = tk.Label(window, text="QR Code Name:")
label_name.pack()
entry_name = tk.Entry(window, width=30)
entry_name.pack(pady=5)

# Create a button to generate the QR code
generate_button = tk.Button(
    window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

window.mainloop()