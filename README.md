# autoscaler-ml
O AutoScaler ML foi desenvolvido como uma API headless (sem interface gráfica), focada na orquestração de recursos computacionais. 
Um pprojeto para a faculdade, acompanhado de um extenso trabalho de 60 páginas 

### Principais Funcionalidades
* **API Headless:** Focada puramente em backend e processamento de dados.
* **Orquestração:** Gerenciamento automático de recursos/modelos.
* **Monitoramento:** [Todo o monitoramento acontece pelo Google Cloud].
* junto com a aplicação principal, estou enviando um modelo simples para testes!!!

  ## 🛠 Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** Frask
* **ML Libraries:**  sklearn/ pandas
* **Containerização:** Docker

  ## ⚙️ Instalação e Configuração

Siga os passos abaixo para rodar o projeto localmente:

1. **Clone o repositório:**
   ```
   bash
   git clone [https://github.com/Rickreck/autoscaler-ml.git](https://github.com/Rickreck/autoscaler-ml.git)
   cd autoscaler-ml

2. **Crie um ambiente virtual**
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

3. **Instale as dependências de requirements.txt**
    ```
    pip install -r requirements.txt

4. Configure as variáveis de ambiente: Crie um arquivo .env na raiz e adicione:
    ```
    PORT=5000
    MODEL_PATH=./models

5. Execute a API
   ```
   python main.py
   # ou uvicorn main:app --reload
