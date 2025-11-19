class Pers:
    demeg = None
    name = None
    hp = None
    protection = None
    listt = []
    def __init__(self):
        Pers.listt.append(self)
    def creation(self, demeg, name, hp, protection):
        self.demeg = int(demeg)#Для випадків коли вже відомі показники
        self.name = name
        self.hp = int(hp)
        self.protection = int(protection)
    def creation2(self):
        self.name = input("Ведіть назву")#Для створрення персонажа
        self.demeg = int(input("Ведіть урон"))
        self.hp = int(input("Ведіть здоров'я"))
        self.protection = int(input("Ведіть захист"))
        creation3 = int(input("Якщо хочете зберегти персонажа ведіть 1 якщо ні 2"))
        if creation3 == 1:
            demeg = str(self.demeg)
            hp = str(self.hp)
            protection = str(self.protection)
            text = input("Ведіть назву файлу в який збереже персонажа фаїл буде створеноо автоматично тому для коректного збереження будьласка ведь фаїл якого не існує розширення буде додано автоматично")
            text += ".txt"
            file = open(text, "a+")
            file.write(self.name)
            file.write(";")
            file.write(demeg)
            file.write(";")
            file.write(hp)
            file.write(";")
            file.write(protection)
            file.write(";")
            file.close()
    def pers(self, name):
        for li in Pers.listt:
            if name == li.name:
                return li
    def Print(self):
        for li in Pers.listt:
            print("Назва", li.name, "Урон", li.demeg, "Здоров'я", li.hp, "Захист", li.protection)
