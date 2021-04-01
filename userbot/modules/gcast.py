# frm Ultroid
# port by Koala @manusiarakitann
# @LordUserbot_Group

from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern="^.gcast (.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Berikan Saya Teks Untuk Di Broadcast`")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("`• 📢 Proses Mengirim Pesan Siaran! Mohon Sabar...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Berhasil Mengirim Di {done} Chat, Gagal Di {er} Pesan (s)")


CMD_HELP.update(
    {
        "gcast": ".gcast\
    \nMengirim Pesan Siaran Secara Global."
    })
