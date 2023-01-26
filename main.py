'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.
#VERSION: 1.0.6
#AUTHOR: Marshall Burns a.k.a Schooly B


####!!!---KNOWN ISSUES:     ---!!!###
# THE RENAME_FILE() FUNCTION IS BUGGED


###IMPORT 'TKINTER', 'OS', 'SHUTIL', AND 'SUBPROCCESS' ###
###IMPORT 'FILEDIALOG' AND 'MESSAGEBOX'###

from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import os
import shutil
import subprocess


###DECLARING OPEN_FILE()FUNCTION###
def open_file():
    
    file = fd.askopenfilename(title='Choose a file of any type', filetypes=[('All files', "*.*")])
    subprocess.call(['xdg-open', file])

###DECLARING COPY_FILE()FUNCTION###
def copy_file():
    fileSource = fd.askopenfilename(title='choose a file to copy', filetypes=[('All files', '*.*')])
    fileDestination = fd.askdirectory(title='Which folder would you like to place this file?')

    try:
        shutil.copy(fileSource, fileDestination)
        mb.showinfo(title='File Copied!',message='Your file has been moved to')
    except:
        mb.showerror(
            title='Error!', message='We were unable to copy your file, Please try again')

###DECLARING DELETE_FILE()FUNCTION###
def delete_file():
    file = fd.askopenfilename(title='Choose a file to delete', filetypes=[("All files", "*.*")])
    os.remove(os.path.abspath(file))
    mb.showinfo(title='File deleted',message='Your desired file has been deleted')

###DECLARING RENAME_FILE()FUNCTION###   
def rename_file():
    file = fd.askopenfilename(title='Choose a file to rename', filetypes=[("All files", "*.*")])
    rename_wn = Toplevel(root)
    rename_wn.title("Rename the file to")
    rename_wn.geometry("250x70")
    rename_wn.resizable(0, 0)
    Label(rename_wn, text='What should be the new name of the file?',font=("Times New Roman", 10)).place(x=0, y=0)
    new_name = Entry(rename_wn, width=40, font=("Times New Roman", 10))
    new_name.place(x=0, y=30)
    new_file_name = os.path.join(os.path.dirname(file), new_name.get()+os.path.splitext(file)[1])
    os.rename(file, new_file_name)
    mb.showinfo(title="File Renamed",message='Your desired file has been renamed')

###DECLARING OPEN_FOLDER()FUNCTION###
def open_folder():
    folder = fd.askdirectory(title="Select Folder to open")
    subprocess.call(['xdg-open', folder])

###DECLARING DELETE_FOLDER()FUNCTION###
def delete_folder():
    folderToDelete = fd.askdirectory(title='Choose a folder to delete')
    os.rmdir(folderToDelete)
    mb.showinfo("Folder Deleted", "Your desired folder has been deleted")

###DECLARING MOVE_FOLDER()FUNCTION###
def move_folder():
    sourceFolder = fd.askdirectory(title='Select the folder you want to move')
    mb.showinfo(message='You just selected the folder to move, now please select the desired destination where you want to move the folder to')
    destinationFolder = fd.askdirectory(title='Where to move the folder to')
    try:
        shutil.move(sourceFolder, destinationFolder)
        mb.showinfo("Folder moved", 'Your desired folder has been moved to the location you wanted')
    except:
        mb.showerror('Error', 'We could not move your folder. Please make sure that the destination exists')

###DECLARING LIST_FILES_IN_FOLDER()FUNCTION###
def List_File_In_Folder():
    i = 0

    folder = fd.askdirectory(title='Select the folder twhose files you want to list.')
    files = os.listdir(os.path.abspath(folder))

    list_files_wn = Toplevel(root)
    list_files_wn.title(f'Files in {folder}')
    list_files_wn.geometry('250x250')
    list_files_wn.resizable(0, 0)

    listbox = Listbox(list_files_wn, selectbackground='SteelBlue', font=("Georgia", 10))
    listbox.place(relx=0, rely=0, relheight=1, relwidth=1)

    scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox.config(yscrollcommand=scrollbar.set)

    while i < len(files):
        listbox.insert(END, files[i])
        i += 1


title = "Direct'O'Tron"
background = 'White'
button_font = ("Times New Roman", 13)
button_background = 'Gray'


root = Tk()
root.title(title)
root.geometry('250x400')
root.resizable(0, 0)
root.config(bg=background)


###CREATING POP UP WINDOW AND PLACING COMMANDS IN THEM###
Label(root, text=title, font=("Comic Sans MS", 15),
      bg=background, wraplength=250).place(x=20, y=0)
Button(root, text='Open a file', width=20, font=button_font,
       bg=button_background, command=Open_File).place(x=30, y=50)
Button(root, text='Copy a file', width=20, font=button_font,
       bg=button_background, command=Copy_File).place(x=30, y=90)
Button(root, text='Rename a file', width=20, font=button_font,
       bg=button_background, command=Rename_File).place(x=30, y=130)
Button(root, text='Delete a file', width=20, font=button_font,
       bg=button_background, command=Delete_File).place(x=30, y=170)
Button(root, text='Open a folder', width=20, font=button_font,
       bg=button_background, command=Open_Folder).place(x=30, y=210)
Button(root, text='Delete a folder', width=20, font=button_font,
       bg=button_background, command=Delete_Folder).place(x=30, y=250)
Button(root, text='Move a folder', width=20, font=button_font,
       bg=button_background, command=Move_Folder).place(x=30, y=290)
Button(root, text='List all files in a folder', width=20, font=button_font,
       bg=button_background, command=List_Files_In_Folder).place(x=30, y=330)

# Finalizing the window###

root.update()
root.mainloop()
