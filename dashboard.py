import streamlit as st
import pandas as pd
import requests

# CONFIGURAÇÃO INICIAL DA INTERFACE DO DASHBOARD
st.set_page_config(page_title="Dashboard de leilões", layout="wide")

st.title("📊 Painel de controle de leilões")
st.markdown("Visualização em tempo real dos dados coletados via API.")

try:
    # REQUISIÇÃO PARA BUSCAR DADOS DO BACKEND
    response = requests.get("http://127.0.0.1:8001/leilões")
    if response.status_code == 200:
        dados_brutos = response.json()["data"]
        df = pd.DataFrame(dados_brutos)
        
        if not df.empty:
            # LIMPEZA E CONVERSÃO DOS VALORES MONETÁRIOS PARA CÁLCULOS MATEMÁTICOS
            df['valor_numerico'] = df['valor inicial'].str.replace('R$', '', regex=False).str.replace('RS', '', regex=False).str.replace('.', '', regex=False).str.replace(',', '.').astype(float)

            # EXIBIÇÃO DE MÉTRICAS RESUMIDAS
            col1, col2, col3 = st.columns(3)
            col1.metric("Total de leilões", len(df))
            col2.metric("Soma de valores iniciais", f"R$ {df['valor_numerico'].sum():,.2f}")
            col3.metric("Categorias únicas", df['categoria'].nunique())

            st.divider()

            # CONSTRUÇÃO DOS GRÁFICOS DE ANÁLISE
            col_graph1, col_graph2 = st.columns(2)
            
            with col_graph1:
                st.subheader("Leilões por categoria")
                st.bar_chart(df['categoria'].value_counts())

            with col_graph2:
                st.subheader("Distribuição de valores")
                st.line_chart(df.set_index('nome')['valor_numerico'])

            # APRESENTAÇÃO DA TABELA DE DADOS COMPLETA
            st.subheader("Dados detalhados")
            st.dataframe(df.drop(columns=['valor_numerico']), use_container_width=True)
            
        else:
            st.warning("Banco de dados vazio. Informações insuficientes para formar o dashboard")
    else:
        st.error(f"Erro de conexão: {response.status_code}")

except Exception as e:
    st.error(f"Erro: {e}")

# BOTÃO PARA ATUALIZAR AS INFORMAÇÕES NA TELA
if st.button('Atualizar dados'):
    st.rerun()

# streamlit run dashboard.py
