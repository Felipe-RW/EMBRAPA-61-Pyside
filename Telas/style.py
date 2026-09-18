BACKGROUND = "Imagens/background.png"
VERDE =  "#058914"
BRANCO = "#FFFFFF"
PRETO = "#000000"
QSS = f"""
QFrame{{background-image:url({BACKGROUND});
}}

QLabel#sub_t{{
    font-weight: bold;
    font-size: 20px;
    background : transparent;
    font-family: Verdana;
    
 }}
QLabel#Botao_fechar{{
    background: none;
}}

QLabel#Logo{{max-width :476px;
    max-height: 206px;
}}

QPushButton#butao{{ 
    background-color: {VERDE};
    color:{BRANCO};
    font-size: 20px;
    font-family: Verdana;
    font-weight: bold;
    
}}

QWidget#Painel{{
    background-color: {BRANCO};
    border: 3px solid {PRETO};
    border-radius: 10px;
}}

QLineEdit#Input_pin{{
    min-width:612px ;
    min-height:40px ;
}}


"""
