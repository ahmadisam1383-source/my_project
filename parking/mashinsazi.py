from datetime import *
class Car:
    def __init__(self,pelak,model,color):
        self.pelak=pelak
        self.model=model
        self.color=color
        self.zaman= datetime.now()

    def info(self):
        txt = f"خودرو {self.model}  با پلاک {self.pelak} در تاریخ و زمان {self.zaman_v} به رنگ {self.color} وارد پارکینگ شد"
        return txt

