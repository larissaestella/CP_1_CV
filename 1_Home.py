import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Home",
    page_icon="📄",
    layout="wide"
)

# Função principal
def main():
    # Cabeçalho
    st.title("📄 Currículo Interativo")
    st.markdown("---")

    # Seção de apresentação
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("perfil.jpg", width=200) 
    with col2:
        st.header("Larissa Estella Gonçalves dos Santos")
        st.write("""
        **Objetivo**
        
        Desenvolver uma carreira sólida na área de tecnologia, aprimorando minhas habilidades 
        em desenvolvimento de software e análise de dados para contribuir com soluções 
        inovadoras e eficientes. Desejo aplicar e expandir meus conhecimentos técnicos, 
        especialmente em programação e engenharia de software, para agregar valor ao 
        ambiente corporativo e apoiar a transformação digital da empresa.  
        """)
        st.markdown("📧 Email: larissaestella56@gmail.com  \n📞 Telefone: (11) 94898-3450")
    
    st.markdown("---")
    
    # Seção de Redes Sociais
    st.subheader("🌐 Conecte-se comigo")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("[LinkedIn](https://www.linkedin.com/in/larissa-estella/)")
    with col2:
        st.markdown("[GitHub](https://github.com/larissaestella)")
    
    st.markdown("---")
    
    # Seção de Navegação
    st.subheader(" Seções do Currículo")
    st.write("Use o menu lateral para navegar entre as seções:")
    st.markdown("""
    - 🎓 Formação e Experiência Profissional
    - 💻 Skills
    - 📊 Análise de Dados
    """)
    st.markdown("---")
    
    # Rodapé
    st.markdown("Desenvolvido por Larissa Estella.")

if __name__ == "__main__":
    main()
