from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from typing import Callable, Dict, Any, Awaitable
import app.requests as rq
class TestMiddleWare(BaseMiddleware):
    async def __call__ (self, handler: Callable[[TelegramObject, Dict[str,Awaitable]],
                                                 Awaitable[Any]], 
                                                 event:TelegramObject,
                                                 data: Dict[str, Any]) -> Any:
        if isinstance(event, Message):
            await rq.set_user(event.from_user.id)
        print("Actions before handler")
        result = await handler(event, data)
        print("Actions after handler")
        return result
    
