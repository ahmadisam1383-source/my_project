from tkinter import  messagebox
from tkinter import *
txt_code={
    "a":"1","b":"2","c":"3","d":"4","e":"5",
    "f":"6","g":"7","h":"8","i":"9",
    "j":"10","k":"11","l":"12","m":"13",
    "n":"14","o":"15","p":"16","q":"17",
    "r":"18","s":"19","t":"20","u":"21",
    "v":"22","w":"23","x":"24","y":"25",
    "z":"26"," ":"27"
}
code_txt={v:k for k,v in txt_code.items()}
def coder(txt):
    txt=txt.lower()
    txt_list=[txt_code.get(dozd,dozd) for dozd in txt]
    return " ".join(txt_list)
def dcoder(code):
    code_list=[code_txt.get(dozd,dozd) for dozd in code.split()]
    return "".join(code_list)
def ramzkon_btn():
    txt=ent_txt_left.get()
    code=coder(txt)
    ent_code_left.delete(0,END)
    ent_code_left.insert(0,code)
def unramzkon_btn():
    code=ent_code_right.get()
    txt=dcoder(code)
    ent_txt_right.delete(0,END)
    ent_txt_right.insert(0,txt)
def on_enter(e):
    e.widget['background']='#e6e6e6'
    e.widget['relief']='raised'
def on_leave(e):
    e.widget['background']='systembuttonface'
    e.widget['relief']='flat'

jigar=Tk()
jigar.geometry("800x450")
jigar.title("god ali")
Label(jigar,text="coder",font=("arial",20,"bold")).grid(row=0,column=0,padx=10,pady=10)
Label(jigar,text="txt",font=("arial",20,"bold"),fg="purple").grid(row=1,column=0,padx=10,pady=10)
ent_txt_left=Entry(jigar,font=("arial",20,"bold"),width=7,justify="center")
ent_txt_left.grid(row=1,column=1,padx=10,pady=10)


Label(jigar,text="code",font=("arial",20,"bold"),fg="purple").grid(row=2,column=0,padx=10,pady=10)
ent_code_left=Entry(jigar,font=("arial",20,"bold"),width=7,justify="center")
ent_code_left.grid(row=2,column=1,padx=10,pady=10)
but_code_left=Button(jigar,text="code",font=("arial",20,"bold"),fg="purple",command=ramzkon_btn)
but_code_left.grid(row=3,column=1,padx=10,pady=10)
but_code_left.bind("<Enter>",on_enter)
but_code_left.bind("<Leave>",on_leave)

Label(jigar,text="Dcoder",font=("arial",20,"bold")).grid(row=0,column=2,padx=10,pady=10)
Label(jigar,text="code",font=("arial",20,"bold"),fg="purple").grid(row=1,column=2,padx=10,pady=10)
ent_code_right=Entry(jigar,font=("arial",20,"bold"),width=7,justify="center")
ent_code_right.grid(row=1,column=3,padx=10,pady=10)


Label(jigar,text="txt",font=("arial",20,"bold"),fg="purple").grid(row=2,column=2,padx=10,pady=10)
ent_txt_right=Entry(jigar,font=("arial",20,"bold"),width=7,justify="center")
ent_txt_right.grid(row=2,column=3,padx=10,pady=10)
but_txt_right=Button(jigar,text="txt",font=("arial",20,"bold"),fg="purple",command=unramzkon_btn)
but_txt_right.grid(row=3,column=3,padx=10,pady=10)
but_txt_right.bind("<Enter>",on_enter)
but_txt_right.bind("<Leave>",on_leave)


jigar.mainloop()
