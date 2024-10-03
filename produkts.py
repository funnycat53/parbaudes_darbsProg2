class Produkts():
    def __init__(self, name, count, type):
        self.nosaukums = name
        self.skaits = count
        self.tips = type

    def paaugstinas_skaits(self):
        self.skaits =+ 1
        self.info()

    def jaunsNosaukums(self, jaunais_nosaukums):
        self.nosaukums = jaunais_nosaukums
        self.info()

    def mainit_tipu(self, jaunais_tips = ""):
        if jaunais_tips == "":
            if self.tips == "Det":
                self.tips = "Prog"
            else:
                self.tips = "Prod"
        else:
            self.tips = jaunais_tips
        self.info()

    def info(self):
        if self.tips == "Prog":
                veids = "Programmatūra"
        elif self.tips == "Det":
            veids = "Detaļa"
        else:
            veids = self.tips
        return "Produkta nosaukums: {}. \n Produktu kopējais skaits: {}. \n Produkta veids:{}".format(self.nosaukums, self.skaits, veids)



class Dators(Produkts):
    def __init__(self, name, count, razotajs):
        super().__init__(name, count, "Produkts")
        self.razotajs = razotajs
        self.info()

    def info(self):
        super().info()
#         print("Datora ražotājs:", self.razotajs, "Datora nosaukums:", self.nosaukums, "Datoru skaits:", self.skaits)

# pirmais = Dators("ThinkPad", "12", "Lenovo")