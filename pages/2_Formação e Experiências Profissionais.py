import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Formação e Experiências",
    page_icon="🎓",
    layout="wide"
)

# Função principal
def main():
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
    
    st.markdown("""
    - [Certificado de Algoritmos: Aprenda a programar - FIAP](7dd74ac6f7670639f873https://on.fiap.com.br/local/nanocourses/gerar_certificado.php?chave=7dd74ac6f7670639f873dfb2df0dc1e3&action=viewdfb2df0dc1e3)
    - [Certificado de Design Thinking - FIAP](https://on.fiap.com.br/local/nanocourses/gerar_certificado.php?chave=7374accb2ea8026be9932e7c05a1f4b6&action=view)
    - [Certificado de Design Thinking Process- FIAP](https://on.fiap.com.br/local/nanocourses/gerar_certificado.php?chave=e1720332058c183f15b4d6cd11a48c86&action=view)
    - [Certificado de Formação Social e Sustentabilidade - FIAP](https://on.fiap.com.br/local/nanocourses/gerar_certificado.php?chave=35995b50a5b46efe8faf37f73d4d93ca&action=view)
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

    # Experiência 2
    with st.expander("🔹 Estagiário em Administração, Arquivista — Prefeitura Municipal de Barueri (mar/2022 - dez/2022)"):
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
    st.markdown("🔙 [Voltar para Home](./)") 
    st.markdown("Desenvolvido por Larissa Estella.")

if __name__ == "__main__":
    main()
