from fastapi import FastAPI,UploadFile

app = FastAPI()

@app.get('/')
def home():
    return {
        'data':'Welcome to homepage'
    }

@app.get('/contact')
def contact():
    return {
        'data':'welcome to contact page'
    }

@app.post('/upload')
def handleImage(files:list[UploadFile]):
    print(files)
    return {
        'status':'Got the files'
    }

import uvicorn
uvicorn.run(app)