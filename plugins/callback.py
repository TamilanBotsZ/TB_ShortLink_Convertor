from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from configs import *


@Client.on_callback_query()
async def callback(bot, query):
    me = await bot.get_me()
    data = query.data
    msg = query.message

    if data == "delete":
        await msg.delete()
        try:
            await msg.reply_to_message.delete()
        except:
            pass

    elif data == "help":
        await msg.edit(
            HELP_TXT.format(me.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Sᴇᴛ Sʜᴏʀᴛɴᴇʀ", callback_data="set_shortner"),
                     InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")],     
                    [InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ Gʀᴏᴜᴩ", url=f"https://t.me/{SUPPORT_GROUP}"),
                     InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")]
                ]
            )
        )
      
    elif data == "about":
        await msg.edit(
            ABOUT_TXT.format(me.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Hᴇʟᴩ Mᴇɴᴜ", callback_data="help"),
                     InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")],
                    [InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ Gʀᴏᴜᴩ", url=f"https://t.me/{SUPPORT_GROUP}")],
                    [InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")]
                ]
            )
        )

    elif data == "set_shortner":
        await msg.edit("Send shortner URL & API along with the command.\n\nEx: <code>/set_shortner example.com api</code></b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Hᴇʟᴩ Mᴇɴᴜ", callback_data="help"),
                     InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")],
                    [InlineKeyboardButton("Bᴀᴄᴋ", callback_data="help"),                     
                     InlineKeyboardButton("Cʟᴏsᴇ ❌", callback_data="delete")]
                ]
            )
        )
                      
         
      
    elif data == "earn_money":
        await msg.edit("๏Yᴏᴜ ᴄᴀɴᴇᴀʀɴ ᴜsɪɴɢ ᴀɴʏ sʜᴏʀᴛɴᴇʀ sɪᴛᴇ.\n๏Sɪɢɴ ᴜᴩ ᴀɴᴅ ɢᴇɴʀᴀᴛᴇ sʜᴏʀᴛ ʟɪɴᴋs ᴀɴᴅ sʜᴀʀᴇ ᴛʜᴇᴍ ᴛᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Hᴇʟᴩ Mᴇɴᴜ", callback_data="help"),
                        InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
                    ],
                    [
                        InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ Gʀᴏᴜᴩ", url=f"https://t.me/{SUPPORT_GROUP}"),
                        InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")
                    ]
                ]
            )
        )

    elif data == "start":
        await msg.edit(
            START_TXT.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Hᴇʟᴩ Mᴇɴᴜ", callback_data="help"),
                     InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")],
                    [InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                     InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}")],
                    [InlineKeyboardButton("Cʟᴏsᴇ ❌", callback_data="delete")]
                ]
            )
        )
