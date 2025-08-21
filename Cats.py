from tkinter import *
import requests 
from PIL import Image,ImageTk
from io import BytesIO
from tkinter import Toplevel
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
def open_new_window():
    tag=tag_entru.get()
    url_tag=f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img=load_image(url_tag)
    if img:
        new_window = Toplevel()
        new_window.title("cat")
        new_window.geometry("600x500")
        label = Label(new_window, image=img)
        label.pack()
        label.image=img
def exit():
    window.destroy()


window =Tk()
window.title("cat")
window.geometry("600x600")
tag_entru=Entry()
tag_entru.pack()

load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

# update_button = Button(text="update",command=set_image)
# update_button.pack()
url='https://cataas.com/cat'


window.mainloop()


