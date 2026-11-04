from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str ="Anonymous"
    signup:datetime | None
user=User(id="123",signup=datetime.strptime("10/10/2010", "%d/%m/%Y"))

print(user)
