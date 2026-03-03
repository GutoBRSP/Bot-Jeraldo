from bot_logic import *
from discord.ext import commands
import discord
import os
import random
import requests

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

# Comando para enviar uma imagem
@bot.command()
async def meme(ctx):
    with open('imagens/Programação.png', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

#usando a biblioteca os e o comando lisdir
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('imagens'))
    
    with open(f'imagens/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

# Comando para enviar uma imagem aleatória de pato
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# Executar o bot (coloque seu token aqui)
bot.run("")
