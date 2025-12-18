from fastapi import FastAPI, UploadFile, File, HTTPException
import fitz  # PyMuPDF
import io

app = FastAPI()

@app.get("/")
def home():
    return {"status": "online", "message": "API de extracción lista"}

@app.post("/extract")
async def extract_text(file: UploadFile = File(...)):
    try:
        # 1. Leer el contenido binario
        pdf_content = await file.read()
        
        # 2. Abrir el PDF
        doc = fitz.open(stream=pdf_content, filetype="pdf")
        
        # 3. Extraer metadatos ANTES de cerrar
        text_output = ""
        total_paginas = len(doc) # Guardamos el número de páginas aquí
        
        for page in doc:
            text_output += page.get_text()
            
        # 4. Ahora sí podemos cerrar el documento
        doc.close()
        
        # 5. Devolver la respuesta
        return {
            "archivo": file.filename,
            "texto": text_output,
            "total_paginas": total_paginas # Usamos la variable guardada
        }
        
    except Exception as e:
        return {"error": f"Error procesando el PDF: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
