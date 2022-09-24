from fastapi import FastAPI
#from fastapi import uvicorn
app = FastAPI()
@app.get("/")
def root():
    return{'message':"my api is best"}

# if __name__=="__main__":
#     uvicorn.run(app,port=8090)
