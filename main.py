from telethon import TelegramClient, events
import asyncio

api_id = '24337774'
api_hash = '15eaac65b5312d9b7f91a5f43c478c88'
phone_number = '+998973024959'

client = TelegramClient('userbot', api_id, api_hash)

SOURCE_GROUP_ID = 1644715431
DESTINATION_GROUP_ID = -1002306592274

# Oqibatid = -1644715431
# mersedes = 2092343101
async def main():
    await client.start(phone_number)

    @client.on(events.NewMessage(chats=SOURCE_GROUP_ID))
    async def handler(event):
        message = event.message
        user_id = message.sender_id
        user_name = message.sender.username if message.sender.username else message.sender.first_name
        text = message.text

        if text:
            print(f"Matnli xabar olindi: {text} (ID: {user_id}, Username: {user_name})")
            await client.send_message(DESTINATION_GROUP_ID, f"Yangi xabar: {text}")
            print(f"Xabar {DESTINATION_GROUP_ID} guruhiga yuborildi.")

        if message.media:
            print(f"Media fayl olindi: {message.media}")
            try:
                await message.forward_to(DESTINATION_GROUP_ID)
                print(f"Media fayl {DESTINATION_GROUP_ID} guruhiga yuborildi.")
            except Exception as e:
                print(f"Xatolik: {e}")

    print("Userbot ishga tushdi.")
    await client.run_until_disconnected()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
