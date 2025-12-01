import character
import json
import sys
from PyQt5.QtWidgets import *
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
    def game(self, Pers, Peers, Action, Actionn):
        actionn = []
        if self.game_state['run'] == True:
            print("12")
            actionn = self.game_state['actionn']
        else:
            print("11")
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
        number = self.game_state['number']
        action = []
        action.append(int(Action))
        action.append(int(Actionn))
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
        if self.game_state['hp'] <= 0:
            self.run = False
            self.game_state['run'] = False
            with open("game_state.json", "+w") as f:
                json.dump(self.game_state, f)
            return 1
        if self.game_state['Peers_hp'] <= 0:
            self.game_state['run'] = False
            self.run = False
            with open("game_state.json", "+w") as f:
                json.dump(self.game_state, f)
            return 2
        with open("game_state.json", "+w") as f:
            json.dump(self.game_state, f)
        return 0
class Start:
    listt = []
    start = []
    def json_file(self, file):
        file += '.json'
        try:
            with open(file, "r") as fille:
                data = json.load(fille)
                print(type(data))
                nam = data['name']
                dameg = data['dameg']
                hp = data['hp']
                protection = data['protection']
                filee ={
                    'name': []
                    }# список створюється зановокожен раз для того щоб не було декількох однакових персонажей
                with open('file.json', 'r') as f:
                    filee = json.load(f)# спочатку переносить всі дані в програму
                    filee['name'].append(file)
                with open('file.json', '+w') as f:
                    json.dump(filee, f)# потім видаляє старий вміст і додає новий
                text = "Фаїл успішно відновлено"
                self.createe()
                return text
        except FileNotFoundError:
            text = "Нажаль такого файлу не існує або був введений неправильний шлях"
            return text
    def choice(self, info):
        name = info
        Info = pers.pers(name)
    def createe(self):
        i = 0
        try:
            with open('file.json', 'r') as f:
                fille = json.load(f)
                self.start = fille['name']
        except FileNotFoundError:
            print('Нажаль фаїл зі збереженнями не знайдено його буде автоматично відновлено')
            File = {
                'name': []
                }
            with open('file.json', '+w') as f:
                json.dump(File, f)
        for l in self.start:
            file = l
            try:
                with open(file, "r") as f:
                    data = json.load(f)
                    name = data['name']
                    dameg = data['dameg']
                    hp = data['hp']
                    protection = data['protection']
                    if name == None:
                        pass
                    else:
                        self.listt.append(character.Pers())
                        a = self.listt[i]
                        a.creation(dameg, name, hp, protection)
                    i += 1
            except FileNotFoundError:
                print("Персонажа не знайдено")
    
    def savee(self):
        try:
            with open("game_state.json", "r") as file:
                gamee.game_state = json.load(file)
                if gamee.game_state['run'] == True:
                    return '1'
                else:
                    return '0'
        except FileNotFoundError:
            return '0'  
class Save:
    def save(self, vin, Pers, Peers):
        file = open("save.txt", "a+")
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
        savee = "Фаїл збережений"
        return savee

pers = character.Pers()
peers = character.Pers()
gamee = Game()
sTart = Start()
savee = Save()

pers.creation(5, "pers1", 15, 3)
peers.creation(7, "pers2", 17, 3)
#sTart.startt()

