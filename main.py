from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.utils import img_to_array
import numpy as np
import io
import os

script_dir = os.path.dirname(__file__)

app = FastAPI()
templates_dir = os.path.join(script_dir,'templates')
templates = Jinja2Templates(directory= templates_dir)
model = ResNet50(weights='imagenet')

 

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, file: UploadFile = File(...)):
    # Przetwarzanie obrazu
    contents = await file.read()
    image = load_img(io.BytesIO(contents), target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    
    preds = model.predict(image)
    result = decode_predictions(preds, top=1)[0][0]
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "prediction": f"{result[1]} ({result[2]*100:.2f}%)"
    })

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
