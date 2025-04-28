import requests
from pyrogram import Client, filters

# Bot Setup
app = Client("my_bot", api_id=21075063, api_hash="c53c07f566f354f166277745eb6fb423", bot_token="7381603599:AAG2zleJn5Ci3k64VmlGenCfCqn-0itNBT0")

# Handle the TeraFileShare link
@app.on_message(filters.regex(r"https://terafileshare.com/s/"))
async def download_video(client, message):
    link = message.text.strip()  # Clean the message and get the link
    unique_id = link.split('/')[-1]  # Extract the unique file ID from the link
    
    # Now use the unique_id to generate the download URL
    download_url = f"https://terafileshare.com/d/{unique_id}"

    try:
        # Send GET request to download the video
        response = requests.get(download_url)
        
        if response.status_code == 200:
            video_data = response.content  # Get the video data
            
            # Send video back to the user
            await message.reply_video(video_data)
        else:
            await message.reply_text("Sorry, video download failed.")
    except Exception as e:
        await message.reply_text(f"Error: {e}")

# Start the bot
app.run()
