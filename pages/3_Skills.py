import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Skills",
    page_icon="💻",
    layout="wide"
)

# Função principal
def main():
    st.title("💻 Skills Profissionais")
    st.markdown("---")

    st.write("""
    Aqui estão algumas das principais habilidades que desenvolvi ao longo da minha trajetória profissional, 
    acadêmica e pessoal.
    """)

    st.markdown("## 🔧 Hard Skills (Habilidades Técnicas)")
    
    # Dividindo as colunas de hard skills
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Linguagens de Programação**")
        st.progress(50)  
        st.write("Python")
        st.progress(70)  
        st.write("JavaScript")
        st.progress(50)  
        st.write("Java")
        st.progress(40)  
        st.write("C++")
        st.progress(20)  
    
    with col2:
        st.markdown("**Ferramentas e Tecnologias**")
        st.progress(85)  
        st.write("Git & GitHub")
        st.progress(75)  
        st.write("MySQL")
        st.progress(50)  
        st.write("React / Node.js")
        st.progress(50)  
        st.write("Metodologia ágil")
        st.progress(60) 

    st.markdown("---")
    
    # Soft Skills
    st.markdown("## 🤝 Soft Skills (Habilidades Interpessoais)")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("- ✅ Organização e Planejamento")
        st.markdown("- ✅ Trabalho em Equipe")
        st.markdown("- ✅ Relacionamento Interpessoal")

    with col4:
        st.markdown("- ✅ Adaptabilidade")
        st.markdown("- ✅ Comunicação")
        st.markdown("- ✅ Resolução de Problemas")

    st.markdown("---")

    # Idiomas
    st.markdown("## 🌐 Idiomas")
    st.markdown("""
    - **Inglês:** Avançado
    - **Português:** Nativo
    """)

    st.markdown("---")
    
    # Rodapé
    st.markdown("🔙 [Voltar para Home](./)")
    st.markdown("Desenvolvido por Larissa Estella.")

if __name__ == "__main__":
    main()
