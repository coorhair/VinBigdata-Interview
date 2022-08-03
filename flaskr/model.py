import typing
from datetime import datetime
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from .objectid import PydanticObjectId


class CallBase(BaseModel):
    created_at: typing.Optional[datetime]
    updated_at: typing.Optional[datetime]


class Call(CallBase):
    id: typing.Optional[PydanticObjectId] = Field(None, alias='_id')
    username: str = Field(..., max_length=32)
    call_duration: int = Field(...)  # milisecond

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get('_id') is None:
            data.pop('_id', None)
        return data
