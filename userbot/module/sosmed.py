# Port by Koala 🐨/@manuskarakitann
# Nyenyenye bacot

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP


@register(outgoing=True, pattern="^.pint ?(.*)")
@register(outgoing=True, pattern="^.tik ?(.*)")
@register(outgoing=True, pattern="^.ig ?(.*)")
async def insta(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Reply Link Asu.`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Sertakan LinkNya.`")
        return
    chat = "@SaveAsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("Sabar Bentar.")
        return
    await event.edit("`Lagi Proses...` ⌛")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("@SaveAsbot'u `Unblock Dulu Terus Coba Lagi`")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "Akun Private Nih Mek."
            )
        else:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"@bestparrtt 🤍",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
            await event.delete()


@register(outgoing=True, pattern="^.dez(?: |$)(.*)")
async def DeezLoader(event):
    if event.fwd_from:
        return
    dlink = event.pattern_match.group(1)
    if ".com" not in dlink:
        await event.edit("`Sertakan LinkNya Asu`")
    else:
        await event.edit("**Lagi Proses Download** 🎶")
    chat = "@DeezLoadBot"
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.get_response()
            await conv.send_message(dlink)
            details = await conv.get_response()
            song = await conv.get_response()
#                                   #
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("@DeezLoadBot'Unblok Lalu Coba Lagi.")
            return
        await bot.send_file(event.chat_id, song, caption=details.text)

CMD_HELP.update(
    {
        "sosmed": ">`.pint`"
        "\nUsage: Download Media Dari Pinterest"
        "\n\n>`.tik`"
        "\nUsage: Download Vidio TikTok."
        "\n\n>`.ig`"
        "\nUsage: Download Media Dari Instagram."
        "\n\n>`.dez`"
        "\nUsage: Download Lagu Via Deezloader"


    }
)
