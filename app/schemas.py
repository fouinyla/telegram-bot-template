from pydantic import BaseModel


class MessageSchema(BaseModel):
    text: str
