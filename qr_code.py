from tkinter import*
import qrcode
from PIL import Image,ImageTk

root =Tk()
root.title("QR Code Generator")

def generate_qr():
    qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4)
    qr.add_data(entry.get())
    qr.make(fit=True)
    img=qr.make_image(fill_color="blue",back_colors="white")
    # img=img.resize((300,300),Image.ANTIALIAS)
    qr_img=ImageTk.PhotoImage(img)
    qr_label.config(image=qr_img)
    qr_label.image=qr_img

entry=Entry(root,font=("Helvatica",18))
entry.pack(pady=20)

generate_button=Button(root,text="Generate QR Code",command=generate_qr)
generate_button.pack(pady=20)

qr_label=Label(root)
qr_label.pack(pady=20)

root.mainloop()