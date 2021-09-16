import tkinter


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
ls_btn   = tkinter.Button(input_frame,text="Add Item",bg=btn_color,font=main_font)

ls_entry.grid(row=0,column=0,pady=(20,5),ipady=3)
ls_btn.grid(row=0,column=1,pady=(20,5),padx=5)
root.mainloop()