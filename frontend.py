from tkinter import *
import backend

root=Tk()
root.geometry()
root.title("My favorite movies")

titlevar=StringVar()
genrevar=StringVar()
yearvar=StringVar()
runtimevar=StringVar()

def Clear():
    titlevar.set("")
    genrevar.set("")
    yearvar.set("")
    runtimevar.set("")

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple = list1.get(index)
    titleEntry.delete(0,END)
    titleEntry.insert(END,selected_tuple[1])
    genreEntry.delete(0, END)
    genreEntry.insert(END,selected_tuple[2])
    yearEntry.delete(0, END)
    yearEntry.insert(END,selected_tuple[3])
    runtimeEntry.delete(0,END)
    runtimeEntry.insert(END,selected_tuple[4])
#    runtimeEntry.insert(END,'{}' .format(selected_tuple[4]))


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)


def AddMovie():
    backend.insert(titlevar.get(),genrevar.get(),yearvar.get(),runtimevar.get())
    list1.delete(0, END)
    list1.insert(END, (titlevar.get(), genrevar.get(), yearvar.get(), runtimevar.get()))


def search_movie():
    list1.delete(0,END)
    for row in backend.search(titlevar.get(),genrevar.get(),yearvar.get(),runtimevar.get()):
        list1.insert(END,row,str(""))

def delete_movie():
    backend.delete(selected_tuple[0])
#    list1.delete(0, END)
    view_command()

def update_movie():
    backend.update(selected_tuple[0],titlevar.get(),genrevar.get(),yearvar.get(),runtimevar.get())
    view_command()

l1=Label(root,text="Add Your Favorite Movies",  font=('arial',30, 'bold'), bd=21,bg='light goldenrod yellow',
                fg='black',justify=CENTER,relief=RIDGE)
l1.grid(row=0,column=0)

AddFrame=Frame(root,bg='light goldenrod yellow', bd=10, relief=RIDGE )
AddFrame.grid()

Buttons=Frame(root,bg='light goldenrod yellow', bd=10, relief=RIDGE )
Buttons.grid()

MoviesList=Frame(root,bg='light goldenrod yellow', bd=10, relief=RIDGE)
MoviesList.grid()

titlel1=Label(AddFrame,text="Add Title",  font=('arial',18, 'bold'), width=17,  bd=6,bg='light goldenrod yellow',
                fg='black',relief=RIDGE)
titlel1.grid(row=0,column=0)


titleEntry=Entry(AddFrame,font=('arial', 16,'bold'),  bd=7, width=17, justify='left',textvariable=titlevar)
titleEntry.grid(row=0,column=1)

genrel=Label(AddFrame,text="Add Genre",  font=('arial',18, 'bold'), width=17,  bd=6,bg='light goldenrod yellow',
                fg='black',relief=RIDGE)
genrel.grid(row=1,column=0)

genreEntry=Entry(AddFrame,font=('arial', 16,'bold'),  bd=7, width=17, justify='left',textvariable=genrevar)
genreEntry.grid(row=1,column=1)

yearl=Label(AddFrame,text="Add Year",  font=('arial',18, 'bold'), width=17,  bd=6,bg='light goldenrod yellow',
                fg='black',relief=RIDGE)
yearl.grid(row=2,column=0)

yearEntry=Entry(AddFrame,font=('arial', 16,'bold'),  bd=7, width=17, justify='left', textvariable=yearvar)
yearEntry.grid(row=2,column=1)

runtimel=Label(AddFrame,text="Add Runtime",  font=('arial',18, 'bold'), width=17,  bd=6,bg='light goldenrod yellow',
                fg='black',relief=RIDGE)
runtimel.grid(row=3,column=0)

runtimeEntry=Entry(AddFrame,font=('arial', 16,'bold'),  bd=7, width=17, justify='left',textvariable=runtimevar)
runtimeEntry.grid(row=3,column=1)

AddButton =Button(Buttons, padx=16,pady=1,bd=6,fg="black", font=('arial', 14,'bold'), width=5, text="Add movie"
                 ,bg="light goldenrod yellow" , command=AddMovie).grid(row=0, column=0)
DeleteButton =Button(Buttons, padx=16,pady=1,bd=7,fg="black", font=('arial', 14,'bold'), width=4, text="Delete"
                 ,bg="light goldenrod yellow" , command=delete_movie).grid(row=0, column=1)
Update =Button(Buttons, padx=16,pady=1,bd=7,fg="black", font=('arial', 14,'bold'), width=4, text="Update"
                 ,bg="light goldenrod yellow" , command=update_movie).grid(row=0, column=2)
ViewAll =Button(Buttons, padx=16,pady=1,bd=7,fg="black", font=('arial', 14,'bold'), width=4, text="View all"
                 ,bg="light goldenrod yellow" , command=view_command).grid(row=0, column=3)
Search =Button(Buttons, padx=16,pady=1,bd=7,fg="black", font=('arial', 14,'bold'), width=4, text="Search"
                 ,bg="light goldenrod yellow" , command=search_movie).grid(row=0, column=4)
clear =Button(Buttons, padx=16,pady=1,bd=7,fg="black", font=('arial', 14,'bold'), width=4, text="Clear"
                 ,bg="light goldenrod yellow" , command=Clear).grid(row=1, column=2)

list1=Listbox(MoviesList,height=10,width=81,bd=7,bg='light goldenrod yellow',font=('arial',8,'bold'))
list1.grid(row=2,column=0)

sb1=Scrollbar(MoviesList,orient=VERTICAL,bg='light goldenrod yellow')
sb1.grid(row=2,column=2,sticky='ns')

list1.bind('<<ListboxSelect>>',get_selected_row)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)



root.mainloop()