# Usa uma imagem leve do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /financial

# Copia apenas o arquivo de dependências para otimizar o cache
COPY requirements.txt /financial/

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta (se o gRPC estiver rodando nela)
EXPOSE 50052

# Define o comando para rodar o app gRPC
CMD ["python", "server_grpc.py"]
