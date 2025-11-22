import character
import json
import sys
class Game:
    vin = None
    run = True
    regulations = "Правила гри гравець має 2 дії нахід їх можна використовувати для захисту чи нападу якщо захист більший за напад відновлює здоров'я на кількість захисту яка залишилася після нападу"
    game_state = {
        'run': None,
        'pers': None,
        'demeg': None,
        'start_hp': None,
        'protection': None,
        'hp': None,
        'Peers_start_hp': None,
        'Peers_hp': None,
        'actionn': [],
        'number': 0,
        }
    def game(self, Pers, Peers):
        actionn = []
        if self.game_state['run'] == True:
            actionn = self.game_state['actionn']
        else:
            self.game_state['run'] = True
            self.game_state['pers'] = Pers.name
            self.game_state['demeg'] = Pers.demeg
            self.game_state['start_hp'] = Pers.hp
            self.game_state['protection'] = Pers.protection
            self.game_state['hp'] = Pers.hp
            self.game_state['Peers_start_hp'] = Peers.hp
            self.game_state['Peers_hp'] = Peers.hp
            self.game_state['actionn'] = []
            self.game_state['number'] = 0
        #hp = Pers.hp
        #hp1 = Peers.hp
        regulationss = int(input("якщо бажаєте познайомитися з правилами гри ведіть 1 якщо ні 2"))
        if regulationss == 1:
            print(self.regulations)
        #actionn = []
        number = self.game_state['number']
        #with open("game_state.json", "w") as f:
        while self.run:
            #Pers.hp -= (Peers.demeg - Pers.protection)
            #Peers.hp -= (Pers.demeg - Peers.protection)
            action = []
            action.append(int(input("Ведіть першу дію 1 атака 2 захист")))
            action.append(int(input("Ведіть другу дію 1 атака 2 захист")))
            demeg = self.game_state["demeg"]
            demeg1 = Peers.demeg
            protection = 0
            number += 1
            self.game_state['number'] = number
            numberr = "дія номер" + str(number)
            actionn.append(numberr)
            self.game_state['actionn'] = actionn
            for L in action:
                actionn.append(L)
                if L == 1:
                    self.game_state['Peers_hp'] -= (demeg - Peers.protection)
                if L == 2:
                    protection += self.game_state['protection']
            self.game_state['hp'] -= (demeg1 - protection)
            print("Ваше здоров'я", self.game_state['hp'])
            print("Здоров'я суперника", self.game_state['Peers_hp'])
            #number += 1
            if self.game_state['hp'] <= 0:
                self.vin = False
                self.run = False
            if self.game_state['Peers_hp'] <= 0:
                self.vin = True
                self.run = False
            with open("game_state.json", "+w") as f:
                json.dump(self.game_state, f)
        printaction = input("Ведіть 1 щоб вивесити попередні дії чи будьщо інше щоб нічого не виводити")
        if printaction == "1":
            print(actionn)
        if self.vin == True:
            print("Ви перемогли")
        else:
            print("Ви програли")
        sav = int(input("Ведіть 1 щоб зберегти результат гри чи 2 щоб не зберігати"))
        if sav == 1:
            savee.save(self.vin, self.game_state, Peers)
        self.game_state['run'] = False
        with open("game_state.json", "+w") as f:
            json.dump(self.game_state, f)
class Start:
    def startt(self):
        try:
            with open("game_state.json", "r") as file:
                gamee.game_state = json.load(file)
                if gamee.game_state['run'] == True:
                    run = input("ведіть 1 щоб перезапустити гру з останнього моменту або будьщо інше щоб почати заново")
                    if run == "1":
                        gamee.game(pers, peers)
                        sys.exit()
                    else:
                        gamee.game_state['run'] = False
        except FileNotFoundError:
            pass
        #except JSONDecodeError:
            #pass
        start = int(input("Ведіть 1 щоб створити свого персонажа, 2 щоб вибрати одного з запропонованих, 3 щоб вибрати один з інснуючих варіантів, 4 щоб завантажити з json файлу"))
        if start == 2:
            pers.Print()
            name = input("Ведіть назву персонаж")
            perss = pers.pers(name)
            gamee.game(perss, peers)
        if start == 1:
            pErs = character.Pers()
            pErs.creation2()
            gamee.game(pErs, peers)
        if start == 3:
            name = input("Ведіть шлях до файлу і назву файлу")
            dem = ""
            Name = ""
            hp = ""
            protection = ""
            try:
                with open(name, "r", encoding="utf-8") as file:
                    text = list(file.read())
                    i = 1
                    for a in text:
                        if i == 1:
                            if a == ";":
                                i += 1
                            else:
                                Name += a
                        elif i == 2:
                            if a == ";":
                                i += 1
                            else:
                                dem += a
                        elif i == 3:
                            if a == ";":
                                i += 1
                                hp = int(hp)
                            else:
                                hp = str(hp)
                                hp += a
                        elif i == 4:
                            if a == ";":
                                i += 1
                                protection = int(protection)
                            else:
                                protection = str(protection)
                                protection += a
                    pErs = character.Pers()
                    pErs.creation(dem, Name, hp, protection)
                    gamee.game(pErs, peers)
            except FileNotFoundError:
                print("був ведений неправильний шлях або такого файлу неіснуює")
        if start == 4:
            self.json_file()
            #gamee.game(pErs, peers)
    def json_file(self):
        file = input("Ведіть шлях до файлу")
        try:
            with open(file, "r") as fille:
                data = json.load(fille)
                print(type(data))
                nam = data['name']
                dameg = data['dameg']
                hp = data['hp']
                protection = data['protection']
                pErs = character.Pers()
                pErs.creation(dameg, nam, hp, protection)
                gamee.game(pErs,peers)
        except FileNotFoundError:
            print("Нажаль такого файлу не існує або був введений неправильний шлях")
class Save:
    def save(self, vin, Pers, Peers):
        sav = input("Ведіть назву файлу в який буде збережено результат")
        sav += ".txt"
        file = open(sav, "a+")
        if vin == True:
            file.write("Результат гри: перемога")
        else:
            file.write("Результат гри: поразка")
        file.write("\nВи грали за: ")
        file.write(Pers['pers'])
        file.write("\nУрон: ")
        file.write(str(Pers['demeg']))
        file.write("\nЗдоров'я: ")
        file.write(str(Pers['start_hp']))
        file.write("\nЗахист: ")
        file.write(str(Pers['protection']))
        file.write("\nЗалишилося здоров'я: ")
        file.write(str(Pers['hp']))
        file.write("\nПроти вас грав: ")
        file.write(Peers.name)
        file.write("\nУрон: ")
        file.write(str(Peers.demeg))
        file.write("\nЗдоров'я: ")
        file.write(str(Peers.hp))
        file.write("\nЗахист: ")
        file.write(str(Peers.protection))
        file.write("\nЗалишилося здоров'я: ")
        file.write(str(Pers['Peers_hp']))
        file.write("\n\n")
        file.close()
pers = character.Pers()
peers = character.Pers()
gamee = Game()
sTart = Start()
savee = Save()

pers.creation(5, "pers1", 15, 3)
peers.creation(7, "pers2", 17, 3)
sTart.startt()

