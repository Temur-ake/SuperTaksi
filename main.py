import asyncio
from telethon import TelegramClient, events
from telegram import Bot

# Telethon va Bot ma'lumotlari
api_id = '24337774'
api_hash = '15eaac65b5312d9b7f91a5f43c478c88'
phone_number = '+998973024959'

BOT_TOKEN = '7660895998:AAFXezwUF68t861ym2kPGUIO2xsPl8MGCrI'

SOURCE_GROUP_ID = 1644715431
DESTINATION_GROUP_ID = -1002477688128

client = TelegramClient('userbot', api_id, api_hash)
bot = Bot(token=BOT_TOKEN)

ALLOWED_BOTS = ["Andijon_toshkent_2bot", "andijon_toshkent_taxi_7bot"]


# Telefon raqamini aniqlash funksiyasi
def contains_phone_number(text):
    import re
    phone_pattern = r'\b(?:\+?998)?[\s-]?[\(]?\d{2,3}[\)]?[\s-]?\d{3}[\s-]?\d{2,3}[\s-]?\d{2,3}\b'
    return bool(re.search(phone_pattern, text))


@client.on(events.NewMessage(chats=SOURCE_GROUP_ID))
async def forward_message(event):
    sender = await event.get_sender()
    sender_username = sender.username or "N/A"
    message = event.message
    text = message.text or "---"

    # Faqat ruxsat berilgan botlardan kelgan xabarlar ishlanadi
    if sender_username in ALLOWED_BOTS:
        message = event.message
        text = message.text or "---"

        if message.reply_markup:  # Tugmalar mavjud bo'lsa
            print("Message has inline buttons. Checking for phone number...")
            if contains_phone_number(text):  # Telefon raqami mavjud bo'lsa
                try:
                    await bot.send_message(chat_id=DESTINATION_GROUP_ID, text=text)
                    print("Message with phone number forwarded to destination group.")
                except Exception as e:
                    print(f"Error while sending message: {e}")
                    await asyncio.sleep(5)
            else:
                print("No phone number found in the button message. Skipping...")
        else:  # Tugmalar mavjud bo'lmasa
            try:
                print("Message without buttons forwarded to destination group.")
            except Exception as e:
                print(f"Error while sending message: {e}")
                await asyncio.sleep(5)
    if contains_phone_number(text):
        try:
            await bot.send_message(chat_id=DESTINATION_GROUP_ID, text=text)
            print("Message with phone number forwarded to destination group.")
        except Exception as e:
            print(f"Error while sending message: {e}")
            await asyncio.sleep(5)


async def main():
    await client.start(phone_number)
    print("Userbot started.")
    await client.run_until_disconnected()


if __name__ == "__main__":
    # Aniq asyncio loopni o'rnatish
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())  # Asinxron ishni boshlash uchun asyncio.run() ishlatish
