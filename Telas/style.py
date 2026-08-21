BACKGROUND = "Imagens/background.png"
VERDE =  "#058914"
BRANCO = "#FFFFFF"
QSS = f"""
QFrame{{background-image:url({BACKGROUND});
}}

QLabel#sub_t{{
    font-weight: bold;
    font-size: 20px;
    background : transparent;
    
 }}

QLabel#Logo{{max-width :280px;
    max-height: 180px;
}}

QPushButton{{ 
    background-color: "{VERDE}";
    color:{BRANCO};
    font-size: 50px
}}

QPushButton::hover{{
background-color: "{BRANCO}";
    color:{BRANCO};

}}
"""