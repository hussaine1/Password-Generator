from tkinter import *
from tkinter import messagebox
import random

root = Tk()
frame=Frame(root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky='nsew', column=0, row=3, columnspan=1)
Grid.rowconfigure(frame, 0, weight=1)
Grid.rowconfigure(frame, 1, weight=1)
Grid.rowconfigure(frame, 2, weight=1)
Grid.rowconfigure(frame, 3, weight=1)
Grid.columnconfigure(frame, 0, weight=1)
Grid.columnconfigure(frame, 1, weight=1)
Grid.columnconfigure(frame, 2, weight=1)
Grid.columnconfigure(frame, 3, weight=1)
Grid.columnconfigure(frame, 4, weight=1)
Grid.columnconfigure(frame, 5, weight=1)

minsize=Label(frame,text='minsize')
minsize.grid(row=0, column=0,columnspan=1)
minsizeent=Entry(frame, bd=5)
minsizeent.grid(row=0, column=1,columnspan=1)

maxsize=Label(frame,text='maxsize')
maxsize.grid(row=0, column=2,columnspan=1)
maxsizeent=Entry(frame, bd=5)
maxsizeent.grid(row=0, column=3,columnspan=1)

capital=IntVar()
captialcheck=Checkbutton(frame,text='Capital',variable=capital)
captialcheck.grid(row=1, column=0,columnspan=1)

number=IntVar()
numbercheck=Checkbutton(frame,text='Number',variable=number)
numbercheck.grid(row=1, column=1,columnspan=1)

symbol=IntVar()
symbolcheck=Checkbutton(frame,text='Special Character',variable=symbol)
symbolcheck.grid(row=1, column=2,columnspan=1)

lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_list = ['0','1','2','3','4','5','6','7','8','9']
specialchar_list=['!','£','$','%','^','&','*','(',')','-','_','=','+','@','#']

#function to make password





def genpassword():
    if minsizeent.get() == '':
        min_nom = 0
    else:
        min_nom = int(minsizeent.get())
    if maxsizeent.get() == '':
        max_nom = 0
    else:
        max_nom = int(maxsizeent.get())
    pass_list = []
    a = random.randint(min_nom, max_nom)
    if min_nom == 0:
        return "Input minimum password size in the 'minsize' field."
    elif min_nom < 4:
        return "Minimum password size must be 4 to generate."
    elif min_nom > max_nom:
        return "Minimum cannot be larger than the maximum."
    if capital.get()==1 and number.get()==1 and symbol.get() ==1:
        pass_list.append(random.choice(upper_case))
        pass_list.append(random.choice(number_list))
        pass_list.append(random.choice(specialchar_list))
        pass_list.append(''.join(random.choices(lower_case,k=a-3)))
        random.shuffle(pass_list)
        pass_string = ''.join(pass_list)
        shuf_pass_string = ''.join(random.sample(pass_string,len(pass_string)))
        return shuf_pass_string
    elif capital.get() ==1 and number.get()==0 and symbol.get()==0:
        pass_list.append(random.choice(upper_case))
        pass_list.append(''.join(random.choices(lower_case,k=a - 1)))
        random.shuffle(pass_list)
        pass_string = ''.join(pass_list)
        shuf_pass_string = ''.join(random.sample(pass_string, len(pass_string)))
        return shuf_pass_string
    elif number.get() == 1 and capital.get()==0 and symbol.get()==0:
        pass_list.append(random.choice(number_list))
        pass_list.append(''.join(random.choices(lower_case,k=a - 1)))
        random.shuffle(pass_list)
        pass_string = ''.join(pass_list)
        shuf_pass_string = ''.join(random.sample(pass_string, len(pass_string)))
        return shuf_pass_string
    elif symbol.get() == 1 and capital.get()==0 and number.get()==0:
        pass_list.append(random.choice(specialchar_list))
        pass_list.append(''.join(random.choices(lower_case, k=a - 1)))
        random.shuffle(pass_list)
        pass_string = ''.join(pass_list)
        shuf_pass_string = ''.join(random.sample(pass_string, len(pass_string)))
        return shuf_pass_string
    elif capital.get() ==1 and number.get() == 1 and symbol.get()==0:
        pass_list.append(random.choice(upper_case))
        pass_list.append(random.choice(number_list))
        pass_list.append(''.join(random.choices(lower_case, k=a - 2)))
        random.shuffle(pass_list)
        pass_string = ''.join(pass_list)
        shuf_pass_string = ''.join(random.sample(pass_string, len(pass_string)))
        return shuf_pass_string
    elif capital.get() ==1 and symbol.get() == 1 and number.get()==0:
        pass_list.append(random.choice(upper_case))
        pass_list.append(random.choice(specialchar_list))
        pass_list.append(''.join(random.choices(lower_case, k=a - 2)))
        random.shuffle(pass_list)
        pass_string = ''.join(pass_list)
        shuf_pass_string = ''.join(random.sample(pass_string, len(pass_string)))
        return shuf_pass_string
    elif symbol.get() ==1 and number.get() == 1 and capital.get()==0:
        pass_list.append(random.choice(number_list))
        pass_list.append(random.choice(specialchar_list))
        pass_list.append(''.join(random.choices(lower_case, k=a - 2)))
        random.shuffle(pass_list)
        pass_string = ''.join(pass_list)
        shuf_pass_string = ''.join(random.sample(pass_string, len(pass_string)))
        return shuf_pass_string
    else:
        pass_list.append(''.join(random.choices(lower_case, k=a)))
        random.shuffle(pass_list)
        pass_string = ''.join(pass_list)
        shuf_pass_string = ''.join(random.sample(pass_string, len(pass_string)))
        return shuf_pass_string

#now just need to output the value of the define function onto screen after pressing a button.



def showMsg():
    messagebox.showinfo('Generated Password', genpassword())

generate_button=Button(frame, text= 'Generate',command =showMsg)
generate_button.grid(row=2, column=0,columnspan=1)
root.mainloop()

