# scrappy_google_sheet
WebScrappy que raspa dados de vaga de emprego de programador python e lança em planilha google sheets.

# Primeiro passo:
Criar uma Google Sheet no seu Google Drive
Pode criar e inclusive adicionar já os cabeçalhos que usamos no scraper.
Exemplo:
TITLE - COMPANY - LOCATION - HOW OLD - LINK

# Segundo passo:
Criar sua conta no Google Cloud Platform
Caso ainda não possua uma conta no Google Cloud, crie a sua:
 - https://cloud.google.com/

Após criar sua conta acesse o console:
  - Após criar sua conta acesse o console:
  - https://console.cloud.google.com/

# Terceiro passo:
Novo projeto + instalar APIs + gerar credenciais e
importar
  **- # No Google Console você precisa:**
  - Criar um novo **projeto** no **Google Console**
    Instalar as **APIs** necessárias no projeto: **Google Drive API, Google Sheets
    APIGerar as credenciais com permissão de edição**
    Baixar as credenciais e importar o arquivo **json** no **Repl.it**
    
    
 # Quarto passo:
  - Conectar na Sheet + Configurar o gspread
   Agora que temos as credencias do nosso Bot (user) vamos adicionar na Sheet
   e fazer as configurações necessárias no gspread.
   
 - Adicionar o e-mail do Bot (credencial) na Sheet com permissão de edição
 - Importar gspread
 - Adicionar o gspread o ID do Sheet(que está na URL)
 - Selecione a Worksheet que irá trabalhar (aquela tap/menu da planilha), no caso é sheet1(quando é apenas 1 ta/menu na planilha)
 
