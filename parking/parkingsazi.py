from tkinter.messagebox import showinfo

from mashinsazi import *
class Parking :
    def __init__(self, z=10):
        self.zarfiyat =z
        self.place=[]
    def add_khodro(self,mashin):
        if len(self.place) < self.zarfiyat:
            self.place.append(mashin)
            return True
        return False
    def hazf_khodro(self,p):
        for peyda in self.place:
            if peyda.pelak == p:
                self.place.remove(peyda)
                return peyda
        return False

    def hazine (self,deelmashin):
        zaman_khoroj = datetime.now()
        zaman_park = zaman_khoroj - deelmashin.zaman
        zaman_park_h = zaman_park.total_seconds() / 3600
        return round(zaman_park_h * 1000, 2)
    def all_show(self):
        all_info=[f"{dozd.pelak} - {dozd.model} - {dozd.color}" for dozd in self.place]
        return "\n".join(all_info)

    def show_faza_khali(self):
        return self.zarfiyat - len(self.place)

