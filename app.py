import tkinter
from tkinter import END
from tkinter import font
from tkinter.constants import ANCHOR


#define window
root = tkinter.Tk()
root.title("Checklist")
root.iconbitmap("checklist_icon.ico")
root.geometry("400x400")
root.resizable(0,0)

#define fonts and colors
main_font = ("Times New Roman",12)
main_color = "#BBA191"
btn_color = "#DDD0C8"

root.config(bg=main_color)

#define functions
count = 0
def add_item():
    global count
    if(ls_entry.get() == ""):
        return
    ls_listbox.insert(END,ls_entry.get())
    if (count % 2 == 0):
        ls_listbox.itemconfig(count,{'bg':'#f1ece9'})
        count += 1
    else :
        ls_listbox.itemconfig(count,{'bg':'#ddd0c8'})
        count += 1
    
    ls_entry.delete(0,END)

def rm_item():
    global count
    #remove item from listbox with the help of ANCHOR
    ls_listbox.delete(ANCHOR)
    count -= 1
#--define layout--#
#Create frames
input_frame = tkinter.Frame(root,bg=main_color)
output_frame = tkinter.Frame(root,bg=main_color)
button_frame = tkinter.Frame(root,bg=main_color)

input_frame.pack()
output_frame.pack()
button_frame.pack()


#input_frame
ls_entry = tkinter.Entry(input_frame,width=35,font=main_font)
ls_btn   = tkinter.Button(input_frame,text="Add Item",bg=btn_color,font=main_font,command=add_item)


ls_entry.grid(row=0,column=0,pady=(20,5),ipady=3)
ls_btn.grid(row=0,column=1,pady=(20,5),padx=5)

#output frame layout
ls_listbox_scrollbar = tkinter.Scrollbar(output_frame)
#@,yscrollcommand=ls_listbox_scrollbar.set : scrollbar activated if we have enough items
ls_listbox = tkinter.Listbox(output_frame,height=15,width=45,borderwidth=2,font=main_font,yscrollcommand=ls_listbox_scrollbar.set)
ls_listbox.grid(row=0,column=0)

#link scrollbar to listbox
ls_listbox_scrollbar.config(command=ls_listbox.yview)
ls_listbox_scrollbar.grid(row=0,column=1,sticky="NS")

#btn frame layout
ls_remove_btn = tkinter.Button(button_frame,text="Remove Item",bg=btn_color,font=main_font,command=rm_item)
ls_clear_btn = tkinter.Button(button_frame,text="Clear List",bg=btn_color,font=main_font)
ls_save_btn = tkinter.Button(button_frame,text="Save List",bg=btn_color,font=main_font)

ls_remove_btn.grid(row=0,column=0,padx=10)
ls_clear_btn.grid(row=0,column=1,padx=10,ipadx=20)
ls_save_btn.grid(row=0,column=2,padx=10,ipadx=20)
root.mainloop()