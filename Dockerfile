# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Directorio de trabajo
WORKDIR /app

# Copiamos los archivos necesarios
COPY requirements.txt .
COPY app.py .
COPY index.html .

# Instalamos Flask
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto 80 (igual que antes)
EXPOSE 80

# Comando para iniciar la app
CMD ["python", "app.py"]