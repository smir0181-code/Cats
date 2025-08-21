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
        img.thumbnail((600, 500), Image.Resampling.LANCZOS)
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
def exit():
    window.destroy()


window =Tk()
window.title("cat")
window.geometry("600x600")
label = Label()
label.pack()
menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=set_image)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

# update_button = Button(text="update",command=set_image)
# update_button.pack()
url='https://cataas.com/cat'
set_image()


window.mainloop()


