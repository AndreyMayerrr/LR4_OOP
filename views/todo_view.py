from fastapi import APIRouter, Request, Depends
from typing import List
from ..models import Todo, Item
from ..services.todo_service import ITodoService

router = APIRouter(prefix="/todos")

class TodoView:
    def __init__(self, service: ITodoService):
        self.service = service

    @router.get("/", response_model=List[Todo])
    async def get_all_todos(self, request: Request) -> List[Todo]:
        return await self.service.get_all_todos()

    @router.post("/", response_model=Todo)
    async def add_todo(self, todo: Todo, request: Request) -> Todo:
        return await self.service.add_todo(todo)

    @router.delete("/{todo_id}")
    async def remove_todo(self, todo_id: int, request: Request) -> None:
        await self.service.remove_todo(todo_id)

    @router.get("/{todo_id}/items", response_model=List[Item])
    async def get_items(self, todo_id: int, request: Request) -> List[Item]:
        return await self.service.get_items(todo_id)

    @router.post("/{todo_id}/items", response_model=Item)
    async def add_item(self, todo_id: int, item: Item, request: Request) -> Item:
        return await self.service.add_item(todo_id, item)

    @router.delete("/{todo_id}/items/{item_id}")
    async def remove_item(self, item_id: int, request: Request) -> None:
        await self.service.remove_item(item_id)