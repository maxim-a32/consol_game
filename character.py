import json
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
            #demeg = str(self.demeg)
            #hp = str(self.hp)
            #protection = str(self.protection)
            save_file = {
                'dameg': self.demeg,
                'name': self.name,
                'hp': self.hp,
                'protection': self.protection
                }
            text = input("Ведіть назву файлу в який збереже персонажа фаїл буде створеноо автоматично тому для коректного збереження будьласка ведь фаїл якого не існує розширення буде додано автоматично")
            text += ".json"
            file = open(text, "w+")
            json.dump(save_file, file)
            file.close()
            fille = {}
            try:
                with open('file.json', 'r') as f:
                    fille = json.load(f)
                    fille['name'].append(text)
            except FileNotFoundError:
                print("Фаїл для збереження не був знайдений генерація нового файлу щоб повернути файли скорестайтеся функцією повенення")
                File = {
                    'name': []
                    }
                with open('file.json', '+w') as f:
                    json.dump(File, f)
                with open('file.json', 'r') as f:
                    fille = json.load(f)
                    fille['name'].append(text)
            with open('file.json', '+w') as f:
                json.dump(fille, f)
            #file.write(self.name)
            #file.write(";")
            #file.write(demeg)
            #file.write(";")
            #file.write(hp)
            #file.write(";")
            #file.write(protection)
            #file.write(";")
            file.close()
    def pers(self, name):
        for li in Pers.listt:
            if name == li.name:
                return li
    def Print(self):
        for li in Pers.listt:
            print("Назва", li.name, "Урон", li.demeg, "Здоров'я", li.hp, "Захист", li.protection)
