# Geometria140

Este projeto realiza cálculos geométricos utilizando Python, com foco em testes automatizados e organização modular.

## Estrutura do Projeto
- `unitest/`: Implementação das funções de cálculo geométrico.
- `utils/`: Funções utilitárias auxiliares.
- `fixtures/`: Arquivos de dados para testes (ex: `massa_piramide.csv`).
- `__tests__/`: Testes automatizados utilizando `unittest`.

## Ferramentas Utilizadas
- **Python 3.12**
- **pytest**: Para execução dos testes.

## Como rodar localmente

1. **Clone o repositório:**
   ```powershell
   git clone https://github.com/souza-vitor/Geometria140.git
   cd Geometria140
   ```

2. **(Opcional) Crie um ambiente virtual:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```

3. **Instale o pytest (opcional):**
   ```powershell
   pip install pytest
   ```

4. **Execute os testes:**
   - Usando unittest:
     ```powershell
     python -m unittest discover __tests__
     ```
   - Usando pytest:
     ```powershell
     pytest __tests__
     ```

## Observações
- Os arquivos de teste estão em `__tests__`.
- Os dados de exemplo estão em `fixtures/`.
- As funções principais estão em `unitest/` e `utils/`.