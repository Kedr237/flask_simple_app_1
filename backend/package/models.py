from pydantic import UUID4, BaseModel


class PersonInfo(BaseModel):
    id: UUID4
    first_name: str
    last_name: str
