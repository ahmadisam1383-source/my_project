from mashinsazi import *
from parkingsazi import *
from tkinter import *
from tkinter.messagebox import showinfo, showerror


class App:
    def __init__(self):
        self.root = Tk()
        self.parking = Parking()
        self.wdg()
        self.root.geometry("500x500")
        self.root.resizable(0, 0)
        self.root.title("car")
        #------------------------------------------------------------------------------------------------------
        def addcar():
            model1 = self.model.get()
            if any(char.isdigit() for char in model1):
                showerror("Error", "Lotfan dar Model adad vared nakonid!")
            if not model1 :
                showerror("Error", "Lotfan dar Model ye chiz bnvis!")
                return
            color1 = self.color.get()
            if any(char.isdigit() for char in color1):
                showerror("Error", "Lotfan dar Color adad vared nakonid!")
            if not color1 :
                showerror("Error", "Lotfan dar Color ye chiz bnvis!")
                return
            car = Car(self.get_pelak(), self.model.get(), self.color.get())
            self.parking.add_khodro(car)
            showinfo("car", "add shod")
        def hazf():
                p = self.get_pelak()
                car_hazf=self.parking.hazf_khodro(p)
                if car_hazf:
                    h=self.parking.hazine(car_hazf)
                    showinfo("hazine", f"mahin hazf shod hazine={h}toman")
                else:
                    showerror("Error", "pelak ro vard knid")
        def allinfo():
            try:
                info = self.parking.all_show()
                showinfo("car", f"{info}")
            except:
                showerror("Error", "yek chiz nevesshtid")
        def faz():
            try:
                khali = self.parking.show_faza_khali()
                showinfo("faze khali", f"{khali}")
            except:
                showerror("Error", "yek chiz nevesshtid")
        # ------------------------------------------------------------------------------------------------------
        frame1 = Frame(self.root)
        frame1.pack(pady=10)
        Button(frame1, text="add car", command=addcar).grid(row=0, column=1)
        Button(frame1, text="hazf", command=hazf).grid(row=0, column=2)
        Button(frame1, text="all info car", command=allinfo).grid(row=1, column=1)
        Button(frame1, text="fazay khali", command=faz).grid(row=1, column=2)
        self.root.mainloop()
    def get_pelak(self):
        return (
            self.pelak1.get()
            + self.pelak2.get()
            + self.pelak3.get()
            + self.pelak4.get()
        )
    def wdg(self):
        frame = Frame(self.root)
        frame.pack(pady=10)

        Label(frame, text="pelak").grid(row=0, column=0)
        Label(frame, text="model").grid(row=1, column=0)
        Label(frame, text="rang").grid(row=2, column=0)

        self.pelak1 = Entry(frame)
        self.pelak1.grid(row=0, column=1)

        self.pelak2 = Entry(frame)
        self.pelak2.grid(row=0, column=2)

        self.pelak3 = Entry(frame)
        self.pelak3.grid(row=0, column=3)

        self.pelak4 = Entry(frame)
        self.pelak4.insert(0, "ایران|")
        self.pelak4.grid(row=0, column=4)

        self.model = Entry(frame)
        self.model.grid(row=1, column=1)

        self.color = Entry(frame, )
        self.color.grid(row=2, column=1)
app = App()