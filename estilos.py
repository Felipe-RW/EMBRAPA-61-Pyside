ESTILO = """

QWidget {
    font-family: Verdana;
}


/* POPUP */

QWidget#popup {
    background-color: #FFFFFF;
    border-radius: 20px;
}


/* ÁREA CINZA */

QWidget#areaCinza {
    background-color: #DFDFDF;
}


/* TÍTULO PRINCIPAL */

QLabel#titulo {
    color: #000000;

    font-family: Verdana;
    font-size: 32px;
    font-weight: bold;
}


/* TÍTULOS DAS SEÇÕES */

QLabel#tituloSecao {
    color: #000000;

    font-family: Verdana;
    font-size: 20px;
    font-weight: bold;
}


/* BOTÃO RELATÓRIO DE PESQUISAS */

QPushButton#botaoRelatorio {
    background-color: #356394;
    color: #FFFFFF;

    border: none;
    border-radius: 20px;

    font-family: Verdana;
    font-size: 14px;
    font-weight: bold;
}


/* BOTÕES AZUIS */

QPushButton#botaoAzul {
    background-color: #356394;
    color: #FFFFFF;

    border: none;
    border-radius: 20px;

    font-family: Verdana;
    font-size: 14px;
    font-weight: bold;
}


/* BOTÕES BRANCOS */

QPushButton#botaoBranco {
    background-color: #FFFFFF;
    color: #000000;

    border: none;
    border-radius: 20px;

    font-family: Verdana;
    font-size: 14px;
    font-weight: bold;
}


/* BOTÃO GERAR RELATÓRIO */

QPushButton#botaoGerar {
    background-color: #263878;
    color: #FFFFFF;

    border: none;
    border-radius: 20px;

    font-family: Verdana;
    font-size: 13px;
    font-weight: bold;
}


/* BOTÃO X */

QPushButton#botaoFechar {
    background-color: transparent;
    color: #000000;

    border: none;

    font-family: Verdana;
    font-size: 27px;
    font-weight: bold;
}


/* CHECKBOX */

QCheckBox {
    color: #303438;

    font-family: Verdana;
    font-size: 14px;

    spacing: 10px;
}


QCheckBox::indicator {
    width: 23px;
    height: 23px;

    background-color: #F5F5F2;

    border: 1px solid #72937A;
    border-radius: 8px;
}


QCheckBox::indicator:checked {
    background-color: #356394;
}


/* CAMPO DE PESQUISA */

QLineEdit {
    background-color: #FFFFFF;

    border: 1px solid #8D8D8D;
    border-radius: 12px;

    color: #555555;

    font-family: Verdana;
    font-size: 16px;

    padding-left: 12px;
}


QLineEdit::placeholder {
    color: #888888;
}
"""