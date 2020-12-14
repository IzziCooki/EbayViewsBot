import requests
import discord
from discord.ext import commands, tasks
from pytz import timezone
from discord import embeds
from datetime import datetime
import time
import pytz
import t
import tweepy
import json
from PIL import Image

from selenium import webdriver

PATH = 'chromedriver.exe'
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.idle,
        activity=discord.Game(".commands to start"))
    print("Bot it ready.")


@client.command()
async def views(ctx, *, link, member: discord.member = None):
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = member.create_dm()
        await channel.send("%s Sending Views")

    embed = discord.Embed(
        title="Ebay View Gen",
        description="Sending 100 Views!",
        colour=discord.Colour.green())
    embed.set_footer(text=f"IzziCooki#0001 {current_time}")
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/750415281431511082/765716553714106378/text.gif"
    )
    embed_after = discord.Embed(
        title="Ebay View Gen",
        description="Views Sent!",
        color=discord.Colour.green())
    embed_after.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/750415281431511082/765716553714106378/text.gif"
    )
    embed_after.set_footer(text=f"IzziCooki#0001 : Start time: {current_time}")
    https = link[:8]
    http = link[:7]
    print(http)
    if https == "https://" or http == "http://":
        await ctx.send(embed=embed)
        await send_views(link)
        await ctx.send(embed=embed_after)
    else:
        await ctx.send("Please Enter Vaild Address")

    print(link)


async def send_views(link):
    print(f"Task has started! ")  
    for i in range(100):
        r = requests.get(link)
    print("Task Complete")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command()
@commands.has_permissions()
async def clear(ctx, amount):
    amount = int(amount)
    await ctx.channel.purge(limit=amount)



@client.command()
async def fees(ctx, price):
    ebay_price = float(price) * float(.87) - float(0.3)
    ebay_price = int(ebay_price)

    stockx_price_1 = float(price) * float(.875)
    stockx_price_1 = int(stockx_price_1)

    stockx_price_2 = float(price) * float(.88)
    stockx_price_2 = int(stockx_price_2)

    stockx_price_3 = float(price) * float(.885)
    stockx_price_3 = int(stockx_price_3)

    stockx_price_4 = float(price) * float(.89)
    stockx_price_4 = int(stockx_price_4)

    goat_price = float(price) * float(.876)
    goat_price = int(goat_price + 5)

    mercari_price = float(price) * float(.9)
    mercari_price = int(mercari_price)

    final_price = f"Ebay (12.9% + $0.3): {ebay_price} \n " \
                  f"StockX Seller Level 1 (12.5%): {stockx_price_1} \n " \
                  f"StockX Seller Level 2 (12.0%): {stockx_price_2} \n " \
                  f"StockX Seller Level 3 (11.5%):  {stockx_price_3} \n " \
                  f"StockX Seller Level 4 (11.0%): {stockx_price_4} \n" \
                  f" Goat (12.4% + $5): {goat_price} \n " \
                  f"Mercari (10%): {mercari_price}"

    goat_price = float(price) * float(.876)
    goat_price = int(goat_price + 5)
    embed = discord.Embed(
        title="Fee Calculator: $" + price,
        description=final_price,
        colour=discord.Colour.blue())
    embed.set_footer(
        text=f"Developed by IzziCooki#0001 : Start time: {current_time}", )
    embed.set_author(name="Ebot.io", )
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/750415281431511082/765716553714106378/text.gif"
    )
    await ctx.send(embed=embed)


@client.command()
async def commands(ctx):
    embed = discord.Embed(
        title="Ebay Gen Help",
        description=
        "Usable Commands: \n \n .views (link) : Send Ebay Views \n \n.fees (price) : Calculate the profit after selling fees \n \n.delay (tasks) (proxies): Calculates the delay to run for the amount of tasks and proxies you have \n \n.commands: Shows this text",
        colour=discord.Colour.red())
    embed.set_footer(
        text=f"Developed by IzziCooki#0001 : Start time: {current_time}")
    embed.set_author(name="Ebot.io", )
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/750415281431511082/765716553714106378/text.gif"
    )
    await ctx.send(embed=embed)


@client.command()
async def delay(ctx, tasks, proxies):

    delay = 3500
    tasks = int(tasks)
    proxies = int(proxies)
    if tasks > 0 and proxies == 0:
        await ctx.send("Infinite Delay")
    elif tasks == 0 and proxies == 0:
        await ctx.send("Error")
    elif tasks == 0 and proxies > 0:
        await ctx.send("You must run task!")
    cal = tasks * delay / proxies
    cal = int(cal)

    embed = discord.Embed(
        title="Shopify Delay Calculator",
        description=f"{tasks} tasks \n {proxies} proxies \n Delay: {cal}",
        color=discord.Colour.blurple())
    embed.set_footer(
        text=f"Developed by IzziCooki#0001 : Start time: {current_time}", )
    embed.set_author(name="Ebot.io", )
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/750415281431511082/765716553714106378/text.gif"
    )

    await ctx.send(embed=embed)


"""@client.event
async def on_message(message):
    print(message.attachments)
    for attachment in message.attachments:
    # Do what you want with attachment.url
      print(attachment.url)


      CONSUMER_KEY = "BhgwlGKfAK4GTjXkOFZOWR9cs"
      CONSUMER_SECRET  = "KpJiT1FlGAzmR1FN7gEuE7u5wclMbakA25MtQWXQpHj5hTBKOg"
      ACCESS_TOKEN = '1105327574069202944-ivdmWaSzIH2705Kw9IrQBGh5Erhy1k'
      ACCESS_TOKEN_SECRET = 'gvQKF2kz44gvT9oZsb30zg6MvHrDri0lbPNiZPUjaGdlQ'

      auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
      auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
      api = tweepy.API(auth)
      message.attachments.url.saveToFile()
      with open(message.attachments, 'r') as f:
        temp = json.load(f)

      with open('images.json', 'w') as f:
        json.dump(temp, f, indent=4)
"""
@client.command()
async def upload_file(ctx):
    attachment_url = ctx.message.attachments[0].url
    file_request = requests.get(attachment_url)
    print(file_request.content)  
    x = bytes('Python, bytes', 'file_request','utf8')
    print(x)


@client.command()
async def yt(link):
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get(link)
    driver.sleep(10)
    driver.close()


    
client.run('')
