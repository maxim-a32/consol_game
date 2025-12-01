from PyQt5.QtWidgets import *
import sys
import json
import character
import game

class Consolee(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scren()
    def scren(self):
        self.screen_size = QApplication.primaryScreen().size()
        self.screen_width = self.screen_size.width()
        self.screen_height = self.screen_size.height()
        self.label = QLabel("Ведіть 2 щоб вибрати персонажа, 1 щоб створити персонажа, 4 щоб відновити персонажа", self)
        self.Label = QLabel("", self)
        
        self.line = QLineEdit()
        self.continuee = start.savee()
        if self.continuee == "1":
            self.Label.setText("Ведіть 3 щоб продовжити гру з останнього моменту")
                
        self.button = QPushButton("Кнопка", self)
        self.button.clicked.connect(self.btn_clik)
        self.resize(self.screen_width, self.screen_height)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.Label)
        vbox.addWidget(self.button)
        vbox.addWidget(self.line)
        
        container = QWidget()
        container.setLayout(vbox)
        
        self.setCentralWidget(container)
    def btn_clik(self):
        text = self.line.text()
        start.createe()
        self.Label.setText(text)
        if text == "2":
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.btn_cliK)
            start.createe()
            self.info = PERS.Print()
            self.label.setText(self.info)
            self.Label.setText("ведіть назву персонажа")
        if text == "1":
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.createe)
            self.label.setText("Ведіть назву персонажа")
        if text == "4":
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.restoration)
            self.label.setText("Ведіть шлях до файлу який бажаєте відновити")
        if text == "3":
            try:
                with open("game_state.json", "r") as f:
                    gamE.game_state = json.load(f)
                    if gamE.game_state['run'] == True:
                        self.pers = None
                        self.button.clicked.disconnect()
                        self.button.clicked.connect(self.action_one)
                        self.label.setText("ведіть першу дію 1 атак 2 захист")
                        self.Label.setText(gamE.regulations)
            except FileNotFoundError:
                pass
    def btn_cliK(self):
        start.createe()
        text = self.line.text()
        self.pers = PERS.pers(text)
        self.button.clicked.disconnect()
        self.button.clicked.connect(self.action_one)
        self.label.setText("ведіть першу дію 1 атака 2 захист")
        self.Label.setText(gamE.regulations)
    def btn_clik_game(self):
        result = gamE.game(self.pers, pErs, self.action, self.actionn)
        if result == 1:
            self.label.setText("Ви програли якщо бажаєте зберегти результат гри введіть 1")
            text = str(gamE.game_state['actionn'])
            self.Label.setText(text)
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.sav)
            self.vin = False
        if result == 2:
            self.label.setText("Ви перемогли якщо бажаєте зберегти результат гри ведіть 1")
            self.Label.setText(gamE.game_state['actionn'])
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.sav)
            self.vin = True
        if result == 0:
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.action_one)
            self.label.setText("ведіть першу дію")
            hp = gamE.game_state['hp']
            hpp = gamE.game_state['Peers_hp']
            self.Label.setText(f"Ваше здоров'я {hp} здоров'я суперника {hpp}")
    def action_one(self):
        self.action = self.line.text()
        self.label.setText("ведіть другу дію 1 атака 2 захист")
        self.button.clicked.disconnect()
        self.button.clicked.connect(self.action_two)
    def action_two(self):
        self.actionn = self.line.text()
        self.btn_clik_game()
    def sav(self):
        sav = self.line.text()
        if sav == "1":
            text = save.save(self.vin, gamE.game_state, pErs)
            self.Label.setText(text)
    def createe(self):
        self.name = self.line.text()
        self.button.clicked.disconnect()
        self.button.clicked.connect(self.create_demeg)
        self.label.setText("Ведіть урон")
    def create_demeg(self):
        self.demeg = int(self.line.text())
        self.button.clicked.disconnect()
        self.button.clicked.connect(self.create_hp)
        self.label.setText("Ведіть здоров'я")
    def create_hp(self):
        self.hp = int(self.line.text())
        self.button.clicked.disconnect()
        self.button.clicked.connect(self.create_protection)
        self.label.setText("Ведіть захист")
    def create_protection(self):
        self.protection = int(self.line.text())
        self.button.clicked.disconnect()
        self.button.clicked.connect(self.create_file)
        self.label.setText("Ведіть назву файлу")
    def create_file(self):
        self.file = self.line.text()
        PERS.creation(self.demeg, self.name, self.hp, self.protection)
        PERS.save(self.file, self.demeg, self.name, self.hp, self.protection)
        self.button.clicked.disconnect()
        self.button.clicked.connect(self.btn_clik)
        self.label.setText('Ведіть 2 щоб вибрати персонажа, 1 щоб створити персонажа, 4 щоб відновити персонажа')
    def restoration(self):
        file = self.line.text()
        text = start.json_file(file)
        self.Label.setText(text)
start = game.Start()
gamE = game.Game()
PERS = character.Pers()
pErs = game.peers
save = game.Save()

app = QApplication(sys.argv)
console = Consolee()

console.show()
sys.exit(app.exec_())

