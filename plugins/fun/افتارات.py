"""
**❃ جميع هذه الاوامر تستخدم بالأرسال فقط**

❃ `{i}حالات`
❃ `{i}ستوري انمي`
❃ `{i}رقيه`
❃ `{i}رمادي`
❃ `{i}رماديه`
❃ `{i}بيست`
❃ `{i}حب`
❃ `{i}رياكشن`
❃ `{i}ادت`
❃ `{i}غنيلي`
❃ `{i}شعر`
❃ `{i}ميمز`
❃ `{i}ري اكشن`
❃ `{i}معلومه`
❃ `{i}تويت`
❃ `{i}خيرني`
❃ `{i}ولد انمي`
❃ `{i}بنت انمي`
❃ `{i}بنات`

سورس ميكثون ୭‌✧ 
"""

import asyncio
import os
from secrets import choice
import random
from urllib.parse import quote_plus
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice, InputMessagesFilterPhotos

from .. import eor, jmthon_cmd

# تعريف الدوال المساعدة
async def edit_or_reply(event, text):
    """دالة للرد على الرسالة أو تعديلها"""
    try:
        if event.is_reply:
            replied = await event.get_reply_message()
            return await replied.reply(text)
        return await event.reply(text)
    except:
        return await event.edit(text)

async def eor(event, text):
    """دالة مختصرة لـ edit_or_reply"""
    return await edit_or_reply(event, text)

# الأوامر الأصلية بدون تغيير
@jmthon_cmd(pattern="حالات$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل حـالات واتـس ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@RSHDO5", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**🎆┊حـالات واتـس قصيـرة 🧸♥️**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="ستوري انمي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الستـوري ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@AA_Zll", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**🎆┊ستـوريات آنمـي قصيـرة 🖤🧧**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="رقيه$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرقيـه ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@Rqy_1", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**◞مقاطـع رقيـه شرعيـة ➧🕋🌸◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="رمادي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الافتـار ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@shababbbbR", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات شبـاب ࢪمـاديه ➧🎆🖤◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="رماديه$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الافتـار ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@banatttR", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات بنـات ࢪمـاديه ➧🎆🤎◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="بيست$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...🧚🏻‍♀🧚🏻‍♀╰**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@Tatkkkkkim", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات بيست تطقيـم بنـات ➧🎆🧚🏻‍♀🧚🏻‍♀◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="حب$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...♥️╰**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@tatkkkkkimh", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات حـب تمبلـرࢪ ➧🎆♥️◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="رياكشن$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرياكشـن ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@reagshn", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"** 🎬┊رياكشـن تحشيـش ➧🎃😹◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="ادت$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل مقطـع ادت ...**")
    try:
        ZTHONR = [
            asupan
            async for asupan in event.client.iter_messages(
                "@snje1", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**🎬┊مقاطـع ايـدت منوعـه ➧ 🖤🎭◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="غنيلي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الاغنيـه ...𓅫╰**")
    try:
        zedgan = [
            desah
            async for desah in event.client.iter_messages(
                "@TEAMSUL", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**✦┊تم اختياࢪ الاغنيـه لك 💞🎶**\nٴ▁ ▂ ▉ ▄ ▅ ▆ ▇ ▅ ▆ ▇ █ ▉ ▂ ▁",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="شعر$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الشعـر ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@L1BBBL", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**✦┊تم اختيـار مقطـع الشعـر هـذا لك**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="ميمز$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الميمـز ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@MemzWaTaN", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**✦┊تم اختيـار مقطـع الميمـز هـذا لك**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="ري اكشن$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرياكشـن ...**")
    try:
        zedre = [
            zlzz7
            async for zlzz7 in event.client.iter_messages(
                "@gafffg", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedre),
            caption=f"**🎆┊رياكشـن تحشيـش ➧🎃😹◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="معلومه$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل صـورة ومعلومـة ...**")
    try:
        zedph = [
            zilzal
            async for zilzal in event.client.iter_messages(
                "@A_l3l", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**🎆┊صـورة ومعلومـة ➧ 🛤💡◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="تويت$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ كـت تـويت بالصـور ...**")
    try:
        zedre = [
            zlzz7
            async for zlzz7 in event.client.iter_messages(
                "@twit_selva", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedre),
            caption=f"**✦┊كـت تـويت بالصـور ➧⁉️🌉◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="خيرني$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ لـو خيـروك بالصـور ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@SourceSaidi", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**✦┊لـو خيـروك  ➧⁉️🌉◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="ولد انمي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...𓅫╰**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@dnndxn", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات آنمي شبـاب ➧🎆🙋🏻‍♂◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="بنت انمي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...𓅫╰**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@shhdhn", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات آنمي بنـات ➧🎆🧚🏻‍♀◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")

@jmthon_cmd(pattern="بنات$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...𓅫╰**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@banaaaat1", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات بنـات تمبلـرࢪ ➧🎆🧚🏻‍♀◟**",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")