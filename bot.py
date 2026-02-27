from bot_logic import *
from discord.ext import commands
import discord

# Permissões do bot
intents = discord.Intents.default()
intents.message_content = True

# Criar o bot com prefixo $
bot = commands.Bot(command_prefix="$", intents=intents)

# Evento: quando o bot estiver pronto
@bot.event
async def on_ready():
    print(f"Fizemos login como {bot.user}")

# Comando: hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

# Comando: bye
@bot.command()
async def bye(ctx):
    await ctx.send("🙂")

# 💎 Comando: info (Embed bonito)
@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="🤖 Meu Bot",
        description="Eu sou um bot em desenvolvimento na aula de hoje!",
        color=discord.Color.green()
    )

    embed.add_field(
        name="📌 Comandos disponíveis:",
        value="$hello\n$bye\n$senha\n$info",
        inline=False
    )

    embed.set_footer(text="Criado durante a aula de programação 😄")

    await ctx.send(embed=embed)

# Comando para gerar senha
@bot.command()
async def senha(ctx):
    password = gen_pass(10)  # Gerar uma senha de 10 caracteres
    await ctx.send(f"Senha gerada: `{password}`")

# Comando para gerar emodji aleatório
@bot.command(name="emoji")
async def enviar_emoji(ctx):
    """Envia um emoji aleatório"""
    emoji = gen_emodji()
    await ctx.send(emoji)

# Executar o bot (coloque seu token aqui)
bot.run("TOKEN AQUI!")
