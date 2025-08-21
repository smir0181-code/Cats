from tkinter import *
import requests 
from PIL import Image,ImageTk
from io import BytesIO
def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        #img = img.resize((200, 200), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        return img
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None
def set_image():
    img=load_image(url)
    if img:
    # img=ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image=img


window =Tk()
window.title("cat")
window.geometry("600x500")
label = Label()
label.pack()
update_button = Button(text="update",command=set_image)
url='https://cataas.com/cat'
set_image()


window.mainloop()


