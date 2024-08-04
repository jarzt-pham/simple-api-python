from fastapi import FastAPI
from endpoints.item import ItemEndpoint
from app import App

fast = FastAPI()
app = App(fast, ItemEndpoint())