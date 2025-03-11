import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Formação e Experiências",
    page_icon="🎓",
    layout="wide"
)

# Função principal
def main():
    # Cabeçalho
    st.title("Formação e Experiências Profissionais")
    st.markdown("---")

    # Seção Formação Acadêmica
    st.header("🎓 Formação Acadêmica")
    st.write("""
    **Bacharelado em Engenharia de Software**  
    *FIAP - Faculdade de Informática e Administração Paulista*  
    2023 - 2027  
    """)
    
    st.write("""
    **Curso Técnico em Administração**  
    *FIEB - Fundação e Instito de Ensino de Barueri*  
    2020 - 2022  
    """)

    st.markdown("---")

    # Seção de Certificados
    st.subheader("📜 Certificados")
    st.write("Confira os certificados que conquistei ao longo da minha jornada:")
    
    # Lista de Certificados
    st.markdown("""
    - [Certificado de Desenvolvimento de Software - FIAP](https://link-do-certificado.com)
    - [Certificado de Análise de Dados - Data Science Academy](https://link-do-certificado.com)
    - [Certificado de Engenharia de Software - Coursera](https://link-do-certificado.com)
    - [Certificado de Machine Learning - edX](https://link-do-certificado.com)
    """)
    
    st.markdown("---")

    # Seção Experiência Profissional
    st.header("💼 Experiência Profissional")

    # Experiência 1
    with st.expander("🔹 Back Office — Emdia Grupo Santander (2023 - atual)"):
        st.write("""
        - Suporte a usuários internos e externos garantindo a organização e eficiência dos processos internos
        - Treinamento de novos colaboradores no uso de ferramentas da empresa.
        - Diagnóstico e resolução de problemas técnicos.
        - Análise e processamento de dados, acompanhamento de solicitações, resolução de pendências e otimização 
        de fluxos de trabalho
        """)

    # Experiência 3
    with st.expander("🔹 Estagiário em Administração, Arquivista — Prefeitura Municipal de Barueri (2022 - 2022)"):
        st.write("""
        - Organização e digitalização de documentos oficiais
        - Realizar o controle e gestão de entrada e saída de documentos e arquivos físicos e digitais, registrando 
        informações em sistemas de gestão.
        - Gerenciar dados arquivados em sistemas digitais, utilizando ferramentas de software para otimizar a 
        classificação e recuperação de documentos.  
        - Elaboração de relatórios mensais detalhando as atividades realizadas, incluindo a quantidade de 
        documentos arquivados e processos gerenciados.  
        """)

    st.markdown("---")

    # Rodapé
    st.markdown("🔙 [Voltar para Home](./)")  # Link de volta a home 
    st.markdown("Desenvolvido por Larissa Estella.")

# Executa o app
if __name__ == "__main__":
    main()
