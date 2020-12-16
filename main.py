#!/usr/bin/python
# coding: latin-1

from resources.warframemarket import *
from resources.warframestats import *

from CobraLib import updateservercount, getip
from StorageConfig import Settings, Traduction, help

import time
import discord


def options(args, message):
    try:
        if args[1] == args[2]:
            str(args[2])
    except IndexError:
        return Traduction.optionError()
    else:
        pass
    args[2] = args[2].replace('"', '')
    if args[1] == 'commandbegin':
        configch(str(message.guild.id), 'COMMANDBEGIN', args[2])
        return Traduction.optioncommandbegin(args[2])
    elif args[1] == 'language':
        if args[2] == 'fr':
            configch(str(message.guild.id), 'LANGUAGE', 'fr')
            return "Le bot est maintenant en français."
        elif args[2] == 'en':
            configch(str(message.guild.id), 'LANGUAGE', 'en')
            return "The bot is now in english."
        elif args[2] == 'pt':
            configch(str(message.guild.id), 'LANGUAGE', 'pt')
            return "O robô está agora em português."
        else:
            return "The bot is only available in english,french and portuguese.(en,fr,pt)"
    elif args[1] == 'timer':
        try:
            timer = int(args[2])
        except AttributeError:
            timer = 0 ##TODO Error si autre qu'un chiffre au lieu de 0
        if timer > 5:
            timer = 5
        elif 0 > timer:
            timer = 0
        configch(str(message.guild.id), 'TIMER', int(timer))
        return Traduction.optionTimer(str(timer))
    elif args[1] == 'market':
        market = int(args[2])
        if market > 5:
            market = 5
        elif 1 > market:
            market = 1
        configch(str(message.guild.id), 'sizeMarket', int(market))
        return Traduction.optionMarket(str(market))
    return Traduction.optionError()


def configch(serverid, option, params):
    file1 = open("ConfigServer.json", "r")
    file = file1.read()
    file1.close()
    x = json.loads(file)
    try:
        x[str(serverid)][option] = params
    except KeyError:
        setupdate(serverid, option, params)
        return
    y = json.dumps(x)
    file1 = open('ConfigServer.json', "w")
    file1.write(y)
    file1.close()


def getconfig(serverid, option):
    file1 = open("ConfigServer.json", "r")
    file = file1.read()
    file1.close()
    x = json.loads(file)
    try:
        return x[str(serverid)][option]
    except KeyError:
        setupdate(serverid)
        dic = {
            "LANGUAGE": "en",
            "COMMANDBEGIN": "!",
            "TIMER": 0,
            "sizeMarket": 1
        }
        return dic[option]


def issuesend(message, args):
    if len(args) < 3:
        return Traduction.IssueParameter()
    parameter = ' '.join(args[2:])
    command = args[1]
    embed = discord.Embed(title=command, description=parameter, color=0x00ff00)
    embed.set_author(name=str(message.author), icon_url=message.author.avatar_url)
    embed.set_footer(text=str(message.author.id))
    return embed


def setupdate(serverid, option="", value=""):
    file1 = open("ConfigServer.json", "r")
    file = file1.read()
    file1.close()
    x = json.loads(file)
    dic = {
        "LANGUAGE": "en",
        "COMMANDBEGIN": "!",
        "TIMER": 0,
        "sizeMarket": 1
    }
    if option != "" and value != "":
        dic[option] = value
    x[str(serverid)] = dic
    y = json.dumps(x)
    file1 = open('ConfigServer.json', "w")
    file1.write(y)
    file1.close()


def update(message):
    try:
        Settings.language = getconfig(str(message.guild.id), 'LANGUAGE')
    except AttributeError:
        Settings.language = 'en'
        Settings.commandbegin = "!"
        Settings.timer = 0
        Settings.sizeMarket = 1
    else:
        try:
            Settings.language = getconfig(str(message.guild.id), 'LANGUAGE')
        except (KeyError, discord.errors.NotFound):
            Settings.language = 'en'
            configch(message.guild.id, "LANGUAGE", "en")
        try:
            Settings.commandbegin = getconfig(str(message.guild.id), 'COMMANDBEGIN')
        except (KeyError, discord.errors.NotFound):
            Settings.commandbegin = "!"
            configch(message.guild.id, "COMMANDBEGIN", "!")
        else:
            if Settings.commandbegin == "":
                Settings.commandbegin = "!"
        try:
            Settings.timer = getconfig(str(message.guild.id), 'TIMER')
        except (KeyError, discord.errors.NotFound):
            Settings.timer = 0
            configch(message.guild.id, "TIMER", 0)
        try:
            Settings.sizeMarket = getconfig(str(message.guild.id), 'sizeMarket')
        except (KeyError, discord.errors.NotFound):
            Settings.sizeMarket = 1
            configch(message.guild.id, "sizeMarket", 1)


def main():
    client = discord.Client()

    @client.event
    async def on_message(message):
        if message.author != client.user:
            update(message)
        try:
            if message.author == client.user and Settings.timer != 0 and "settings" not in message.content:
                actualtime = time.time()
                while time.time() - actualtime < Settings.timer:
                    pass
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
        except (AttributeError, discord.errors.NotFound):
            pass
        try:
            if message.content.startswith(Settings.commandbegin + 'ducats'):  # DUCATS
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                msg = await message.channel.send(Traduction.Loading(message).format(message))
                async with message.channel.typing():
                    await msg.edit(embed=ducats(client))
            elif message.content.startswith(Settings.commandbegin + 'WTB ') or message.content.startswith(
                    Settings.commandbegin + 'wtb '):
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                async with message.channel.typing():
                    args = message.content.split(" ")
                    orderList = searchPrice(args, "sell", Settings.marketSize)
                    if isinstance(orderList, discord.Embed):  # Y'a erreur
                        await message.channel.send(embed=orderList)
                    else:
                        for order in orderList:
                            embed = discord.Embed(title="WTB " + str(' '.join(args[1:]).lower()),
                                                  description=" ".join(args), color=0x4296ad)
                            embed.set_thumbnail(url=order['image'])
                            embed = Traduction.WTB(order['player'], order['amount'], order['item'],
                                                   str(int(order['platinium'])),
                                                   order['reputation'], embed,
                                                   ("https://warframe.market/items//" + order['item']))
                            await message.channel.send(embed=embed)
            elif message.content.startswith(Settings.commandbegin + 'credits'):  # credits
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                await message.channel.send(Traduction.credit(message).format(message))
            elif message.content.startswith(Settings.commandbegin + 'WTT ') or message.content.startswith(
                    Settings.commandbegin + 'wtt '):
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                async with message.channel.typing():
                    args = message.content.split(" ")
                    orderList = searchPrice(args, "sell", Settings.marketSize)
                    if isinstance(orderList, discord.Embed):  # Y'a erreur
                        await message.channel.send(embed=orderList)
                    else:
                        for order in orderList:
                            embed = discord.Embed(title="WTB " + str(' '.join(args[1:]).lower()),
                                                  description=" ".join(args), color=0x4296ad)
                            embed.set_thumbnail(url=order['image'])
                            embed = Traduction.WTB(order['player'], order['amount'], order['item'],
                                                   str(int(order['platinium'])),
                                                   order['reputation'], embed,
                                                   ("https://warframe.market/items//" + order['item']))
                            await message.channel.send(embed=embed)
                        orderList = searchPrice(args, "buy", Settings.marketSize)
                        for order in orderList:
                            embed = discord.Embed(title="WTS " + str(' '.join(args[1:]).lower()),
                                                  description=" ".join(args), color=0x4296ad)
                            embed.set_thumbnail(url=order['image'])
                            embed = Traduction.WTS(order['player'], order['amount'], order['item'],
                                                   str(int(order['platinium'])),
                                                   order['reputation'], embed,
                                                   ("https://warframe.market/items//" + order['item']))
                            await message.channel.send(embed=embed)
            elif message.content.startswith(Settings.commandbegin + 'WTS ') or message.content.startswith(
                    Settings.commandbegin + 'wts '):
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                async with message.channel.typing():
                    args = message.content.split(" ")
                    orderList = searchPrice(args, "buy", Settings.marketSize)
                    if isinstance(orderList, discord.Embed):  # Y'a erreur
                        await message.channel.send(embed=orderList)
                    else:
                        for order in orderList:
                            embed = discord.Embed(title="WTS " + str(' '.join(args[1:]).lower()),
                                                  description=" ".join(args), color=0x4296ad)
                            embed.set_thumbnail(url=order['image'])
                            embed = Traduction.WTS(order['player'], order['amount'], order['item'],
                                                   str(int(order['platinium'])),
                                                   order['reputation'], embed,
                                                   ("https://warframe.market/items//" + order['item']))
                            await message.channel.send(embed=embed)
            elif message.content.startswith(Settings.commandbegin + 'relic '):  # relic
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                async with message.channel.typing():
                    args = message.content.split(" ")
                    await message.channel.send(embed=relicSearch(args, client))
            elif message.content.startswith(Settings.commandbegin + 'helpW'):
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                args = message.content.split(" ")
                help_info = help(args)
                if help_info[1] == '`':
                    await message.author.send(str(help_info).format(message))
                else:
                    await message.channel.send(str(help_info[0]).format(message))
            elif message.content.startswith(
                    Settings.commandbegin + 'settings') and message.author.guild_permissions.manage_messages:
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                args = message.content.split(" ")
                await message.channel.send(options(args, message).format(message))
            elif message.content.startswith(Settings.commandbegin + 'baro') or message.content.startswith(
                    Settings.commandbegin + 'voidtrader'):
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                args = message.content.split(" ")
                await message.channel.send(embed=baro(args, client))
            elif message.content.startswith(Settings.commandbegin + 'nora') or message.content.startswith(
                    Settings.commandbegin + 'nightwave'):
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                args = message.content.split(" ")
                await message.channel.send(embed=nightwave(args))
            elif message.content.startswith(Settings.commandbegin + 'fissure'):
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                args = message.content.split(" ")
                await message.channel.send(embed=fissures(args, client))
            elif message.content.startswith('!defaultconfig') and message.author.guild_permissions.manage_messages:
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                configch(str(message.guild.id), 'COMMANDBEGIN', '!')
                await message.channel.send('Command begin : !'.format(message))
            elif message.content.startswith(Settings.commandbegin + 'issue '):
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                args = message.content.split(" ")
                try:
                    await client.get_channel(611237128529117292).send(embed=issuesend(message, args))
                except (AttributeError, discord.errors.NotFound):
                    await client.get_channel(611237128529117292).send(issuesend(message, args))
                else:
                    await message.author.send(Traduction.IssueSend().format(message))
            elif message.content.startswith(Settings.commandbegin + 'cetus'):
                args = message.content.split(" ")
                await message.channel.send(embed=cetus(args, client))
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
            elif message.content.startswith(Settings.commandbegin + 'earth'):
                args = message.content.split(" ")
                await message.channel.send(embed=cetus(args, client, 'Earth'))
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
            elif message.content.startswith(Settings.commandbegin + 'vote'):
                embed = discord.Embed(title=client.user.name,
                                      description='If you want to help me have a better view, please go vote on: [[Discord Bots](https://discordbots.org/api/widget/591950764289818634.svg)](https://discordbots.org/bot/591950764289818634/vote)',
                                      color=0x7289DA)  # todo translate
                embed.set_author(name=client.user.name, icon_url=client.user.avatar_url,
                                 url='https://discordbots.org/bot/591950764289818634')
                embed.set_image(url='https://discordbots.org/api/widget/upvotes/591950764289818634.png')
                embed.set_thumbnail(url=client.user.avatar_url)
                await message.channel.send(embed=embed)
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
            elif message.content.startswith(Settings.commandbegin + 'searchrelic ') or message.content.startswith(
                    Settings.commandbegin + 'relicsearch '):
                async with message.channel.typing():
                    args = message.content.split(" ")
                    await message.channel.send(embed=searchRelic(args, client))
                    try:
                        await message.delete()
                    except (AttributeError, discord.errors.NotFound):
                        pass
            elif message.content.startswith(Settings.commandbegin + 'sortie'):
                args = message.content.split(" ")
                await message.channel.send(embed=sortie(args))
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
            elif message.content.startswith(Settings.commandbegin + 'search ') or message.content.startswith(
                    Settings.commandbegin + 'itemdrops '):
                try:
                    await message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                async with message.channel.typing():
                    args = message.content.split(" ")
                    await message.channel.send(embed=search(args, client))
            elif message.content.startswith(Settings.commandbegin + 'invasion'):
                try:
                    await  message.delete()
                except (AttributeError, discord.errors.NotFound):
                    pass
                await message.channel.send(embed=Invasions(client))
          
    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print('------------')

    client.run(token)


main()
