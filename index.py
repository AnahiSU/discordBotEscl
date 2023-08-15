import discord
from discord.ext import commands
import json 
import random
from keepAlive import keep_alive

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all() )
@bot.event
async def onReady():
    print("The bot is ready!")
    await bot.change_presence(status=discord.Status.do_not_disturb, activity= "escuchando a mis amos")

@bot.command()
async def hello(ctx):
    await ctx.send("Wenas wenas")
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def horario(ctx):
    await ctx.send("Aquí tienes el Cappuchino de la Scesi: http://2023.cappuchino.scesi.umss.edu.bo/")

@bot.command(pass_context=True)
async def joinChannel(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Primero conéctate a un canal de voz y yo te sigo.")

@bot.command(pass_context=True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Nos fuimos, desaparecimos")
    else:
        await ctx.send("¿Esquizofrenia? No estoy en el canal de voz.")
        
@bot.command()
async def sumita(ctx, num1: int, num2: int):
    res = str(num1 + num2)
    await ctx.send("La humilde suma es: "+ res)

@bot.command()
async def randomEntre(ctx, n1: int, n2:int):
    ran = str(random.randint(n1, n2))
    await ctx.send("¿Qué te parece " + ran + "?")

@bot.command()
async def rollDice(ctx):
    ran = str(random.randint(1,6))
    await ctx.send("El dado muestra " + ran)

@bot.command()
async def rollTwice(ctx):
    ran1 = random.randint(1,6)
    ran2 = random.randint(1,6)
    sum = str(ran1 + ran2)
    await ctx.send("El primer dado muestra " + str(ran1) + " y el segundo " + str(ran2)+". La suma es "+sum)

@bot.command()
async def lolsito(ctx):
    await ctx.send("Es una droga maligna creada por RiotGames. De este server Leo es el que más lo jugó y las secuelas fueron terribles, pero ya se está rehabilitando, aunque puede recaer... https://www.leagueoflegends.com/es-es dejaré esto aquí y me iré...")

@bot.command()
async def prediction(ctx, arg):
    ran = random.randint(1,7)
    if(ran == 1):
        msg = "Puede ser choquito."
    elif(ran==2):
        msg = "Yo no estaría tan seguro."
    elif(ran==3):
        msg = "El que tenga miedo, que no nazca B)"
    elif(ran==4):
        msg = "Solo si el guionista de tu vida es piadoso."
    elif(ran==5):
        msg = "Positivo mirrey."
    elif(ran==6):
        msg = "No tengo dudas pero tampoco pruebas."
    else:
        msg="Ni lo pienses"
    await ctx.send(msg)

@bot.command()
async def java(ctx):
    await ctx.send("Somos parte del culto Java Supremacy amigo, nada de que Python es mejor o que viva JS porque baneadísimo.")

@bot.command()
async def websiss(ctx):
    await ctx.send("Websiss a su orden mientras no se haya caído: https://websis.umss.edu.bo/serv_estudiantes.asp")

@bot.command()
async def reverseThis(ctx, arg):
    res = ""
    for i in range(len(arg)-1,-1,-1):
        res = res + arg[i]
    await ctx.send(res)

@bot.command()
async def adios(ctx):
    await ctx.send("Nos vemos, wenas noches")

@bot.command()
async def kitty(ctx):
    embed = discord.Embed(title="Gatito", color=discord.Color.blue())
    embed.set_image(url="https://i.pinimg.com/originals/21/b6/f9/21b6f9ac6bbf9e55768ea530a5a4c8af.jpg")
    await ctx.send(embed=embed)
    

@bot.command()
async def mallaInfo(ctx):
    embed = discord.Embed(title="Esta es la malla curricular de ingeniería informática, la mejor ingeniería B)", color=discord.Color.blue())
    embed.set_image(url="https://www.umss.edu.bo/wp-content/uploads/2019/07/informatica.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def mallaSistemas(ctx):
    embed = discord.Embed(title="Esta es la malla curricular de ingeniería en sistemas, AKA sistemitas", color=discord.Color.blue())
    embed.set_image(url="https://www.umss.edu.bo/wp-content/uploads/2019/07/sistemas.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def helpMe(ctx):
    embed = discord.Embed(title="Ayudita",description="Aquí los comandos disponibles", color=discord.Color.brand_green())
    embed.add_field(name="ping",value="pong.",inline=False)
    embed.add_field(name="hello",value="Hay que ser educados y saludar.",inline=False)
    embed.add_field(name="rollTwice",value="Tira dos dados de 6 caras aleatorio, te da los resultados y además te da la suma.",inline=False)
    embed.add_field(name="rollDice",value="Tira un dado de 6 caras aleatorio y te da el resultado.",inline=False)
    embed.add_field(name="randomEntre",value="Escribiendo el comando y dándole dos números, el primero el menor y el segundo el mayor, te devolverá un número aleatorio en ese rango incluyente.",inline=False)
    embed.add_field(name="joinChannel",value="Permite que Esclavito se una al canal de voz, en caso de que quien mandó el mensaje lo esté.",inline=False)
    embed.add_field(name="leave",value="Hace que Esclavito deje el canal de voz en caso de estar en uno.",inline=False)
    embed.add_field(name="kitty",value="¿Quieres ver un gatito?.",inline=False)
    embed.add_field(name="prediction",value="Pregúntale algo a Esclavito y él te dirá su más sincera quackpinión al respecto.",inline=False)
    embed.add_field(name="reverseThis",value='Voltea la palabra que pongas entre comillas luego del comando. Por ejemplo: .reverseThis "hola" -> aloh.',inline=False)
    embed.add_field(name="websiss",value="Facilita la página del websiss para estudiantes.",inline=False)
    embed.add_field(name="horario",value="Facilita la página de Cappuchino by Scesi UMSS.",inline=False)
    embed.add_field(name="java",value="Si te encantan otros lenguajes, mejor ni lo pruebes.",inline=False)
    embed.add_field(name="lolsito",value="¿Quieres morir joven?",inline=False)
    embed.add_field(name="adios",value="La educación sobre todo.",inline=False)
    embed.add_field(name="sumita",value="Una suma sencilla entre dos números.",inline=False)
    embed.add_field(name="mallaInfo",value="Muestra la malla curricular de ingeniería informática en la UMSS.",inline=False)
    embed.add_field(name="mallaSistemas",value="Muestra la malla curricular de ingeniería en sistemas en la UMSS.",inline=False)
    await ctx.send(embed=embed)

keep_alive()
bot.run('Discord key here')
