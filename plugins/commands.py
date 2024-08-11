from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import db
from configs import *
from utilities import short_link, save_data


@Client.on_message(filters.command('start') & filters.private)
async def start_handler(c, m):
    try:
        await db.add_user(m.from_user.id)
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Hᴇʟᴩ Mᴇɴᴜ", callback_data="help"),
                 InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")],
                [InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                 InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}")],
                [InlineKeyboardButton("Cʟᴏsᴇ ❌", callback_data="delete")]
            ]
        )
            
        await m.reply_text(
            START_TXT.format(m.from_user.mention),
            reply_markup=keyboard
        )
    except:
        pass

@Client.on_message(filters.command('set_shortner') & filters.private)
async def save_shortlink(c, m):
    if len(m.command) < 3:
        await m.reply_text(
            "<b>Command Incomplete:\n\nPut shortner URL & API along with the command.\n\nEx: <code>/set_shortner example.com api</code></b>"
        )
        return    
    usr = m.from_user
    elg = await save_data((m.command[1].replace("/", "").replace("https:", "").replace("http:", "")), m.command[2], uid=usr.id)
    if elg:
        await m.reply_text(f"Shortner has been set successfully!\n\nShortner URL - `{await db.get_value("shortner", uid=usr.id)}`\nShortner API - `{await db.get_value("api", uid=usr.id)}`")
    else:       
        await m.reply_text(f"Error:\n\nYour shortlink API or URL is invalid. Please check again!")    
    
@Client.on_message(filters.text & filters.private)
async def shorten_link(_, m):
    txt = m.text
    if not ("http://" in txt or "https://" in txt):
        await m.reply_text("Send a link that starts with http:// or https:// to shorten.")
        return
    usr = m.from_user
    try:
        short = await short_link(link=txt, uid=usr.id)
        msg = f"__Hᴇʀᴇ ᴀʀᴇ ʏᴏᴜʀ Sʜᴏʀᴛ Lɪɴᴋs__:\n\n<code>{short}</code>"
        await m.reply_text(msg)
    except Exception as e:
        await m.reply_text(f"Error shortening link: {e}")
