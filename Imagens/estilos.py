# Arquivo: estilos.py

ESTILO_GERAL = """
/* Janela Principal do Popup */
QWidget {
    background-color: #FFFFFF;
    font-family: 'Segoe UI', Arial, sans-serif;
}

/* Botão de Fechar (X) */
QPushButton#BotaoFechar {
    background-color: transparent;
    color: #000000;
    font-size: 20px;
    font-weight: bold;
    border: none;
}
QPushButton#BotaoFechar:hover {
    color: #FF0000;
}

/* Título Principal */
QLabel#TituloRelatorio {
    font-size: 22px;
    font-weight: bold;
    color: #000000;
}

/* Abas / Botões Superiores de Seleção (ex: Relatório de Pesquisas) */
QPushButton#BotaoAbaAtivo {
    background-color: #3B6496;
    color: #FFFFFF;
    font-size: 13px;
    font-weight: bold;
    border-radius: 15px;
    padding: 6px 16px;
    text-align: center;
}

/* Caixa Cinza de Fundo das Opções */
QFrame#PainelFundo {
    background-color: #E2E2E2;
    border-radius: 8px;
}

/* Títulos das Colunas (Dados do Relatório, Anos, Pesquisadores) */
QLabel.TituloColuna {
    font-size: 15px;
    font-weight: bold;
    color: #000000;
}

/* Checkboxes */
QCheckBox {
    font-size: 13px;
    color: #000000;
    spacing: 8px;
}
QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border-radius: 4px;
    border: 1px solid #708A76;
    background-color: #FFFFFF;
}
QCheckBox::indicator:checked {
    background-color: #A3C1AD;
}

/* Botões de Alternância (Selecionar anos / Todos os anos) */
QPushButton#BotaoFiltroAtivo {
    background-color: #3B6496;
    color: #FFFFFF;
    font-size: 12px;
    font-weight: bold;
    border-radius: 12px;
    padding: 5px 12px;
}
QPushButton#BotaoFiltroInativo {
    background-color: #FFFFFF;
    color: #000000;
    font-size: 12px;
    font-weight: bold;
    border-radius: 12px;
    padding: 5px 12px;
    border: 1px solid #D0D0D0;
}

/* Campo de Pesquisa */
QLineEdit#CampoPesquisa {
    background-color: #FFFFFF;
    border: 1px solid #B0B0B0;
    border-radius: 6px;
    padding: 6px 10px;
    font-size: 12px;
    color: #555555;
}

/* Botão Inferior (Gerar Relatório) */
QPushButton#BotaoGerar {
    background-color: #122264;
    color: #FFFFFF;
    font-size: 14px;
    font-weight: bold;
    border-radius: 16px;
    padding: 10px 24px;
}
QPushButton#BotaoGerar:hover {
    background-color: #1A318C;
}
"""