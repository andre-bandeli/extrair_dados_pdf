import PyPDF2

def extract_text_from_pdf(pdf_path):
    # Abrir o arquivo PDF
    with open(pdf_path, 'rb') as file:

        # Criar um objeto PDF reader
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Inicializar uma string para armazenar o texto extraído
        text = ''
        
        # Iterar sobre cada página do PDF
        for page_num in range(len(pdf_reader.pages)):

            # Extrair o texto da página atual
            page_text = pdf_reader.pages[page_num].extract_text()

            # Adicionar o texto extraído à string
            text += page_text
        
        # Retornar o texto extraído
        print(text)
        return text
        
# Caminho para o arquivo PDF
pdf_path = 'caminho'

# Chamar a função para extrair o texto do PDF
extracted_text = extract_text_from_pdf(pdf_path)
