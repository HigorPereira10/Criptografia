from PySide6.QtWidgets import QMainWindow
from main_menu import MainMenu
from criptografar_screen import CriptografarScreen
from descriptografar_screen import DescriptografarScreen
from apagar_screen import ApagarScreen


class CripApp(QMainWindow):
    # Inicializa a classe
    def __init__(self):
        super().__init__()
        self.inicializadorUi()

    # Inicializa a interface
    def inicializadorUi(self):
        self.setWindowTitle("Menu Principal")  # Add titulo
        self.setGeometry(500, 200, 400, 300)  # Add as coordenadas e o tamanho

        self.mainMenu = MainMenu(self)
        self.setCentralWidget(self.mainMenu)

    def showCripScreen(self):
        self.cripScreen = CriptografarScreen(self)
        self.setCentralWidget(self.cripScreen)
        self.setWindowTitle("Criptografar")

    def showDescScreen(self):
        self.descScreen = DescriptografarScreen(self)
        self.setCentralWidget(self.descScreen)
        self.setWindowTitle("Descriptografar")

    def showVoltarMenu(self):
        self.mainMenu = MainMenu(self)
        self.setCentralWidget(self.mainMenu)
        self.setWindowTitle("Menu Principal")

    def showApagarScreen(self):
        self.apagarScreen = ApagarScreen(self)
        self.setCentralWidget(self.apagarScreen)
        self.setWindowTitle("Apagar Arquivo")
