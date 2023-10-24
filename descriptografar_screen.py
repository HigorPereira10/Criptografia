from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QLabel,
    QFileDialog,
)
from PySide6.QtGui import QPalette, QColor
import base64


class DescriptografarScreen(QWidget):
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

        label = QLabel("Escolha o arquivo para ser descriptografado:")
        layout.addWidget(label)

        label2 = QLabel("Esta é a mensagem criptografada: ")
        layout.addWidget(label2)

        self.textoDescLabel = QLabel("")
        layout.addWidget(self.textoDescLabel)

        self.arquivoSelectLabel = QLabel("")
        layout.addWidget(self.arquivoSelectLabel)

        self.errolabel = QLabel("")
        self.errolabel.setStyleSheet(style)
        layout.addWidget(self.errolabel)

        openDirButton = QPushButton("Escolher Arquivo")
        openDirButton.setFixedHeight(40)
        openDirButton.clicked.connect(self.openDiretorio)
        layout.addWidget(openDirButton)

        descButton = QPushButton("Descriptografar")
        descButton.setFixedHeight(40)
        descButton.clicked.connect(self.descriptografar)
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

    def descriptografar(self):
        # self.path = self.arquivoPath[0]
        if not self.arquivoPath or not self.arquivoPath[0].strip():
            palette = QPalette()
            palette.setColor(QPalette.WindowText, QColor("red"))
            self.errolabel.setPalette(palette)
            self.errolabel.setText("Escolha um arquivo para ser descriptografado!")
        else:
            arquivo = open(self.arquivoPath[0], "r")
            texto_codificado = arquivo.readline()
            self.errolabel.setText("")
            try:
                decodificado = base64.b64decode(texto_codificado.encode("ASCII"))
                decodificado_ascii = decodificado.decode("ASCII")
                # arquivo.close()
                # arquivo = open(self.arquivoPath[0], "w")
                # arquivo.write(decodificado_ascii)

                self.textoDescLabel.setText(decodificado_ascii)

                palette = QPalette()
                palette.setColor(QPalette.WindowText, QColor("green"))
                self.errolabel.setPalette(palette)
                self.errolabel.setText("As informações foram descriptografadas!")
            except:
                palette = QPalette()
                palette.setColor(QPalette.WindowText, QColor("red"))
                self.errolabel.setPalette(palette)
                self.errolabel.setText(
                    "As informações deste arquivo, já estão descriptografadas!"
                )
