from utils.file_util import make_file_path, read_json
from fastapi import APIRouter

class ItemEndpoint:
    def __init__(self):
        self.router = APIRouter()
        self.tags = ["items"]
        self.register_routes() 
    
    def register_routes(self):
        @self.router.get("/items/")
        def get_items(self):
            item_data_path = make_file_path("item.json", "mocks")
            item_data = read_json(item_data_path)
            return item_data    
            
        @self.router.get("/items/{item_id}")
        def get_item(self, item_id: int):
            return {"item_id": item_id}
