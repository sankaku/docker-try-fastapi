from typing import List

from fastapi import FastAPI
from lib.person import Person

app = FastAPI()

people: List[Person] = [
    Person(name="Alice", age=50),
    Person(name="Bob", age=30),
]


@app.get("/")
async def hello_world(name: str = "World"):
    return {
        "success": True,
        "message": f"Hello {name}"}


@app.get("/people/")
async def fetch_all_people():
    return {
        "success": True,
        "message":
            {"people": people}
    }


@app.get("/people/{person_id}")
async def find_person(person_id: str):
    filtered: List[Person] = [p for p in people if str(p.id_) == person_id]
    if filtered == []:
        return {
            "success": False,
            "message": f"Can't find the person for id = {person_id}"}
    else:
        return {
            "success": True,
            "message": {"person": filtered[0]}
        }
