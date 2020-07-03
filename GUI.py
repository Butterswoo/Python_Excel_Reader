import pandas as pd
from openpyxl.workbook import Workbook
from tkinter import *
from tkinter import messagebox

def test_function(entry):
    print('This is the entry:', entry)

def selected():
    mylabel = Label(root, text=clicked.get()).pack()
    
    list_a.append(clicked.get())
    print(list_a)

def excel_reader(entry):
    if len(entry) == 0:
        messagebox.showinfo("Message", "Input cannot be empty!")
    else:
        global total_verbatim, lists        #why global
        for item in list_a:
            lists.append(data_dict[item])
            lists = list(dict.fromkeys(lists))
        print(lists)    
        for xlsx_list in lists:
            df = pd.read_excel(xlsx_list)

            verbatim = df[df['Verb English'].str.lower().str.contains(entry, na = False)][['Verb English', 'Model Year']]   # prevent none input
            #print(verbatim)
            total_verbatim = total_verbatim.append(verbatim)   # why can't just total_verbatim.append(verbatim)
        print(total_verbatim)
        stored = total_verbatim.to_excel('verbatims.xlsx')

list_a = []
lists = []

# add excel file in the future
data_dict = {'2017 GQRS Ford':'cars test.xlsx', '2018 GQRS Ford':'cars.xlsx', '2019 GQRS Ford':'cars 3.xlsx', '2020 GQRS Ford':'cars 4.xlsx'}

total_verbatim = pd.DataFrame()

# add color/background in future
root = Tk()
root.title('GQRS-NPS-JDP data!')
root.geometry("500x500")

# update name here as well
options = ['2017 GQRS Ford', '2018 GQRS Ford', '2019 GQRS Ford', '2020 GQRS Ford']

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack(pady=20)

button1 = Button(root, text='Load Database', command=lambda: selected())
button1.pack()

entry = Entry(font=40)
entry.place(relx=0.25, rely=0.5, relwidth=0.5,relheight=0.1)

button2 = Button(text='Run query', command=lambda: excel_reader(entry.get()))
button2.place(relx=0.3, rely=0.6, relwidth=0.4,relheight=0.1)

root.mainloop()