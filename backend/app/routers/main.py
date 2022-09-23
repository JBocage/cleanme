from app.config import Settings, get_settings
from app.schemas import AppPayload
from fastapi import Depends, FastAPI

from gilded_rose.db_interface import GildedRoseDB
from gilded_rose.main import GildedRose, Item

application = FastAPI()
gilded_rose = GildedRoseDB()


@application.get("/")
def hello():
    """Hello worlds function"""
    return {"goodbye": "world"}


@application.get("/inventory")
def get_inventory():
    """get inventory function"""
    return {
        item.name: {"sell_in": item.sell_in, "quality": item.quality}
        for item in gilded_rose.items
    }


@application.post("/items")
def add_item(body: AppPayload):
    """add item to the shop"""
    gilded_rose.items.append(
        Item(body.item_name, sell_in=body.item_sell_in, quality=body.item_quality)
    )


@application.put("/items")
def update_items():
    """updates the items at the end of the day"""
    gilded_rose.update_quality()


@application.get("/env")
def get_env(settings: Settings = Depends(get_settings)):
    """get the settings"""
    return {"env": settings.environment}


@application.get("/items/{item_name}")
def get_item(item_name):
    """gets the item out of the gilded rose"""
    for index, item in enumerate(gilded_rose.items):
        if item.name == item_name:
            it = gilded_rose.items.pop(index)
            return {it.name: {"sell_in": it.sell_in, "quality": it.quality}}
    return {}
