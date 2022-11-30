from pydantic import BaseModel


class CatName(BaseModel):
    name: str
    author: str


class CatOutputName(BaseModel):
    name: str
    author: str
    name_id: str


class CatOutputDto(BaseModel):
    cat_names: list[CatOutputName]
    count: int


class CreateOutputDto(BaseModel):
    created_id: str
    replica_id: str
    backend_version: str


class InfoOutputDto(BaseModel):
    backend_version: str
    replica_id: str