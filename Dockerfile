# Usa a imagem oficial do Python (versão leve)
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos da aplicação para dentro do container
COPY todo.py .
COPY testtodo.py .
COPY README.md .

# Instala o pytest (usado nos testes)
RUN pip install --no-cache-dir pytest

# Roda os testes para garantir que tudo está OK antes de subir
RUN pytest testtodo.py -v

# Comando padrão ao iniciar o container
CMD ["python", "todo.py"]
