#from fastapi import FastAPI

#app = FastAPI()

#@app.get("/")
#def read_root():
#    return {"Hello": "World"}

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: str = None):
#    return {"item_id": item_id, "q": q}

#------------------
#from fastapi import FastAPI
#from pydantic import BaseModel

#app = FastAPI()

#class Item(BaseModel):
#    name: str
#    price: float
#    is_offer: bool = None

#@app.post("/items/")
#def create_item(item: Item):
#    return item


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Exemple de modèle
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Votre route personnalisée
@app.get("/loqmanben")
def read_loqmanben():
    return {"name": "LoqmanBen"}
