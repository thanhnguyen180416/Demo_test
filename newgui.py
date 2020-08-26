from tkinter import *
from tkinter import filedialog
from tkinter import ttk

def test():
    print('Bạn đã ấn vào button ' + etr_a.get())
    global a
    a = int(etr_a.get())
    global radio_test
    radio_test = IntVar()
    radio_huong = IntVar()
    for i in range(a):
        Radiobutton(group1, text='Lựa chọn ' + str(i+1), variable=radio_test, value=i+1).grid(row=i+2, column=1, sticky=W+N)
    lbl_test = Label(group1, text = "Chọn Hướng:")
    lbl_test.grid(row = a+2, column = 0, sticky=W)
    Radiobutton(group1, text='Trai ', variable=radio_huong, value='trai').grid(row=a+3, column=1, sticky=W+N)
    Radiobutton(group1, text='Phai ', variable=radio_huong, value='phai').grid(row=a+3, column=2, sticky=W+N)
    Radiobutton(group1, text='Len ', variable=radio_huong, value='len').grid(row=a+4, column=1, sticky=W+N)
    Radiobutton(group1, text='Xuong ', variable=radio_huong, value='xuong').grid(row=a+4, column=2, sticky=W+N)        

    btn_test = Button(group1, text="Di Chuyển", command= Dichuyen, height=2)
    btn_test.grid(row=1, column=3, columnspan=1)

def Dichuyen():
    print('vi tri ' + str(radio_test.get()))

def showr():
    print(scale_widget.get())





root = Tk()
# Group1 Frame ----------------------------------------------------
#root.geometry('600x400')

group1 = LabelFrame(root, text="Chọn vị trí Robot", padx=40, pady=40)
group1.grid(row=0, column=0, padx=20, pady=20, sticky=E+W+N+S)

lbl_setup = Label(group1, text = "Setup", font=("Arial Bold", 20))
lbl_setup.grid(row = 0, column = 1, sticky=W)

lbl_test = Label(group1, text = "Nhập số vị trí: ")
lbl_test.grid(row = 1, column = 0, sticky=W)

_default_value = StringVar(root, value='0')
etr_a = Entry(group1, width = 15, textvariable=_default_value)
etr_a.grid(row = 1, column = 1, sticky=W)

btn_test = Button(group1, text="Chọn", command=test, height=2)
btn_test.grid(row=1, column=2, columnspan=1)

# scale_widget = Scale(root, orient="horizontal", resolution=1,from_=0, to=100)
# scale_widget.grid(row=0, column=3)
# btn_show = Button(root, text="show", command=showr, height=2)
# btn_show.grid(row=0, column=4, columnspan=1)

root.mainloop()