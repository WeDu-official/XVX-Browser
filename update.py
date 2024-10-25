from tkinter import messagebox
getd = open('./XVXBROWSERUPD.pak','rb')
s = str(getd.read(),encoding='utf-8')
data = r'{}'.format(s)
getd.close()
def find_between3(text, firstword, secondword):
    start_index = text.find(firstword) + len(firstword)
    end_index = text.find(secondword)
    if start_index == -1 or end_index == -1:
        return None
    return text[start_index:end_index]
vi = f'#:^#<'
vi2 = f'>#:^#'
ver = find_between3(data,vi,vi2)
for i in range(10000):
    filei = f'$:{i}^$<'
    filei2 = f'>$:{i}^$'
    datai = f'%:{i}^%<'
    datai2 = f'>%:{i}^%'
    fileni = f'$@:{i}^$@<'
    fileni2 = f'>$@:{i}^$@'
    datani = f'%@:{i}^%@<'
    datani2 = f'>%@:{i}^%@'
    filename = find_between3(data,filei,filei2)
    filename_new = find_between3(data,fileni,fileni2)
    if filename is not None and filename != '' and filename != "":
        try:
            fil = open(filename,'wb')
            fil.write(bytes(find_between3(data,datai,datai2),encoding='utf-8'))
            fil.close()
        except (PermissionError,OSError):
            pass
    if filename_new is not None and filename_new != '' and filename_new != "":
        try:
            filx = open(filename_new,'x')
            filx.close()
            fial = open(filename_new,'w')
            fial.write(find_between3(data,datani,datani2))
            fial.close()
        except (PermissionError,OSError,FileExistsError):
            pass
messagebox.showinfo('UPDATE',f'NOW YOUR BROWSER GOT THE NEW {ver} UPDATE,YHY')