from pydantic import BaseModel


class InfoBase(BaseModel):
    app_name: str = None
    release: str = None
