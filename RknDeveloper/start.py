#(©) @RknDeveloper ✨


from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, enums, errors
from pyrogram.errors import UserNotParticipant
from RknDeveloper.untils.database import add_user, add_group
from configs import rkn1
import random, asyncio
import os


# Main Process _ _ _ _ _ Users Send Massage 🥀__🥀 Please 😢 Give Credit

@Client.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(bot, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await bot.send_message(
            rkn1.LOG_CHANNEL,
            f"**--#NᴇᴡGʀᴏᴜᴘ @MoviGenX--**\n\nCʜᴀɴɴᴇʟ & Gʀᴏᴜᴘ Iᴅ: {m.chat.id}\nTɪᴛʟᴇ: `{m.chat.title}`\nUɴ: @{m.chat.username}\n\nBʏ: {m.from_user.mention}"
        )
        await bot.approve_chat_join_request(op.id, kk.id)
        img = random.choice(rkn1.SURPRICE)
        await bot.send_video(kk.id,img, "**Hello {}!\nWelcome To {}\n\n__Pᴏᴡᴇʀᴅ Bʏ : @MoviGenX__**".format(m.from_user.mention, m.chat.title), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url=f"https://t.me/AcceptJoinRequestsBot?startchannel=Bots4Sale&admin=invite_users+manage_chat")],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url=f"https://t.me/AcceptJoinRequestsBot?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                
            ]])            )
        add_user(m.from_user.id)
        await bot.send_message(
            rkn1.LOG_CHANNEL,
            f"**--Nᴇᴡ Uꜱᴇʀ Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bᴏᴛ--**\n\nUꜱᴇʀ: {m.from_user.mention}\nIᴅ: `{m.from_user.id}`\nUɴ: @{m.from_user.username}"
            )
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    

# Start Massage _____ # Please 😢 Give Credit 

@Client.on_message(filters.command("start"))
async def op(bot, m :Message):
    try:
        await bot.get_chat_member(rkn1.UPDATECHANNEL_ID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("─シ｡Aʙᴏᴜᴛ｡シ─", callback_data = "about")
                    ],[
                InlineKeyboardButton("𖣘 Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url="https://t.me/MoviGenX"),
                InlineKeyboardButton("🛍️ 𝕯𝖊𝖆𝖑 𝕮𝖍𝖆𝖓𝖓𝖊𝖑", url="https://t.me/CheapieDeals")
                ],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url=f"https://t.me/AcceptJoinRequestsBot?startchannel=Bots4Sale&admin=invite_users+manage_chat")],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url=f"https://t.me/AcceptJoinRequestsBot?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                
            ]])            
    
            add_user(m.from_user.id)
            await bot.send_message(
            rkn1.LOG_CHANNEL,
            f"**--Nᴇᴡ Uꜱᴇʀ Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bᴏᴛ--**\n\nUꜱᴇʀ: {m.from_user.mention}\nIᴅ: `{m.from_user.id}`\nUɴ: @{m.from_user.username}"
            )
            await m.reply_photo(photo=rkn1.RKN_PIC, caption="**🦊 Hᴇʟʟᴏ {}!\n\nI'ᴍ Aɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ [Aᴅᴍɪɴ Jᴏɪɴ Rᴇǫᴜᴇsᴛs]({}) Bᴏᴛ.\nI Cᴀɴ Aᴘᴘʀᴏᴠᴇ Usᴇʀs Iɴ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs.Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ ᴀɴᴅ Pʀᴏᴍᴏᴛᴇ Mᴇ Tᴏ Aᴅᴍɪɴ Wɪᴛʜ Aᴅᴅ Mᴇᴍʙᴇʀs Pᴇʀᴍɪssɪᴏɴ.\n\n__Pᴏᴡᴇʀᴅ Bʏ : @MoviGenX__**".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)
            
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Pʀɪᴠᴀᴛᴇ", url="https://t.me/AcceptJoinRequestsBot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await bot.send_message(
            rkn1.LOG_CHANNEL,
            f"**--#NᴇᴡGʀᴏᴜᴘ @MoviGenX--**\n\nCʜᴀɴɴᴇʟ & Gʀᴏᴜᴘ Iᴅ: {m.chat.id}\nTɪᴛʟᴇ: `{m.chat.title}`\nUɴ: @{m.chat.username}\n\nBʏ: {m.from_user.mention}"
            )
            await m.reply_text("**❣️ Hᴇʟʟᴏ {}!\n\nWʀɪᴛᴇ Mᴇ Pʀɪᴠᴀᴛᴇ Fᴏʀ Mᴏʀᴇ Dᴇᴛᴀɪʟs.**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🥀 Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 🥀", url=f"https://t.me/MoviGenX")],[
                    InlineKeyboardButton("𖤍 Tʀʏ Aɢᴀɪɴ ༗", "rkn_developer")
                ]
            ]
        )
        await m.reply_text("**💞 Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Tʜɪs Bᴏᴛ!. Iғ Yᴏᴜ Jᴏɪɴᴇᴅ Cʟɪᴄᴋ Tʀʏ Aɢᴀɪɴ Bᴜᴛᴛᴏɴ Tᴏ Cᴏɴғɪʀᴍ. 🥀**".format(rkn1.UPDATE_CHANNEL), reply_markup=key)

