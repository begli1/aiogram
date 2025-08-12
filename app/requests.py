from app.models import async_session
from app.models import User, Category, Item
from sqlalchemy import select

async def set_user(tg_id_from_user):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id_from_user))

        if not user:
            session.add(User(tg_id=tg_id_from_user))
            await session.commit()


async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))
    

async def get_items_by_category(category_id):
    async with async_session() as session:
        return await session.scalars(select(Item).where(Item.category_id == category_id))
    

async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.category_id == item_id))