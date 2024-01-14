from tkinter import Tk, ttk
from tkinter import *

from PIL import Image, ImageTk

#screen
root = Tk()
root.title("Currency GLobal Money Converter")
root.geometry("800x450")
root.configure(bg='#FFFFFF')
#root.resizable()

#color
color1="#FFFFFF" #WHITE
color2="#333333" #BLACK
color3="#EB5D51" #RED

#frames
top = Frame(root,width=350,height=100,bg=color3)
top.grid(row=0, column=0)

main = Frame(root,width=300,height=300,bg=color1)
main.grid(row=1, column=0)

#top frame
icon = Image.open('money-exchange.png')
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image = icon, compound=LEFT, text = "Currency Converter", height=5, padx=40, pady=30, anchor=CENTER, font=('Roboto',15), bg=color3, fg=color1)
app_name.place(x=0,y=0)

#main frame
result = Label(root,text = " ", width= 16,height=2, padx=13, pady=7,relief="solid", anchor=CENTER, font=('Roboto',17),bg=color1, fg=color2)
result.place(x=40,y=350)

#currency- add more currency
currency = ['AED', 'USD', 'EURO', 'GBP', 'PESO', 'YEN']

#from
exchange_label =  Label(top, width= 8,height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Roboto',10), bg=color1, fg=color1)
exchange_label.place(x=40, y=150)

#the choices from what do you want to exchange
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Roboto 12 bold'))
combo1['values'] = (currency)
combo1.place(x=5, y=40)

#to
exchangeto_label =  Label(top, width= 8,height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Roboto',10), bg=color1, fg=color1)
exchangeto_label.place(x=80, y=150)

#the choices from what do you want to exchange part 2
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=('Roboto 12 bold'))
combo2['values'] = (currency)
combo2.place(x=190, y=40)

#the amount
# THE TEXT AMOUNT IS NOT VISIBLE!!
value = Entry(root, text="Amount", width=20, justify=CENTER, font=("Arial 15 bold"), relief=SOLID)
value.place(x=50,y=220)

#button/convert now
button = Button(main,text="Convert now", width=19, padx=5, height=1, bg=color3, fg=color1, font=("Roboto 12 bold"))
button.place(x=30, y=190)

root.mainloop()

