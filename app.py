from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'hello!!'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)