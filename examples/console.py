from tkinter import *
def Insert():
    	name = text.get()
    	Text.insert(END, name)
    	text.delete(0,END)	
    
root = Tk()
root.geometry('300x300')
 
text = Entry(root, bg = 'white')

Text = Listbox(root)
Text.pack(anchor = S)
  
text.pack(anchor = S)


def delete():
  Text.delete(0,END)
Text = Listbox(Text)
Text.pack()


  
Button1 = Button(root, text="ENTRY", width=10, command=Insert)
Button2 = Button(root, text="Clear", width=10, command=delete)
Button3 = Button(root, text='Exit', width=10, command=root.destroy)

Button1.pack()
Button2.pack()
Button3.pack()
Button1.place(x=20, y=190)
Button2.place(x=100, y=190)
Button3.place(x=180, y=190)

root.mainloop()
  	
