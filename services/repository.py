from abc import ABCMeta, abstractmethod
from typing import AsyncIterator, List
from ..models import Todo, Item

class ITodoRepository(metaclass=ABCMeta):
    @abstractmethod
    async def get_all_todos(self) -> List[Todo]: ...

    @abstractmethod
    async def add_todo(self, todo: Todo) -> Todo: ...

    @abstractmethod
    async def remove_todo(self, todo_id: int) -> None: ...

    @abstractmethod
    async def get_items(self, todo_id: int) -> List[Item]: ...

    @abstractmethod
    async def add_item(self, todo_id: int, item: Item) -> Item: ...

    @abstractmethod
    async def remove_item(self, item_id: int) -> None: ...