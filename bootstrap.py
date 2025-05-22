from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .services.sqlalchemy_repository import SqlAlchemyTodoRepository
from .services.todo_service import TodoService
from .views.todo_view import TodoView

async def init_app(settings):
    # Создаем асинхронный движок базы данных
    engine = create_async_engine(f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    # Репозиторий, основанный на SQLAlchemy
    repository = SqlAlchemyTodoRepository(async_session())

    # Сервис уровня доменной логики
    service = TodoService(repository)

    # Представление (view/controller)
    view = TodoView(service)

    # Регистрация контроллера в FastAPI
    app = FastAPI()
    app.include_router(view.router)

    return app