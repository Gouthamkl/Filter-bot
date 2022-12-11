import os
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.handlers import MessageHandler
from pyshorteners import Shortener

BITLY_API = os.environ.get("BITLY_API", "8df1df8c23f719e5cf97788cc2d40321ea30092b")
CUTTLY_API = os.environ.get("CUTTLY_API", "f64dffbde033b6c307387dd50b7c76e505f1c")
SHORTCM_API = os.environ.get("SHORTCM_API", "pk_...NIZv")
GPLINKS_API = os.environ.get("GPLINKS_API", "008ccaedd6061ad1948838f410947603de9007a7")

reply_markup = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Close", callback_data='close_data')
        ]]
    )

@Client.on_message(filters.command(["short"]) & filters.regex(r'https?://[^\s]+'))
async def reply_shortens(bot, update):
    message = await update.reply_text(
        text="`Analysing your link...`",
        disable_web_page_preview=True,
        quote=True
    )
    link = update.matches[0].group(0)
    shorten_urls = await short(link)
    await message.edit_text(
        text=shorten_urls,
        disable_web_page_preview=True
    )

@Client.on_inline_query(filters.regex(r'https?://[^\s]+'))
async def inline_short(bot, update):
    link = update.matches[0].group(0),
    shorten_urls = await short(link)
    answers = [
        InlineQueryResultArticle(
            title="Short Links",
            description=update.query,
            input_message_content=InputTextMessageContent(
                message_text=shorten_urls,
                disable_web_page_preview=True
            ),
            reply_to_message_id=message.message_id
        )
    ]
    await bot.answer_inline_query(
        inline_query_id=update.id,
        results=answers
    )

async def short(link):
    shorten_urls = "**--Shorted URLs--**\n"
    
    # Bit.ly shorten
    if BITLY_API:
        try:
            s = Shortener(api_key=BITLY_API)
            url = s.bitly.short(link)
            shorten_urls += f"\n**𝖡𝗂𝗍.𝗅𝗒 -**\n{url}"
        except Exception as error:
            print(f"Bit.ly error :- {error}")
    
    # Chilp.it shorten
    try:
        s = Shortener()
        url = s.chilpit.short(link)
        shorten_urls += f"\n\n**𝖢𝗁𝗂𝗅𝗉.𝖨𝗍 -**\n{url}"
    except Exception as error:
        print(f"Chilp.it error :- {error}")
    
    # Clck.ru shorten
    try:
        s = Shortener()
        url = s.clckru.short(link)
        shorten_urls += f"\n\n**𝖢𝗅𝗂𝖼𝗄.𝗋𝗎 -**\n{url}"
    except Exception as error:
        print(f"Click.ru error :- {error}")
    
    # Cutt.ly shorten
    if CUTTLY_API:
        try:
            s = Shortener(api_key=CUTTLY_API)
            url = s.cuttly.short(link)
            shorten_urls += f"\n\n**𝖢𝗎𝗍𝗍.𝗅𝗒 -**\n{url}"
        except Exception as error:
            print(f"Cutt.ly error :- {error}")
    
    # Da.gd shorten
    try:
        s = Shortener()
        url = s.dagd.short(link)
        shorten_urls += f"\n\n**𝖣𝖺.𝗀𝖽 -**\n{url}"
    except Exception as error:
        print(f"Da.gd error :- {error}")
    
    # Is.gd shorten
    try:
        s = Shortener()
        url = s.isgd.short(link)
        shorten_urls += f"\n\n**𝖨𝗌.𝗀𝖽 -**\n{url}"
    except Exception as error:
        print(f"Is.gd error :- {error}")
    
    # Osdb.link shorten
    try:
        s = Shortener()
        url = s.osdb.short(link)
        shorten_urls += f"\n\n**𝖮𝗌𝖽𝖻.𝗅𝗂𝗇𝗄 -**\n{url}"
    except Exception as error:
        print(f"Osdb.link error :- {error}")
    
    # Ow.ly shorten
    try:
        s = Shortener()
        url = s.owly.short(link)
        shorten_urls += f"\n\n**𝖮𝗐.𝗅𝗒 -**\n{url}"
    except Exception as error:
        print(f"Ow.ly error :- {error}")
    
    # Po.st shorten
    try:
        s = Shortener()
        url = s.post.short(link)
        shorten_urls += f"\n\n**𝖯𝗈.𝗌𝗋 -**\n{url}"
    except Exception as error:
        print(f"Po.st error :- {error}")
    
    # Qps.ru shorten
    try:
        s = Shortener()
        url = s.qpsru.short(link)
        shorten_urls += f"\n\n**𝖰𝗉𝗌.𝗋𝗎 -**\n{url}"
    except Exception as error:
        print(f"Qps.ru error :- {error}")
    
    # Short.cm shorten
    if SHORTCM_API:
        try:
            s = Shortener(api_key=SHORTCM_API)
            url = s.shortcm.short(link)
            shorten_urls += f"\n\n**𝖲𝗁𝗈𝗋𝗍.𝖼𝗆 -**\n{url}"
        except Exception as error:
            print(f"Short.cm error :- {error}")
    
    # TinyURL.com shorten
    try:
        s = Shortener()
        url = s.tinyurl.short(link)
        shorten_urls += f"\n\n**𝖳𝗂𝗇𝗒𝖴𝗋𝗅.𝖼𝗈𝗆 -**\n{url}"
    except Exception as error:
        print(f"TinyURL.com error :- {error}")
    
    # NullPointer shorten
    try:
        s = Shortener(domain='https://0x0.st')
        url = s.nullpointer.short(link)
        shorten_urls += f"\n\n**0𝗑0.𝗌𝗍 -**\n{url}"
    except Exception as error:
        print(f"NullPointer error :- {error}")
    
    # GPLinks shorten
    try:
        api_url = "https://gplinks.in/api"
        params = {'api': GPLINKS_API, 'url': link}
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url, params=params, raise_for_status=True) as response:
                data = await response.json()
                url = data["shortenedUrl"]
                shorten_urls += f"\n\n**𝖦𝗉𝖫𝗂𝗇𝗄𝗌.𝗂𝗇-**\n{url}"
    except Exception as error:
        print(f"GPLink error :- {error}")
    
    # Send the text
    try:
        shorten_urls += ""
        return shorten_urls
    except Exception as error:
        return error
