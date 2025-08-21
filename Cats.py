from tkinter import *
import requests 
from PIL import ImageTk, Image
from io import BytesIO
window =Tk()
window.title("Weather App")
window.geometry("500x500")
label = Label()
label.pack()
url='https://cataas.com/cat'
img=load_image(url)
if img:
    # img=ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image=img
window.mainloop()


