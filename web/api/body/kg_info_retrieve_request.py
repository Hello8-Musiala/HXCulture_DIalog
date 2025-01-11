
from pydantic import BaseModel


class KgInfoRetrieveRequest(BaseModel):
    text: str