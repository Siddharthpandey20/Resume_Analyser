from fastapi import FastAPI, File, UploadFile
import fitz  # PyMuPDF
import io

app = FastAPI()

@app.post("/extract_text/")
async def extract_text(file: UploadFile = File(...)):
    contents = await file.read()
    pdf_document = fitz.open(stream=io.BytesIO(contents), filetype="pdf")
    
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    return {"filename": file.filename, "text": text}




