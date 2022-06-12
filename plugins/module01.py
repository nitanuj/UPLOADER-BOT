import asyncio
from functions.function00 import *
from pyrogram import Client as Clinton
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InputTextMessageContent
from pyrogram.types import InlineQueryResultArticle

@Clinton.on_inline_query()
async def inline(bot, query):

          searche = query.query
          if searche.startswith("1"):
                await inlineX1(bot, query, searche)
          elif searche.startswith("2"):
                await inlineX2(bot, query, searche)
          elif searche.startswith("3"):
                await inlineX3(bot, query, searche)
          elif searche.startswith("4"):
                await inlineX4(bot, query, searche)
          else:
               await results0(bot, query)


async def inlineX1(bot, update, searche):

          answers = []
          search_ts = searche
          query = search_ts.split(" ", 1)[-1]
          torrentList = await SearchYTS(query)
          if not torrentList:
              answers.append(InlineQueryResultArticle(title="𝙉𝙤 𝙏𝙤𝙧𝙧𝙚𝙣𝙩𝙨 𝙁𝙤𝙪𝙣𝙙 𝙞𝙣 𝙏𝙝𝙚𝙋𝙞𝙧𝙖𝙩𝙚𝘽𝙖𝙮!",
              description=f"𝘾𝙖𝙣'𝙩 𝙛𝙞𝙣𝙙 𝙩𝙤𝙧𝙧𝙚𝙣𝙩𝙨 𝙛𝙤𝙧 {query} 𝙞𝙣 𝙏𝙝𝙚𝙋𝙞𝙧𝙖𝙩𝙚𝘽𝙖𝙮 !!",
              input_message_content=InputTextMessageContent(
              message_text=f"𝘾𝙖𝙣'𝙩 𝙛𝙞𝙣𝙙 𝙩𝙤𝙧𝙧𝙚𝙣𝙩𝙨 𝙛𝙤𝙧 `{query}` 𝙞𝙣 𝙏𝙝𝙚𝙋𝙞𝙧𝙖𝙩𝙚𝘽𝙖𝙮 !!", parse_mode="Markdown"),
              reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton("𝙏𝙧𝙮 𝘼𝙜𝙖𝙞𝙣", switch_inline_query_current_chat="1 ") ] ] ) ) )
          else:
              for i in range(len(torrentList)):
                  dl_links = "- " + "\n\n- ".join(torrentList[i]['Downloads'] )
                  answers.append(InlineQueryResultArticle(title=f"{torrentList[i]['Name']}",
                  description=f"Language: {torrentList[i]['Language']}\nLikes: {torrentList[i]['Likes']}, Rating: {torrentList[i]['Rating']}",
                  input_message_content=InputTextMessageContent(
                  message_text=f"**Genre:** `{torrentList[i]['Genre']}`\n"
                               f"**Name:** `{torrentList[i]['Name']}`\n"
                               f"**Language:** `{torrentList[i]['Language']}`\n"
                               f"**Likes:** `{torrentList[i]['Likes']}`\n"
                               f"**Rating:** `{torrentList[i]['Rating']}`\n"
                               f"**Duration:** `{torrentList[i]['Runtime']}`\n"
                               f"**Released on {torrentList[i]['ReleaseDate']}**\n\n"
                               f"**Torrent Download Links:**\n{dl_links}",
                               parse_mode="Markdown", disable_web_page_preview=True),
                  reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton("𝙎𝙚𝙖𝙧𝙘𝙝 𝘼𝙜𝙖𝙞𝙣", switch_inline_query_current_chat="1 ") ] ] ),
                  thumb_url=torrentList[i]["Poster"] ) )
          try:
              await update.answer(results=answers, cache_time=0)
          except QueryIdInvalid:
              await asyncio.sleep(5)
          try:
              await update.answer(results=answers, cache_time=0,
              switch_pm_text="𝙀𝙧𝙧𝙤𝙧: 𝙎𝙚𝙖𝙧𝙘𝙝 𝙩𝙞𝙢𝙚𝙙 𝙤𝙪𝙩!",
              switch_pm_parameter="start",)
          except QueryIdInvalid:
              pass


async def inlineX2(bot, update, searche):


          answers = []
          search_ts = searche
          query = search_ts.split(" ", 1)[-1]
          torrentList = await SearchAnime(query)
          if not torrentList:
              answers.append(InlineQueryResultArticle(title="𝙉𝙤 𝙏𝙤𝙧𝙧𝙚𝙣𝙩𝙨 𝙁𝙤𝙪𝙣𝙙!",
              description=f"𝘾𝙖𝙣'𝙩 𝙛𝙞𝙣𝙙 𝙔𝙏𝙎 𝙩𝙤𝙧𝙧𝙚𝙣𝙩𝙨 𝙛𝙤𝙧 {query} !!",
              input_message_content=InputTextMessageContent(
              message_text=f"𝙉𝙤 𝙛𝙞𝙣𝙙 𝙔𝙏𝙎 𝙩𝙤𝙧𝙧𝙚𝙣𝙩𝙨 𝙛𝙤𝙧 `{query}`", parse_mode="Markdown"),
              reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton("𝙏𝙧𝙮 𝘼𝙜𝙖𝙞𝙣", switch_inline_query_current_chat="2 ") ] ] ) ) )
          else:
              for i in range(len(torrentList)):
                   answers.append(
                        InlineQueryResultArticle(
                            title=f"{torrentList[i]['Name']}",
                            description=f"Seeders: {torrentList[i]['Seeder']}, Leechers: {torrentList[i]['Leecher']}\nSize: {torrentList[i]['Size']}",
                            input_message_content=InputTextMessageContent(
                                message_text=f"**Category:** `{torrentList[i]['Category']}`\n"
                                             f"**Name:** `{torrentList[i]['Name']}`\n"
                                             f"**Seeders:** `{torrentList[i]['Seeder']}`\n"
                                             f"**Leechers:** `{torrentList[i]['Leecher']}`\n"
                                             f"**Size:** `{torrentList[i]['Size']}`\n"
                                             f"**Upload Date:** `{torrentList[i]['Date']}`\n\n"
                                             f"**Magnet:** \n`{torrentList[i]['Magnet']}`\n",
                                parse_mode="Markdown"
                            ),
                            reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton("𝙎𝙚𝙖𝙧𝙘𝙝 𝘼𝙜𝙖𝙞𝙣", switch_inline_query_current_chat="2 ")]]
                            )
                        )
                    )

          try:
              await update.answer(results=answers, cache_time=0)
          except QueryIdInvalid:
              await asyncio.sleep(5)
          try:
              await update.answer(results=answers, cache_time=0,
              switch_pm_text="𝙀𝙧𝙧𝙤𝙧: 𝙎𝙚𝙖𝙧𝙘𝙝 𝙩𝙞𝙢𝙚𝙙 𝙤𝙪𝙩!",
              switch_pm_parameter="start",)
          except QueryIdInvalid:
              pass


async def inlineX3(bot, update, searche):

          answers = []
          search_ts = searche
          query = search_ts.split(" ", 1)[-1]
          torrentList = await Search1337x(query)
          if not torrentList:
              answers.append(InlineQueryResultArticle(title="𝙉𝙤 𝘼𝙣𝙞𝙢𝙚 𝙏𝙤𝙧𝙧𝙚𝙣𝙩𝙨 𝙁𝙤𝙪𝙣𝙙!",
              description=f"𝙉𝙤 𝘼𝙣𝙞𝙢𝙚 𝙏𝙤𝙧𝙧𝙚𝙣𝙩𝙨 𝙁𝙤𝙪𝙣𝙙 𝙁𝙤𝙧 {query} !!",
              input_message_content=InputTextMessageContent(message_text=f"𝙉𝙤 𝘼𝙣𝙞𝙢𝙚 𝙏𝙤𝙧𝙧𝙚𝙣𝙩𝙨 𝙁𝙤𝙪𝙣𝙙 𝙁𝙤𝙧 `{query}`", parse_mode="Markdown"),
              reply_markup=InlineKeyboardMarkup( [ [InlineKeyboardButton("𝙏𝙧𝙮 𝘼𝙜𝙖𝙞𝙣", switch_inline_query_current_chat="3 ") ] ] ) ) )
          else:
              for i in range(len(torrentList)):
                  answers.append(
                    InlineQueryResultArticle(
                        title=f"{torrentList[i]['Name']}",
                        description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}, Downloads: {torrentList[i]['Downloads']}",
                        input_message_content=InputTextMessageContent(
                            message_text=f"**Category:** `{torrentList[i]['Category']}`\n"
                                         f"**Name:** `{torrentList[i]['Name']}`\n"
                                         f"**Language:** `{torrentList[i]['Language']}`\n"
                                         f"**Seeders:** `{torrentList[i]['Seeders']}`\n"
                                         f"**Leechers:** `{torrentList[i]['Leechers']}`\n"
                                         f"**Size:** `{torrentList[i]['Size']}`\n"
                                         f"**Downloads:** `{torrentList[i]['Downloads']}`\n"
                                         f"__Uploaded by {torrentList[i]['UploadedBy']}__\n"
                                         f"__Uploaded {torrentList[i]['DateUploaded']}__\n"
                                         f"__Last Checked {torrentList[i]['LastChecked']}__\n\n"
                                         f"**Magnet:**\n`{torrentList[i]['Magnet']}`\n",
                            parse_mode="Markdown"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("𝙎𝙚𝙖𝙧𝙘𝙝 𝘼𝙜𝙖𝙞𝙣", switch_inline_query_current_chat="3 ")]]
                        ),
                        thumb_url=torrentList[i]['Poster']
                    )
                )
          try:
              await update.answer(results=answers, cache_time=0)
          except QueryIdInvalid:
              await asyncio.sleep(5)
          try:
              await update.answer(results=answers, cache_time=0,
              switch_pm_text="𝙀𝙧𝙧𝙤𝙧: 𝙎𝙚𝙖𝙧𝙘𝙝 𝙩𝙞𝙢𝙚𝙙 𝙤𝙪𝙩!",
              switch_pm_parameter="start",)
          except QueryIdInvalid:
              pass


async def inlineX4(bot, update, searche):

          answers = []
          search_ts = searche
          query = search_ts.split(" ", 1)[-1]
          torrentList = await SearchPirateBay(query)
          if not torrentList:
              answers.append(InlineQueryResultArticle(title="𝙉𝙤 𝘼𝙣𝙞𝙢𝙚 𝙏𝙤𝙧𝙧𝙚𝙣𝙩𝙨 𝙁𝙤𝙪𝙣𝙙!",
              description=f"𝙉𝙤 𝘼𝙣𝙞𝙢𝙚 𝙏𝙤𝙧𝙧𝙚𝙣𝙩𝙨 𝙁𝙤𝙪𝙣𝙙 𝙁𝙤𝙧 {query} !!",
              input_message_content=InputTextMessageContent(message_text=f"𝙉𝙤 𝘼𝙣𝙞𝙢𝙚 𝙏𝙤𝙧𝙧𝙚𝙣𝙩𝙨 𝙁𝙤𝙪𝙣𝙙 𝙁𝙤𝙧 `{query}`", parse_mode="Markdown"),
              reply_markup=InlineKeyboardMarkup( [ [InlineKeyboardButton("𝙏𝙧𝙮 𝘼𝙜𝙖𝙞𝙣", switch_inline_query_current_chat="4 ") ] ] ) ) )
          else:
              for i in range(len(torrentList)):
                    answers.append(
                        InlineQueryResultArticle(
                            title=f"{torrentList[i]['Name']}",
                            description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}",
                            input_message_content=InputTextMessageContent(
                                message_text=f"**Category:** `{torrentList[i]['Category']}`\n"
                                             f"**Name:** `{torrentList[i]['Seeders']}`\n"
                                             f"**Size:** `{torrentList[i]['Size']}`\n"
                                             f"**Seeders:** `{torrentList[i]['Seeders']}`\n"
                                             f"**Leechers:** `{torrentList[i]['Leechers']}`\n"
                                             f"**Uploader:** `{torrentList[i]['Uploader']}`\n"
                                             f"**Uploaded on {torrentList[i]['Date']}**\n\n"
                                             f"**Magnet:**\n`{torrentList[i]['Magnet']}`",
                                parse_mode="Markdown"
                            ),
                            reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton("𝙎𝙚𝙖𝙧𝙘𝙝 𝘼𝙜𝙖𝙞𝙣", switch_inline_query_current_chat="4 ")]])
                        )
                    )
          try:
              await update.answer(results=answers, cache_time=0)
          except QueryIdInvalid:
              await asyncio.sleep(5)
          try:
              await update.answer(results=answers, cache_time=0,
              switch_pm_text="𝙀𝙧𝙧𝙤𝙧: 𝙎𝙚𝙖𝙧𝙘𝙝 𝙩𝙞𝙢𝙚𝙙 𝙤𝙪𝙩!",
              switch_pm_parameter="start",)
          except QueryIdInvalid:
              pass


async def results0(bot, update):
          print("👀")
