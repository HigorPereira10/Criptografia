from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QPushButton,
    QTextEdit,
    QLabel,
    QFileDialog,
)
from PySide6.QtGui import QPalette, QColor
import os


class ApagarScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.arquivoPath = ""
        self.inicializadorUi()

    def inicializadorUi(self):
        layout = QVBoxLayout()

        style = """
            font-size: 14px; 
            font-weight: bold; 
            """

        label = QLabel("Escolha o arquivo para ser apagado:")
        layout.addWidget(label)

        self.arquivoSelectLabel = QLabel("")
        layout.addWidget(self.arquivoSelectLabel)

        self.errolabel = QLabel("")
        self.errolabel.setStyleSheet(style)
        layout.addWidget(self.errolabel)

        openDirButton = QPushButton("Escolher Arquivo")
        openDirButton.setFixedHeight(40)
        openDirButton.clicked.connect(self.openDiretorio)
        layout.addWidget(openDirButton)

        descButton = QPushButton("Apagar")
        descButton.setFixedHeight(40)
        descButton.clicked.connect(self.apagarArquivo)
        layout.addWidget(descButton)

        voltarButton = QPushButton("Voltar ao Menu")
        voltarButton.clicked.connect(self.parent.showVoltarMenu)
        voltarButton.setFixedHeight(30)
        layout.addWidget(voltarButton)

        self.setLayout(layout)

    def openDiretorio(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        self.arquivoPath = QFileDialog.getOpenFileName(
            self, "Selecionar Arquivo", "", "Arquivos de Texto (*.txt)", options=options
        )

        if self.arquivoPath[0]:
            self.arquivoSelectLabel.setText(
                "Arquivo selecionado: " + self.arquivoPath[0]
            )
        else:
            self.arquivoSelectLabel.setText("Nenhum arquivo selecionado")

    def apagarArquivo(self):
        if not self.arquivoPath or not self.arquivoPath[0].strip():
            palette = QPalette()
            palette.setColor(QPalette.WindowText, QColor("red"))
            self.errolabel.setPalette(palette)
            self.errolabel.setText("Escolha um arquivo para ser apagado!")
        else:
            try:
                os.remove(self.arquivoPath[0])

                palette = QPalette()
                palette.setColor(QPalette.WindowText, QColor("green"))
                self.errolabel.setPalette(palette)
                self.errolabel.setText("O arquivo foi apagado!")
            except:
                palette = QPalette()
                palette.setColor(QPalette.WindowText, QColor("red"))
                self.errolabel.setPalette(palette)
                self.errolabel.setText("Este arquivo já foi apagado!")
