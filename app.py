# IMPORTA A BIBLIOTECA STREAMLIT (usada pra criar o site)
import streamlit as st

# IMPORTA BIBLIOTECA PRA EXPRESSÕES REGULARES (ajuda a identificar linguagens)
import re

# TÍTULO DO SITE
st.title("🔍 Analisador de Código Universal")

# DESCRIÇÃO
st.write("Cole seu código abaixo e eu tento analisar 😎")

# ÁREA DE TEXTO ONDE O USUÁRIO VAI COLAR O CÓDIGO
codigo = st.text_area("Cole seu código aqui:")

# FUNÇÃO PRA TENTAR IDENTIFICAR A LINGUAGEM
def identificar_linguagem(codigo):
    # Verifica se parece Python
    if "def " in codigo or "print(" in codigo:
        return "Python 🐍"
    
    # Verifica se parece C++
    elif "#include" in codigo or "std::" in codigo:
        return "C++ 💻"
    
    # Verifica HTML
    elif "<html" in codigo or "<div" in codigo:
        return "HTML 🌐"
    
    # Verifica JavaScript
    elif "function" in codigo or "console.log" in codigo:
        return "JavaScript ⚡"
    
    # Se não reconhecer
    else:
        return "Desconhecida 🤔"

# FUNÇÃO PRA ANALISAR O CÓDIGO
def analisar_codigo(codigo):
    resultado = ""

    # Conta quantas linhas tem
    linhas = codigo.split("\n")
    resultado += f"📏 Linhas: {len(linhas)}\n"

    # Conta caracteres
    resultado += f"🔤 Caracteres: {len(codigo)}\n"

    # Verifica se tem comentários
    if "#" in codigo or "//" in codigo:
        resultado += "💬 Contém comentários\n"
    else:
        resultado += "⚠️ Sem comentários\n"

    # Verifica possíveis erros simples
    if "==" in codigo and "=" in codigo:
        resultado += "⚠️ Cuidado com '=' vs '=='\n"

    return resultado

# BOTÃO PRA ANALISAR
if st.button("Analisar código"):

    # SE NÃO TIVER NADA ESCRITO
    if codigo.strip() == "":
        st.warning("Digite algum código primeiro!")
    
    else:
        # IDENTIFICA A LINGUAGEM
        linguagem = identificar_linguagem(codigo)

        # MOSTRA A LINGUAGEM
        st.subheader(f"Linguagem detectada: {linguagem}")

        # ANALISA O CÓDIGO
        resultado = analisar_codigo(codigo)

        # MOSTRA RESULTADO
        st.text(resultado)