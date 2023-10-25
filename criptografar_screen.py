from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QPushButton,
    QTextEdit,
    QLabel,
    QFileDialog,
)
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
import base64


class CriptografarScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.pastaPath = ""
        self.setMouseTracking(True)
        self.inicializadorUi()

    # Inicializador desta interface
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

        self.label2 = QLabel("")
        self.label2.setTextInteractionFlags(
            Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard
        )
        layout.addWidget(self.label2)

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

    # Metodo de condição, codificação e criptografia
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
            texto_codificado = base64.b64encode(texto.encode("utf-8"))
            self.chave = texto_codificado.decode("utf-8")

            self.erroLabel.setText("")

            texto_crip = CriptografarScreen.cifra_de_vigenere(texto, self.chave)

            self.label2.setText(f"Sua chave de criptografia é: {self.chave}")

            arquivo = open(f"{self.pastaPath}/codificado.txt", "w")
            arquivo.write(texto_crip)
            arquivo.close()

            palette = QPalette()
            palette.setColor(QPalette.WindowText, QColor("green"))
            self.erroLabel.setPalette(palette)
            self.erroLabel.setText("As informações foram criptografadas!")

    # Metodo de criptografia
    def cifra_de_vigenere(texto, chave):
        resultado = []

        for i in range(len(texto)):
            if texto[i].isalpha():
                texto_offset = ord("a") if texto[i].islower() else ord("A")
                chave_offset = ord("a") if chave[i % len(chave)].islower() else ord("A")

                deslocamento = (
                    ord(texto[i]) - texto_offset + ord(chave[i % len(chave)]) - chave_offset
                ) % 26
                resultado.append(chr(deslocamento + texto_offset))
            else:
                resultado.append(texto[i])

        return "".join(resultado)
