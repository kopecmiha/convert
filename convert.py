from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from PIL import Image, ImageTk
import os
from tkinter import Tk, Button, Label, Entry, IntVar, filedialog, messagebox
from tkinter.ttk import Radiobutton
import time

d = {0: ".jpg", 1: ".png"}
def convert_prop(path):
    img = Image.open(os.path.abspath(path))
    wide, high = img.size 
    res = wide/high 
    s = 36000
    max_wide = int((s*res)**(1/2))
    max_high = int(s/max_wide)
    resized_img = img.resize((max_wide, max_high))
    resized_img.save("propimage.jpg")


def convert(wide, high, rasr):
    image = Image.open(os.path.abspath(file))
    max_wide = int(wide)
    max_high = int(high)
    resized_image = image.resize((max_wide, max_high))
    img_name = "convert-image" + str(time.time()) + rasr
    resized_image.save(img_name)
    messagebox.showinfo("Успешно", "Конвертированная картинка сохранена под именем:" +img_name)
    img.destroy()
    txthigh.delete(0,'end')
    txtwide.delete(0,'end')

def clicked(): 
        wide = txtwide.get()
        high = txthigh.get()
        rasr = d[select.get()]
        convert(wide, high, rasr)

def clean():
    img.destroy()

def openfile():
    global file
    global img
    img = None
    file = filedialog.askopenfilename()
    convert_prop(file)
    load = Image.open("propimage.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render)
    img.image = render
    img.place(x=200, y=0)
    os.remove("propimage.jpg")


window = Tk()

window.title("Image Converter v1.0")
window.geometry('800x600')

lblresol = Label(window, text="Введите разрешение")  
lblresol.grid(column=0, row=2)

lblwide = Label(window, text="Width")
lblwide.grid(column=0, row=3)
txtwide = Entry(window,width=10)  
txtwide.grid(column=1, row=3)

lblhigh = Label(window, text="Height")  
lblhigh.grid(column=0, row=4)
txthigh = Entry(window,width=10)  
txthigh.grid(column=1, row=4)

lblras = Label(window, text="Выберите расширение")  
lblras.grid(column=0, row=5)

select = IntVar() 
rad1 = Radiobutton(window,text='.jpg', value=0, variable=select)  
rad2 = Radiobutton(window,text='.png', value=1, variable=select)
rad1.grid(column=0, row=6)  
rad2.grid(column=0, row=7)  



btn = Button(window, text="Конвертировать", command=clicked)  
btn.grid(column=0, row=8)  

btnfile = Button(window, text="Открыть Файл", command=openfile)  
btnfile.grid(column=0, row=0)
'''
btnfile = Button(window, text="Очистить", command=clean)  
btnfile.grid(column=0, row=10)
'''
window.mainloop()

