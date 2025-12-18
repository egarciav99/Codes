from fastapi import FastAPI, UploadFile, File, HTTPException
import fitz  # PyMuPDF
import io

app = FastAPI()

@app.get("/")
def home():
    return {"status": "online", "message": "API de extracción lista"}

@app.post("/extract")
async def extract_text(file: UploadFile = File(...)):
    """
    Este endpoint recibe el binario desde n8n. 
    El nombre 'file' es el que debes poner en la columna 'Name' de n8n.
    """
    try:
        # 1. Leer el contenido binario del archivo
        pdf_content = await file.read()
        
        # 2. Abrir el PDF desde la memoria (stream)
        doc = fitz.open(stream=pdf_content, filetype="pdf")
        
        text_output = ""
        
        # 3. Recorrer las páginas y extraer texto
        for page in doc:
            text_output += page.get_text()
            
        doc.close()
        
        # 4. Devolver el JSON a n8n
        return {
            "archivo": file.filename,
            "texto": text_output,
            "total_paginas": len(doc)
        }
        
    except Exception as e:
        return {"error": f"Error procesando el PDF: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
