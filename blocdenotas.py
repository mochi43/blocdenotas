from PyQt5.QtWidgets import* 
import os
import sys



class blocdenotas(QMainWindow):
    def __init__(self):
        super().__init__()

        self.titulo = "Bloc de Notas"
        self.x = 130
        self.y = 130
        self.ancho = 500
        self.alto = 500

        self.setGeometry(self.x,self.y, self.ancho, self.alto)

        self.setWindowTitle(self.titulo)

        self.caracteres = ""
        
        #Menu
        barrademenu = self.menuBar()


        #barradearchivo
        menu_archivo = barrademenu.addMenu("Archivo")

        abrir = QAction("Abrir", self)
        abrir.setShortcut("Ctrl+A")
        abrir.triggered.connect(self.abrir)
        menu_archivo.addAction(abrir)

        guardar = QAction("guardar", self)
        guardar.setShortcut("Ctrl+S")
        guardar.triggered.connect(self.guardar)
        menu_archivo.addAction(guardar)

        
        
    
        #barraeditar
        menu_editar = barrademenu.addMenu("&Editar")

        botoncopiar = QAction("Copiar", self)
        botoncopiar.setShortcut("Ctrl+C")
        menu_editar.addAction(botoncopiar)
        
        

        botonpegar = QAction ("Pegar", self)
        botonpegar.setShortcut("Ctrl+V")
        menu_editar.addAction(botonpegar)

        botoncortar = QAction ("Cortar", self)
        botoncortar.setShortcut("Ctrl+X")
        menu_editar.addAction(botoncortar)




        contenedorVertical = QVBoxLayout()

        self.texto = QPlainTextEdit()

        self.texto.textChanged.connect(self.contadordeletras)

        self.contador = QLabel(self.caracteres)

        

        
        contenedorVertical.addWidget(self.texto)
        contenedorVertical.addWidget(self.contador)


        widgetPrincipal = QWidget()

        widgetPrincipal.setLayout(contenedorVertical)

        self.setCentralWidget(widgetPrincipal)

    

    def contadordeletras(self):

        cantidad = len(self.texto.toPlainText())
        cantidad = str(cantidad)
        total =  "Cantidad de letras: "  + cantidad
        
        self.contador.setText(total)


    def abrir(self, e):
        archivo = QFileDialog.getOpenFileName(self,"Documento de Texto (*.txt)")
        if (os.path.exists(archivo [0]) == True):
            with open(archivo [0], 'r') as f:                   
                texto = f.read()
        self.texto.setPlainText(texto)
    
    def guardar (self, e):
        archivo = QFileDialog.getSaveFileName (self,"Documento de Texto (*.txt)")
        texto = self.texto.toPlainText()
        with open (archivo [0], 'w') as guardar:
            guardar.write(texto)
        


    


   



   
    
    
app = QApplication(sys.argv)
ventana = blocdenotas()
ventana.show()
app.exec()
