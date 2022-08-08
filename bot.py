import discord
from discord.ext import commands
from intelligent import send_message
from datos import DISCORD_TOKEN
# Create a discord bot
bot = commands.Bot(command_prefix='>')

# Create on_ready function
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# Create speak command
@bot.command()
async def hablar(ctx, *, msg):
    await ctx.send(send_message(msg))

# Create help command
@bot.command()
async def ayuda(ctx):
    mensaje = '''
AIBO: Bot de discord inteligente.
--------------------------------
--- PREFIX: > ---

Util:
    - >ayuda : Muestra esta ayuda.

Pasar el rato:
    - >hablar : Envía un mensaje a una inteligencia artificial y te responderá

-- FAQ --
¿Como puedo enseñarle cosas a la IA?: Debes contactar con el desarrollador, RinkaDev#9894.
¿Donde puedo ver el codigo?: Actualmente está en Github, habla con el desarrollador.
¿Como funciona la IA?: Está creado con la API Brainshop.ai
Pero Brainshop solo soporta inglés y el chino: Uso la libreria de Deep Translator para acceder a la API de Google Translator.
¿Como puedo sugerir comandos?: Debes contactar con el desarrollador, RinkaDev#9894.
¿Qué hosting usa Aibo?: Heroku.
¿Es heroku gratuito?: Si, te ofrece una cuenta gratuita con 5 apps gratis.
'''
    await ctx.send(mensaje)

# Run bot
bot.run(DISCORD_TOKEN)