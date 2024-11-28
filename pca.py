import tkinter as tk
from tkinter import PhotoImage
import subprocess
import os
setpfn = 1
def st():
    if setpfn == 1:
        subprocess.Popen('python main.py', creationflags=subprocess.CREATE_NO_WINDOW)
        exit()
    if setpfn == 2:
        subprocess.Popen('python main2.py', creationflags=subprocess.CREATE_NO_WINDOW)
        exit()
    if setpfn == 3:
        subprocess.Popen('python main3.py', creationflags=subprocess.CREATE_NO_WINDOW)
        exit()
    if setpfn == 4:
        subprocess.Popen('python main4.py', creationflags=subprocess.CREATE_NO_WINDOW)
        exit()
    if setpfn == 5:
        subprocess.Popen('python maincognito.py', creationflags=subprocess.CREATE_NO_WINDOW)
        exit()
def setpfn1():
    global setpfn
    setpfn = 1
    w = open('PCC.txt','w')
    w.write('True')
    w.close()
    st()
def setpfn2():
    global setpfn
    setpfn = 2
    w = open('PCC.txt', 'w')
    w.write('True')
    w.close()
    st()
def setpfn3():
    global setpfn
    setpfn = 3
    w = open('PCC.txt', 'w')
    w.write('True')
    w.close()
    st()
def setpfn4():
    global setpfn
    setpfn = 4
    w = open('PCC.txt', 'w')
    w.write('True')
    w.close()
    st()
def setpfn5():
    global setpfn
    setpfn = 5
    w = open('PCC.txt', 'w')
    w.write('True')
    w.close()
    st()
root = tk.Tk()
root.title('choose a profile')
root.iconbitmap("logo.ico")
root.geometry('570x250')
root.resizable(False,False)
tk.Label(root,text='choose a profile to start this session').pack()
profilenamelist = ['second user','third user','forth user']
gombi = PhotoImage(file='logo.png')
gombi = gombi.subsample(2, 2)
def nuke():
    write0 = open('chi2.txt', 'w')
    write0.write("B")
    write0.close()
    #--------1--------
    write1 = open('bookmarks.txt', 'w')
    write1.write("")
    write1.close()
    os.startfile('clearcommand.bat')
    #--------2--------
    write2 = open('bookmarks2.txt', 'w')
    write2.write("")
    write2.close()
    os.startfile('clearcommand2.bat')
    #--------3--------
    write3 = open('bookmarks3.txt', 'w')
    write3.write("")
    write3.close()
    os.startfile('clearcommand3.bat')
    #--------4--------
    write4 = open('bookmarks4.txt', 'w')
    write4.write("")
    write4.close()
    os.startfile('clearcommand4.bat')
    #--------5--------
    write5 = open('bookmarksi.txt', 'w')
    write5.write("")
    write5.close()
    os.startfile('clearcommandi.bat')
    #-------------------------------
def nuke2():
    write0 = open('chi2.txt', 'w')
    write0.write("B")
    write0.close()
    #-------------1---------------
    write = open('bookmarks.txt', 'w')
    write.write("")
    write.close()
    subprocess.Popen('python clearc.py')
    #-------------2---------------
    write = open('bookmarks2.txt', 'w')
    write.write("")
    write.close()
    subprocess.Popen('python clearc2.py')
    # -------------3---------------
    write = open('bookmarks3.txt', 'w')
    write.write("")
    write.close()
    subprocess.Popen('python clearc3.py')
    # -------------4---------------
    write = open('bookmarks4.txt', 'w')
    write.write("")
    write.close()
    subprocess.Popen('python clearc4.py')
    # -------------5---------------
    write = open('bookmarksi.txt', 'w')
    write.write("")
    write.close()
    subprocess.Popen('python clearci.py')
def vac():
    write0 = open('chi2.txt', 'w')
    write0.write("B")
    write0.close()
    # --------1--------
    os.startfile('clearcommand.bat')
    # --------2--------
    os.startfile('clearcommand2.bat')
    # --------3--------
    os.startfile('clearcommand3.bat')
    # --------4--------
    os.startfile('clearcommand4.bat')
    # --------5--------
    os.startfile('clearcommandi.bat')
    # -------------------------------
def vac2():
    write0 = open('chi2.txt', 'w')
    write0.write("B")
    write0.close()
    #-------------1---------------
    subprocess.Popen('python clearc.py')
    #-------------2---------------
    subprocess.Popen('python clearc2.py')
    # -------------3---------------
    subprocess.Popen('python clearc3.py')
    # -------------4---------------
    subprocess.Popen('python clearc4.py')
    # -------------5---------------
    subprocess.Popen('python clearci.py')
tk.Button(root, text='incognito', command=setpfn5,bg='Black',fg='White').place(x=5,y=30)
tk.Button(root, text='Nuke', command=nuke,bg='yellow',fg='black').place(x=70,y=30)
tk.Button(root, text='Nuke PSCFs', command=nuke2,bg='yellow',fg='black').place(x=112,y=30)
tk.Button(root, text='vacuum', command=vac,bg='light gray',fg='blue').place(x=189,y=30)
tk.Button(root, text='vacuum PSCFs', command=vac2,bg='light gray',fg='blue').place(x=245,y=30)
text = "sometimes N\\Vs doesn't work correctly, to"
text2 = 'make sure it works correctly, do it 2\\3 times'
tk.Label(root, text=text).place(x=335,y=25)
tk.Label(root, text=text2).place(x=335,y=45)
tk.Button(root, image=gombi, command=setpfn1).pack(side="left", padx=5)
tk.Button(root, image=gombi,command=setpfn2).pack(side="left",padx=5)
tk.Button(root, image=gombi, command=setpfn3).pack(side="left", padx=5)
tk.Button(root, image=gombi, command=setpfn4).pack(side="left", padx=5)
l1 = tk.Label(root,text='main user')
l1.place(x=41,y=220)
l2 = tk.Label(root, text=profilenamelist[0])
l2.place(x=181,y=220)
l3 = tk.Label(root, text=profilenamelist[1])
l3.place(x=330,y=220)
l4 = tk.Label(root, text=profilenamelist[2])
l4.place(x=469,y=220)
root.mainloop()