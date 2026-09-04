BACKGROUND = "Imagens/background.png"
VERDE =  "#058914"
BRANCO = "#FFFFFF"
PRETO = "#000000"
OFF_WHITE = "#A0C7FA"
QSS = f"""
QFrame#a{{background-image:url({BACKGROUND});
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

QLabel#Logo{{
    max-width :476px;
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

QWidget#background_gaveta{{
    background-color:{OFF_WHITE};
    min-height:70%;
    border-radius: 20%;
}}

QFrame#fundo_branco{{
    background-color:{BRANCO};
    border-radius: 20%;
    max-width: 650px;
    max-height: 450px;

}}

QLabel#dropdown{{
    max-width :476px;
    max-height: 206px;
        
  
}}
QFrame#aiai{{
    max-width :900px;
    max-height: 80px;
    background-color:{OFF_WHITE};
}}

"""
