import contextlib
import asyncio
from aiogram.types import ChatJoinRequest
from aiogram import Bot, Dispatcher, F
import logging
bot_token = "(id bot)"
channel_id = -1002038618240
admin_id = 1001151147

async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    msg = F"<b>Рады приветствовать тебя в нашем телеграмм канале🤍.</b>\r\n\r\n"\
           F"Спасибо за подписку, твоя заявка принята!"

    await bot.send_message(chat_id=chat_join.from_user.id, text=msg)
    await chat_join.approve()

async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - [%levelname_s] - %(name)s -"
                               "(%(filename)s).%(funcName)s(%lineno)d) - %(message)s"
                        )

    bot: Bot = Bot(token= bot_token)
    dp = Dispatcher()
    dp.chat_join_request.register(approve_request, F.chat.id==channel_id)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
       logging.error(f"[Exception] - {ex}" , exc_info=True)
    finally:
        await bot.session.close()


if __name__ == "__main1__":
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())
