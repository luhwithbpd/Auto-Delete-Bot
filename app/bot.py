import discord
from discord.ext import commands
from config import TOKEN, CANAL_PERMITIDO_ID

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=";", intents=intents)

@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id != CANAL_PERMITIDO_ID:
        return

    if message.content.startswith("m!"):
        try:
            await message.delete()
            print(f"Mensagem apagada: {message.content}")
        except Exception as e:
            print(f"Erro ao apagar mensagem: {e}")

    await bot.process_commands(message)

bot.run(TOKEN)