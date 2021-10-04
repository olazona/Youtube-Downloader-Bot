from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Owner", url="https://t.me/Ola_z_slim_yoda")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Ola_z_slim_yoda")]
    ])
    welcomed = f"Hello <b>{message.from_user.first_name}.</b>\n/help for More info.\nCreated by Ola Zona"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
