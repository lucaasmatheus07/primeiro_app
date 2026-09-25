import streamlit as st
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(
    page_title="Calculadora Alvinegra - Corinthians",
    page_icon="🦅",
    layout="centered"
)

# Estilização personalizada em CSS (Cores do Corinthians: Preto, Branco e Destaques)
st.markdown("""
    <style>
    /* Fundo da página e fontes */
    .main {
        background-color: #0e0e0e;
    }
    
    /* Estilo do Título e Cabeçalho */
    h1 {
        color: #ffffff !important;
        text-shadow: 2px 2px 4px #000000;
        font-weight: 800;
    }
    
    p, label {
        color: #e0e0e0 !important;
    }

    /* Botão Principal Estilizado */
    div.stButton > button:first-child {
        background-color: #111111 !important;
        color: #ffffff !important;
        border: 2px solid #ffffff !important;
        font-weight: bold;
        font-size: 18px !important;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-color: #000000 !important;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# 1. Cabeçalho com Escudo e Título
col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    # Escudo oficial do Corinthians
    st.image(
        "https://upload.wikimedia.org/wikipedia/pt/b/b4/Corinthians_simbolo.png", 
        width=80
    )

with col_titulo:
    st.title("Calculadora do Timão 🦅")
    st.caption("Vai Corinthians! Faça suas contas com a força da Fiel.")

st.divider()

# 2. Entradas Numéricas em Duas Colunas
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Primeiro Número:", value=0.0, step=1.0)

with col2:
    num2 = st.number_input("Segundo Número:", value=0.0, step=1.0)

# 3. Escolha da Operação
operacao = st.selectbox(
    "Escolha a Operação:",
    options=["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"]
)

st.write("")

# 4. Botão de Calcular
if st.button("🏁 CALCULAR (VAI CORINTHIANS!)", use_container_width=True):
    
    resultado = None
    erro = False

    # Lógica Matemática
    if operacao == "Soma (+)":
        resultado = num1 + num2
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
    elif operacao == "Divisão (/)":
        if num2 == 0:
            st.error("⚠️ Fala, Fiel! Não existe divisão por zero no futebol nem na matemática!")
            erro = True
        else:
            resultado = num1 / num2

    # Exibição do Resultado e Animação de GOL
    if not erro and resultado is not None:
        
        # ----------------------------------------------------
        # ⚽ EFEITO ESPECIAL: BOLA NA REDE, SOM DE GOL E CONFETES
        # ----------------------------------------------------
        components.html(
            """
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
            
            <!-- Áudio de GOL / Torcida -->
            <audio autoplay>
              <source src="https://actions.google.com/sounds/v1/crowds/cheering_and_clapping.ogg" type="audio/ogg">
            </audio>

            <!-- Overlay de Gol na Tela -->
            <div id="gol-overlay" style="
                position: fixed;
                top: 0; left: 0;
                width: 100vw; height: 100vh;
                pointer-events: none;
                z-index: 9999;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                background: rgba(0,0,0,0.4);
                animation: fadeInOut 2.8s forwards;
            ">
                <div style="font-size: 80px; animation: bounce 0.6s infinite alternate;">⚽🥅</div>
                <h1 style="
                    color: #fff;
                    font-size: 48px;
                    font-family: sans-serif;
                    text-shadow: 0 0 20px #ffffff, 0 0 40px #d4af37;
                    margin-top: 10px;
                    letter-spacing: 2px;
                    text-align: center;
                ">GÓÓÓÓL DO TIMÃO!</h1>
            </div>

            <style>
                @keyframes bounce {
                    from { transform: translateY(0px) scale(1); }
                    to { transform: translateY(-25px) scale(1.15); }
                }
                @keyframes fadeInOut {
                    0% { opacity: 0; }
                    15% { opacity: 1; }
                    80% { opacity: 1; }
                    100% { opacity: 0; }
                }
            </style>

            <script>
                // Disparo de Confetes Pretos, Brancos e Dourados
                confetti({
                    particleCount: 120,
                    spread: 100,
                    origin: { y: 0.5 },
                    colors: ['#000000', '#ffffff', '#d4af37']
                });

                // Remove o efeito da tela após 2.8 segundos
                setTimeout(() => {
                    const overlay = document.getElementById('gol-overlay');
                    if(overlay) overlay.remove();
                }, 2800);
            </script>
            """,
            height=0
        )

        st.success("⚽ Golaço! Cálculo realizado com sucesso.")
        st.metric(label="Resultado Final:", value=f"{resultado:,.2f}")
        #feito
