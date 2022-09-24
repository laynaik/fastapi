from email.quoprimime import body_check
from operator import itemgetter
import string
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

class package(BaseModel):
    name: str
    number : int
    description : Optional[str] = None


app = FastAPI()
@app.get("/")
def root():
    return{'message':"my api is best"}

#path parameters
@app.get("/items/{item_id}")
async def read_item(item_id):
    return{"itemid":item_id}


#path perametrs with type
@app.get("/items1/{item_id1}")
async def read_item1(item_id1:int):
    return{"item_id" : item_id1}


#query paramter
@app.get("/items2/{item_id2}")
async def read_item1(item_id2:int , q:str |None = None,short:float | None = None):
    if q:
        return{"itemid":item_id2 , 'q':q}
    if (q and short):
         return{"item_id" : item_id2,"q":q,"short":short}
    return{"itemid":item}


#request body
@app.post("/package/")
async def make_package(package:package):
    return package
    


