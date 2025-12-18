# PDF Text Extractor API (n8n Ready)

Este es un microservicio construido con **FastAPI** diseñado para recibir archivos PDF a través de peticiones HTTP POST y devolver el texto extraído en formato JSON. Está optimizado para ser utilizado como un nodo en flujos de **n8n**.

## 🚀 Características
- Extracción de texto ultra rápida usando `PyMuPDF`.
- Endpoint específico para integración con el nodo "HTTP Request" de n8n.
- Despliegue automático en **Render**.

## 🛠️ Instalación y Despliegue en Render

1. Crea un nuevo **Web Service** en Render.
2. Conecta este repositorio de GitHub.
3. Configura los siguientes parámetros:
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port 10000`

## 🔗 Uso con n8n (HTTP Request Node)

Para integrar este servicio en tu flujo de n8n, configura el nodo **HTTP Request** de la siguiente manera:

* **Method:** `POST`
* **URL:** `https://tu-app-en-render.onrender.com/extract`
* **Body Content Type:** `Multipart-Form-Data`
* **Binary Data:** `true`
* **Fields to Send:**
    * **Name:** `file`
    * **Type:** `Binary Data`
    * **Property Name:** (El nombre de la propiedad binaria que viene del trigger, ej: `data`)

## 📄 Endpoints

### `GET /`
Verifica si la API está en línea.

### `POST /extract`
Recibe el PDF y devuelve el texto.
**Response:**
```json
{
  "filename": "documento.pdf",
  "text": "Contenido del pdf...",
  "page_count": 5
}
