from fastapi import FastAPI, UploadFile, File, HTTPException
import fitz  # PyMuPDF
import io

app = FastAPI()

@app.get("/")
def home():
    return {"status": "online", "message": "PDF Text Extractor API"}

@app.post("/extract")
async def extract_text(file: UploadFile = File(Sube_un_pdf)):
    # Validar que sea un PDF
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="El archivo debe ser un PDF")

    try:
        # Leer el contenido del archivo subido
        pdf_content = await file.read()
        
        # Abrir el PDF desde la memoria
        doc = fitz.open(stream=pdf_content, filetype="pdf")
        
        full_text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            full_text += page.get_text()
            
        doc.close()
        
        return {
            "filename": file.filename,
            "text": full_text,
            "page_count": len(doc)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
