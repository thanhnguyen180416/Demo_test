from tkinter import *
from tkinter import filedialog
from tkinter import ttk
i = 1

def hoc():
    global i
    global radio_test
   
    print('Da Nhan vao button hoc')
    Radiobutton(group1, text='Vi tri:' + str(i), variable=radio_test, value=i, command=pr).grid(row=i+1, column=0, sticky=W+N)
    i=i+1
def pr():
    vt = radio_test.get()
    print('Vi tri duoc chon:'+str(vt) )
    selection = "Vi Tri Duoc Chon: " + str(vt)
    lbl_test.config(text = selection)

def dichuyen():
    vt = radio_test.get()
    print('di chuyen den: '+ str(vt))


root = Tk()
# Group1 Frame ----------------------------------------------------

radio_test = IntVar()
group1 = LabelFrame(root, text="Arar", padx=50, pady=50)
group1.grid(row=0, column=0, padx=10, pady=10, sticky=E+W+N+S)

btn_test = Button(group1,text="Hoc", command=hoc, height=2, width=10)
btn_test.grid(row=1, column=0, columnspan=2)
btn_test = Button(group1,text="Di Chuyen", command=dichuyen, height=2, width=10)
btn_test.grid(row=1, column=2, columnspan=2)

lbl_test = Label(group1, text = "Vi Tri Duoc Chon:")
lbl_test.grid(row = 0, column = 0, sticky=W)


group2 = LabelFrame(root, text="Dieu Khien", padx=50, pady=50)
group2.grid(row=0, column=1, padx=10, pady=10, sticky=E+W+N)
btn_len = Button(group2,text="Len", command='', height=2, width=5)
btn_len.grid(row=1, column=2, columnspan=2)
btn_trai = Button(group2,text="Trai", command='', height=2, width=5)
btn_trai.grid(row=2, column=0, columnspan=2)
btn_xuong = Button(group2,text="Xuong", command='', height=2, width=5)
btn_xuong.grid(row=2, column=2, columnspan=2)
btn_phai = Button(group2,text="Phai", command='', height=2, width=5)
btn_phai.grid(row=2, column=4, columnspan=2)

root.mainloop()