class Produkts():
    def __init__(self, name, type, count, price):
        self.nosaukums = name
        self.skaits = count
        self.veids = type
        self.cena = price

    def jaunsNosaukums(self, jaunais_nosaukums):
        self.nosaukums = jaunais_nosaukums

    def pardotais_produkts(self):
        self.skaits = int(self.skaits)
        self.skaits -= 1

    def mainit_tipu(self, jaunais_veids = ""):
        if jaunais_veids == "":
            if self.veids == "D":
                self.veids = "P"
            else:
                self.veids = "P"
        else:
            self.veids = jaunais_veids
        self.info()

    def info(self):
        if self.veids == "P":
                veids = "Programmatūra"
        elif self.veids == "D":
            veids = "Detaļa"
        else:
            veids = self.veids
        return "Produkta nosaukums: {}\n Produkta veids: {}\n Produktu kopējais skaits: {}\n Produkta cena: {}€".format(self.nosaukums, veids, self.skaits, self.cena)



class Dators(Produkts):
    def __init__(self, name, count, razotajs):
        super().__init__(name, count, "Produkts")
        self.razotajs = razotajs
        self.info()

    def info(self):
        super().info()
#         print("Datora ražotājs:", self.razotajs, "Datora nosaukums:", self.nosaukums, "Datoru skaits:", self.skaits)

# pirmais = Dators("ThinkPad", "12", "Lenovo")