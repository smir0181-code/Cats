from tkinter import *
import requests 
from PIL import ImageTk, Image
from io import BytesIO
def load_image():
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(BytesIO(img_data))
        img = img.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        return img
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None
window =Tk()
window.title("cat")
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


