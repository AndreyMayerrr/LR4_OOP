from typing import Protocol, runtime_checkable
from .repository import ITodoRepository
from ..models import Todo, Item

@runtime_checkable
class ITodoService(Protocol):
    async def get_all_todos(self) -> list[Todo]: ...

    async def add_todo(self, todo: Todo) -> Todo: ...

    async def remove_todo(self, todo_id: int) -> None: ...

    async def get_items(self, todo_id: int) -> list[Item]: ...

    async def add_item(self, todo_id: int, item: Item) -> Item: ...

    async def remove_item(self, item_id: int) -> None: ...

class TodoService(ITodoService):
    def __init__(self, repository: ITodoRepository):
        self.repository = repository

    async def get_all_todos(self) -> list[Todo]:
        return await self.repository.get_all_todos()

    async def add_todo(self, todo: Todo) -> Todo:
        return await self.repository.add_todo(todo)

    async def remove_todo(self, todo_id: int) -> None:
        await self.repository.remove_todo(todo_id)

    async def get_items(self, todo_id: int) -> list[Item]:
        return await self.repository.get_items(todo_id)

    async def add_item(self, todo_id: int, item: Item) -> Item:
        return await self.repository.add_item(todo_id, item)

    async def remove_item(self, item_id: int) -> None:
        await self.repository.remove_item(item_id)