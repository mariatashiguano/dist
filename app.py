# app.py
from flask import Flask, jsonify, send_from_directory
import os
import platform
import datetime

app = Flask(__name__)

# Configuración para servir el index.html desde la misma carpeta
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# --- TU NUEVO BACKEND ---
@app.route('/api/info')
def get_system_info():
    # Simulamos lógica de negocio o datos del servidor
    data = {
        "sistema": platform.system(),
        "nodo": platform.node(),
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mensaje": "¡Hola desde el Backend en Python!",
        "status": "Conectado exitosamente"
    }
    return jsonify(data)

if __name__ == '__main__':
    # Importante: host='0.0.0.0' y port=80 para que funcione con tu configuración actual de Terraform
    app.run(host='0.0.0.0', port=80)