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
            text = input("Ведіть шлях до файлу")
            self.save(text, self.demeg, self.name, self.hp, self.protection)
    def save(self, text, demeg, name, hp, protection):
        print('A')
        save_file = {
            'dameg': demeg,
            'name': name,
            'hp': hp,
            'protection': protection
            }
        print('B')
        #text = input("Ведіть назву файлу в який збереже персонажа фаїл буде створеноо автоматично тому для коректного збереження будьласка ведь фаїл якого не існує розширення буде додано автоматично")
        text += ".json"
        file = open(text, "w+")
        json.dump(save_file, file)
        file.close()
        fille = {}
        print(text)
        try:
            with open('file.json', 'r') as f:
                print("DC")
                fille = json.load(f)
                print('d')
                fille['name'].append(text)
                print('D')
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
                print('D')
        with open('file.json', '+w') as f:
            json.dump(fille, f)
    def pers(self, name):
        for li in Pers.listt:
            if name == li.name:
                return li
    def Print(self):
        a = ""
        for li in Pers.listt:
            if li.name != None:
                a += f"\nНазва {li.name} Урон {li.demeg} Здоров'я {li.hp} Захист {li.protection}"
        return a
