from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app
from config import BOT_USERNAME

start_txt = "❖ ʜᴇʏ , ᴛʜᴇʀᴇ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ  ♥︎\n\n● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ○● ɴᴏᴛ | ꜱʜᴇɴɴ •》 XD ♡゙, ʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏʟʟᴇᴄᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ○● ɴᴏᴛ | ꜱʜᴇɴɴ •》 ♡゙ MUSIC"




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/+zcNPiCtKlVM5MjU1"),
          InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/+W7fUZMIpwLVhNjc1")
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/ec5d7ec6899af85241cd9.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
  
