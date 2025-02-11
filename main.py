from fastapi import FastAPI

app = FastAPI()

inventory = {
    1: {
        'name': 'Beans',
        'price': 3.99,
        'brand': 'Exwcutive'
    }
}

@app.get("/")
def get_root():
    return {'Data': 'Testing my knowledge'}

@app.get("/about")
def about():
    return {'data': 'this is about page'}

@app.get('/item/{item_id}')
def get_item(item_id: int):
    return inventory[item_id]