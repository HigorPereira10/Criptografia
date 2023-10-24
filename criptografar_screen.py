from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QPushButton,
    QTextEdit,
    QLabel,
    QFileDialog,
)
from PySide6.QtGui import QPalette, QColor
import base64


class CriptografarScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.pastaPath = ""
        self.inicializadorUi()

    def inicializadorUi(self):
        layout = QVBoxLayout()

        style = """
            font-size: 14px; 
            font-weight: bold; 
            """

        label = QLabel("Digite o texto para ser criptografado:")
        layout.addWidget(label)

        self.erroLabel = QLabel("")
        self.erroLabel.setStyleSheet(style)
        layout.addWidget(self.erroLabel)

        self.textoEdit = QTextEdit()
        layout.addWidget(self.textoEdit)

        openDirButton = QPushButton("Selecionar Diretório")
        openDirButton.setFixedHeight(35)
        openDirButton.clicked.connect(self.openDiretorio)
        layout.addWidget(openDirButton)

        cripButton = QPushButton("Gerar arquivo criptografado")
        cripButton.setFixedHeight(40)
        cripButton.clicked.connect(self.criptografar)
        layout.addWidget(cripButton)

        voltarButton = QPushButton("Voltar ao Menu")
        voltarButton.clicked.connect(self.parent.showVoltarMenu)
        voltarButton.setFixedHeight(30)
        layout.addWidget(voltarButton)

        self.setLayout(layout)

    def openDiretorio(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly

        self.pastaPath = QFileDialog.getExistingDirectory(
            self, "Selecionar Diretório", "", options=options
        )

        print(self.pastaPath)

    def criptografar(self):
        texto = self.textoEdit.toPlainText()
        if not texto.strip():
            palette = QPalette()
            palette.setColor(QPalette.WindowText, QColor("red"))
            self.erroLabel.setPalette(palette)
            self.erroLabel.setText("Digite algo para ser criptografado!!")
        elif not self.pastaPath.strip():
            palette = QPalette()
            palette.setColor(QPalette.WindowText, QColor("red"))
            self.erroLabel.setPalette(palette)
            self.erroLabel.setText("Escolha a pasta para salvar o arquivo!")
        else:
            texto_codificado = base64.b64encode(texto.encode("ASCII"))
            codificado_ascii = texto_codificado.decode("ASCII")

            self.erroLabel.setText("")

            arquivo = open(f"{self.pastaPath}/codificado.txt", "w")
            arquivo.write(codificado_ascii)
            arquivo.close()

            palette = QPalette()
            palette.setColor(QPalette.WindowText, QColor("green"))
            self.erroLabel.setPalette(palette)
            self.erroLabel.setText("As informações foram criptografadas!")
