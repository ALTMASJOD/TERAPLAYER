from pyrogram import Client, filters
import requests
import re

# Telegram Bot credentials
api_id = 21075063  # apna api_id bhar
api_hash = "c53c07f566f354f166277745eb6fb423"
bot_token = "7381603599:AAG2zleJn5Ci3k64VmlGenCfCqn-0itNBT0"

app = Client("terabox_downloader_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def get_direct_link(terabox_url):
    # Yeh function terabox URL se direct downloadable link nikaalega
    api = "https://api.tbxdrive.xyz/info?link=" + terabox_url
    response = requests.get(api)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("status") == True:
            return data['data']['download_url']
    return None

@app.on_message(filters.private & filters.text)
async def terabox_handler(client, message):
    url = message.text.strip()
    
    if "terabox.com" not in url and "1024tera.com" not in url:
        await message.reply_text("❌ Bhai sirf Terabox ka link bhej!")
        return
    
    msg = await message.reply_text("⏳ Link process ho raha hai... ruk ja bhai!")
    
    direct_link = get_direct_link(url)
    
    if direct_link:
        await msg.edit("✅ Link mil gaya! Ab bhej raha hoon...")
        await client.send_video(chat_id=message.chat.id, video=direct_link, caption="Terabox se direct!")
    else:
        await msg.edit("❌ Bhai link nahi nikal paya. Shayad galat link hai ya API down hai.")

app.run()