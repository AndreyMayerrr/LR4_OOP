from typing import AsyncIterator, List
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import Todo, Item
from .repository import ITodoRepository

class SqlAlchemyTodoRepository(ITodoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_todos(self) -> List[Todo]:
        stmt = select(Todo)
        result = await self.session.execute(stmt)
        return result.scalars().fetchall()

    async def add_todo(self, todo: Todo) -> Todo:
        self.session.add(todo)
        await self.session.flush()
        await self.session.refresh(todo)
        return todo

    async def remove_todo(self, todo_id: int) -> None:
        todo = await self.session.get(Todo, todo_id)
        if todo:
            await self.session.delete(todo)
            await self.session.flush()

    async def get_items(self, todo_id: int) -> List[Item]:
        stmt = select(Item).where(Item.todo_id == todo_id)
        result = await self.session.execute(stmt)
        return result.scalars().fetchall()

    async def add_item(self, todo_id: int, item: Item) -> Item:
        self.session.add(item)
        await self.session.flush()
        await self.session.refresh(item)
        return item

    async def remove_item(self, item_id: int) -> None:
        item = await self.session.get(Item, item_id)
        if item:
            await self.session.delete(item)
            await self.session.flush()