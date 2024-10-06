class Produkts():
    def __init__(self, name, type, count):
        self.nosaukums = name
        self.skaits = count
        self.veids = type

    def paaugstinas_skaits(self):
        self.skaits += 1
        self.info()

    def samazinas_skaits(self):
        self.skaits -= 1
        self.info()

    def jaunsNosaukums(self, jaunais_nosaukums):
        self.nosaukums = jaunais_nosaukums
        self.info()

    def mainit_tipu(self, jaunais_veids = ""):
        if jaunais_veids == "":
            if self.veids == "Det":
                self.veids = "Prog"
            else:
                self.veids = "Prod"
        else:
            self.veids = jaunais_veids
        self.info()

    def info(self):
        if self.veids == "Prog":
                veids = "Programmatūra"
        elif self.veids == "Det":
            veids = "Detaļa"
        else:
            veids = self.veids
        return "Produkta nosaukums: {}.  \n Produkta veids:{} \n Produktu kopējais skaits: {}.".format(self.nosaukums, veids, self.skaits)



class Dators(Produkts):
    def __init__(self, name, count, razotajs):
        super().__init__(name, count, "Produkts")
        self.razotajs = razotajs
        self.info()

    def info(self):
        super().info()
#         print("Datora ražotājs:", self.razotajs, "Datora nosaukums:", self.nosaukums, "Datoru skaits:", self.skaits)

# pirmais = Dators("ThinkPad", "12", "Lenovo")