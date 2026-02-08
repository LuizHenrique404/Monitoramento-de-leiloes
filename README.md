# 📊 Sistema de Monitoramento de Leilões

Este projeto é uma solução Full Stack para coleta, armazenamento e visualização de dados de leilões (baseado na estrutura do Mega Leilões). O sistema utiliza uma API robusta para gerenciar o banco de dados e um dashboard interativo para análise de métricas.

## 🏗️ Arquitetura do Sistema

O projeto é dividido em três camadas principais:
1.  **Backend (API):** Desenvolvido com **FastAPI** para gerenciar a comunicação com o banco de dados.
2.  **Banco de Dados:** **MongoDB** (NoSQL) para armazenamento flexível dos lotes.
3.  **Frontend (Dashboard):** **Streamlit** para visualização de dados e métricas em tempo real.



---

## 🚀 Tecnologias Utilizadas

* **Python 3.x**
* **FastAPI** & **Uvicorn** (Servidor API)
* **MongoDB** & **PyMongo** (Banco de dados NoSQL)
* **Streamlit** (Interface Visual) 
* **Pandas** (Tratamento de dados) 
* **Pydantic** (Validação de dados)

---

## 🔧 Configuração e Instalação

### 1. Requisitos Prévios
* Ter o **MongoDB** instalado e rodando localmente (porta `27017`).
* Python instalado em sua máquina.

### 2. Instalação
Clone o repositório e instale as dependências:
```bash
pip install -r requirements.txt
