from pydantic import BaseModel


class AppPayload(BaseModel):
    """The pydantic model for the payload"""

    item_name: str
    item_sell_in: int
    item_quality: int
