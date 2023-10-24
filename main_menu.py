from PySide6.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel
from PySide6 import QtCore

# QVBoxLayout - Cria um layout vertical
# QWidget - Cria um tela
# QPushButton - Cria um botão


class MainMenu(QWidget):
    # Inicializa a classe
    def __init__(self, parent):
        super().__init__()
        self.parent = parent  # atributo para herança
        self.inicializadorUi()

    # Inicializa a interface
    def inicializadorUi(self):
        layout = QVBoxLayout()

        label = QLabel(
            "Bem-vindo, ao programa de criptografia do Exercito Brasileiro!\n"
            "Proteja suas mensagens e mantenha a segurança brasileira!"
        )
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        cripButton = QPushButton("Criptografar")
        cripButton.clicked.connect(self.parent.showCripScreen)
        cripButton.setFixedHeight(40)
        layout.addWidget(cripButton)

        descButton = QPushButton("Descriptografar")
        descButton.clicked.connect(self.parent.showDescScreen)
        descButton.setFixedHeight(40)
        layout.addWidget(descButton)

        sairButton = QPushButton("Sair")
        sairButton.clicked.connect(self.parent.close)
        sairButton.setFixedHeight(40)
        layout.addWidget(sairButton)

        self.setLayout(layout)
