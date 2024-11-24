from pydantic import BaseModel

data= {'name': 'Vishal', 'age':'27', 'wexp':'4'}


class Instructor(BaseModel):
    name: str
    age: int
    wexp: int

# user=dict(Instructor(**data))

user=Instructor(**data)

user=user.model_dump()

print(user)
print(type(user))
print(user['name'])