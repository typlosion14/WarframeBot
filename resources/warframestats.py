import discord
import json
from datetime import *

from CobraLib import importjson
from StorageConfig import Traduction, ConvertPart


def baro(args, client):
    platform = '_'.join(args[1:]).lower()
    if platform == 'switch' or platform == 'nintendo':
        platform = 'swi'
    if platform == 'xbox':
        platform = "xb1"
    if platform == '':
        platform = 'pc'
    if platform not in ("pc", "ps4", "xb1", "swi"):
        return discord.Embed(title="Baro Ki'Teer", description=Traduction.platformfail(platform), color=0xFF0000)
    else:
        dicbaro = json.loads(importjson('https://api.warframestat.us/' + platform + '/voidTrader'))
    embed = discord.Embed(title="Baro Ki'Teer " + str(' '.join(args[1:]).lower()),
                          description=" ".join(args), color=0x29DDB1)
    embed.set_thumbnail(
        url='http://content.warframe.com/MobileExport/Lotus/Interface/Icons/Player/BaroKiteerAvatar.png')
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url,
                     url='https://discordbots.org/bot/591950764289818634')
    embed.add_field(name='Location', value=dicbaro['location'])
    if bool(dicbaro['active']):
        return Traduction.baro_depart(dicbaro, embed)
    else:
        return Traduction.baro_arrive(dicbaro, embed)


def nightwave(args):
    platform = '_'.join(args[1:]).lower()
    if platform == 'switch' or platform == 'nintendo':
        platform = 'swi'
    elif platform == 'xbox':
        platform = "xb1"
    elif platform == '':
        platform = 'pc'
    elif platform not in ("pc", "ps4", "xb1", "swi"):
        return Traduction.platformfail(platform)
    nightdic = json.loads(importjson("https://api.warframestat.us/" + platform + "/nightwave"))
    embed = discord.Embed(title="Nightwave", description=" ".join(args), color=0x8D32A8)
    if bool(nightdic['active']):
        return Traduction.Nightwave(nightdic, embed)
    else:
        embed = discord.Embed(title="Nightwave", description='Nora don\'t have any mission for you.', color=0xFF0000)
        embed.set_thumbnail(
            url='https://vignette.wikia.nocookie.net/warframe/images/9/95/Nora_Night_transmission.png/revision/latest?cb=20190301081607')
        embed.set_author(name="Nora",
                         icon_url="https://vignette.wikia.nocookie.net/warframe/images/9/95/Nora_Night_transmission.png/revision/latest?cb=20190301081607")
        return embed


def fissures(args, client):
    try:
        platform = args[1]
    except IndexError:
        platform = ""
    try:
        relicTier = args[2].capitalize()
    except IndexError:
        relicTier = ""
    if platform == 'switch' or platform == 'nintendo':
        platform = 'swi'
    elif platform == 'xbox':
        platform = "xb1"
    elif platform == '':
        platform = 'pc'
    elif platform not in ("pc", "ps4", "xb1", "swi"):
        return discord.Embed(title='Fissure', description=Traduction.platformfail(platform), color=0xFF0000)

    data = json.loads(importjson("https://api.warframestat.us/" + platform + "/fissures"))
    embed = discord.Embed(title="Fissure", description=" ".join(args), color=0xDCF3FF)
    embed.set_thumbnail(
        url='https://vignette.wikia.nocookie.net/warframe/images/9/9c/LuminousIconLarge.png/revision/latest?cb=20160717170505&path-prefix=fr')
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url,
                     url='https://discordbots.org/bot/591950764289818634')
    for place in data:
        embed = Traduction.fissure(place, embed, relicTier)
        if len(embed.fields) >= 24:
            embed.set_footer(text=Traduction.MoreIG())
            return embed
    return embed


def cetus(args, client, world='Cetus'):
    platform = '_'.join(args[1:]).lower()
    if platform == 'switch' or platform == 'nintendo':
        platform = 'swi'
    elif platform == 'xbox':
        platform = "xb1"
    elif platform == '':
        platform = 'pc'
    elif platform not in ("pc", "ps4", "xb1", "swi"):
        return discord.Embed(title=world, description=Traduction.platformfail(platform), color=0xFF0000)
    if world == 'Cetus':
        data = json.loads(importjson('https://api.warframestat.us/' + platform + '/cetusCycle'))
        isDay = data['state']
        timeLeft = data['timeLeft']
        embed = discord.Embed(title="Cetus", description=" ".join(args), color=0xD8A24A)
        embed.set_thumbnail(
            url='https://vignette.wikia.nocookie.net/warframe/images/3/32/OstronSyndicateFlag.png/revision/latest?cb=20171021133528&path-prefix=fr')
        embed.set_author(name=client.user.name, icon_url=client.user.avatar_url,
                         url='https://discordbots.org/bot/591950764289818634')
        embed.add_field(name=Traduction.Day(isDay), value=Traduction.timeleft() + timeLeft)
        return embed
    if world == 'Earth':
        data = json.loads(importjson('https://api.warframestat.us/' + platform + '/earthCycle'))
        isDay = data['state']
        timeLeft = data['timeLeft']
        embed = discord.Embed(title="Earth", description=" ".join(args), color=0x3565A9)
        embed.set_thumbnail(
            url='https://vignette.wikia.nocookie.net/warframe/images/1/1e/Earth.png/revision/latest/scale-to-width-down/350?cb=20161016212227')
        embed.set_author(name=client.user.name, icon_url=client.user.avatar_url,
                         url='https://discordbots.org/bot/591950764289818634')
        embed.add_field(name=Traduction.Day(isDay), value=Traduction.timeleft() + timeLeft)
        return embed


def sortie(args):
    platform = '_'.join(args[1:]).lower()
    if platform == 'switch' or platform == 'nintendo':
        platform = 'swi'
    elif platform == 'xbox':
        platform = "xb1"
    elif platform == '':
        platform = 'pc'
    elif platform not in ("pc", "ps4", "xb1", "swi"):
        return discord.Embed(title='Sortie', description=Traduction.platformfail(platform), color=0xFF0000)
    embed = discord.Embed(title="Sortie", description=" ".join(args), color=0xFFD700)
    embed.set_thumbnail(
        url='https://vignette.wikia.nocookie.net/warframe/images/1/15/Sortie_b.png/revision/latest?cb=20151217134250')
    data = json.loads(importjson('https://api.warframestat.us/' + platform + '/sortie'))
    missionList = data['variants']
    for i in range(len(missionList)):
        dictemp = missionList[i]
        missionType = dictemp['missionType']
        modifiername = dictemp['modifier']
        modifierdesc = dictemp['modifierDescription'].replace('. ', '.\n')
        node = dictemp['node']
        embed.add_field(name="Mission " + str(i + 1), value=node + ' ' + missionType)
        embed.add_field(name=modifiername, value=modifierdesc)
    return embed


def typeofrelic(rarete, item):
    if "axi" in item.lower():
        if rarete == "Intact":
            return 'https://vignette.wikia.nocookie.net/warframe/images/0/0e/VoidProjectionsGoldD.png/revision/latest?cb=20160711164509&path-prefix=fr'
        if rarete == "Exceptional":
            return 'https://vignette.wikia.nocookie.net/warframe/images/3/3c/VoidProjectionsIronA.png/revision/latest?cb=20160903181326&path-prefix=fr'
        if rarete == "Flawless":
            return 'https://vignette.wikia.nocookie.net/warframe/images/4/4e/VoidProjectionsIronB.png/revision/latest?cb=20160903181334&path-prefix=fr'
        if rarete == "Radiant":
            return 'https://vignette.wikia.nocookie.net/warframe/images/1/1a/VoidProjectionsIronC.png/revision/latest?cb=20160903181342&path-prefix=fr'
        else:
            return 'https://vignette.wikia.nocookie.net/warframe/images/0/0e/VoidProjectionsGoldD.png/revision/latest?cb=20160711164509&path-prefix=fr'
    if "meso" in item.lower():
        return 'https://vignette.wikia.nocookie.net/warframe/images/1/12/VoidProjectionsBronzeD.png/revision/latest/scale-to-width-down/199?cb=20160711164431&path-prefix=fr'
    if "neo" in item.lower():
        return 'https://vignette.wikia.nocookie.net/warframe/images/c/c5/VoidProjectionsSilverD.png/revision/latest/scale-to-width-down/199?cb=20160711164523&path-prefix=fr'
    else:
        return 'https://vignette.wikia.nocookie.net/warframe/images/a/ae/VoidProjectionsIronD.png/revision/latest/scale-to-width-down/199?cb=20160711164451&path-prefix=fr'


def relicSearch(args, client):  # !relic
    # Content : https://drops.warframestat.us/data/relics/Meso/R1.json
    try:
        relicTier = args[1].capitalize()
        relicName = args[2].capitalize()
    except IndexError:
        return
    try:
        if args[3] == "1":
            rarete = "Exceptional"
        elif args[3] == "2":
            rarete = "Flawless"
        elif args[3] == "3":
            rarete = "Radiant"
        else:
            rarete = "Intact"
    except:
        rarete = "Intact"
    embed = discord.Embed(title=" Relic " + relicTier + ' ' + relicName, description=rarete,
                          color=0x514430)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url,
                     url='https://discordbots.org/bot/591950764289818634')
    embed.set_thumbnail(url=typeofrelic(rarete, relicTier))
    try:
        jsonall = json.loads(
            importjson("https://drops.warframestat.us/data/relics/" + relicTier + "/" + relicName + ".json"))
    except json.decoder.JSONDecodeError:
        embed.add_field(name=Traduction.bug(relicTier + " " + relicName),
                        value=Traduction.bug(relicTier + " " + relicName))
        return embed

    itemList = sorted(jsonall['rewards'][rarete], key=lambda k: k['chance'], reverse=True)
    for item in itemList:
        name = item['itemName']
        chance = item['chance']
        embed.add_field(name="Drop rate: " + str(chance) + "%", value=name, inline=True)
    return embed


def searchRelic(args, client):  # relicsearch/searchrelic
    # Where to get : https://api.warframestat.us/drops/search/MeSo r1
    try:
        relic = args[1] + " " + args[2]
    except IndexError:
        embed = discord.Embed(title=" Relic " + args[1], description=" ".join(args),
                              color=0x514430)
        embed.set_author(name=client.user.name, icon_url=client.user.avatar_url,
                         url='https://discordbots.org/bot/591950764289818634')
        embed.set_thumbnail(url=typeofrelic(None, args[1]))
        embed.add_field(name=Traduction.bug(args[1]),
                        value=Traduction.bug(args[1]))##TODO Show !helpW relicSearch
        return embed

    embed = discord.Embed(title=" Relic " + relic, description=" ".join(args),
                          color=0x514430)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url,
                     url='https://discordbots.org/bot/591950764289818634')
    embed.set_thumbnail(url=typeofrelic(None, relic))
    try:
        jsonall = json.loads(
            importjson("https://api.warframestat.us/drops/search/" + relic))
    except json.decoder.JSONDecodeError:
        embed.add_field(name=Traduction.bug(relic),
                        value=Traduction.bug(relic))
        return embed

    jsonSorted = sorted(jsonall, key=lambda k: k['chance'], reverse=True)
    for item in jsonSorted:
        place = item['place']
        chance = item['chance']
        if "Relic" not in place:
            embed.add_field(name="Drop rate: " + str(chance) + "%", value=place, inline=True)
    if len(embed.fields) == 0:
        embed.add_field(name="Relic is vaulted", value="Relic is vaulted, so you can only buy it.")
    return embed


def getimage(item):
    try:
        imageNameJs = json.loads(importjson("https://api.warframestat.us/items/search/" + item))
    except json.decoder.JSONDecodeError:
        return ''
    try:
        imageName = imageNameJs[0]['imageName']
    except IndexError:
        return ''
    return "https://raw.githubusercontent.com/wfcd/warframe-items/development/data/img/" + imageName


def cleanItem(args):
    r = ""
    for arg in args:
        r += ConvertPart(arg) + " "
    return r.replace("blueprint", "BP").replace("prime", "P.")[:-1].capitalize()


def search(args, client):
    itemS = cleanItem(args[1:])
    embed = discord.Embed(title=itemS, description=" ".join(args),
                          color=0x514430)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url,
                     url='https://discordbots.org/bot/591950764289818634')
    embed.set_thumbnail(url=getimage(itemS.lower()))
    try:
        jsonall = json.loads(
            importjson("https://api.warframestat.us/drops/search/" + itemS))
    except json.decoder.JSONDecodeError:
        embed.add_field(name=Traduction.bug(itemS),
                        value=Traduction.bug(itemS))
        return embed

    jsonSorted = sorted(jsonall, key=lambda k: k['chance'], reverse=True)
    for item in jsonSorted:
        place = item['place']
        chance = item['chance']
        if itemS.lower() in item['item'].lower():
            embed.add_field(name="Drop rate: " + str(chance) + "%", value=place, inline=True)
    return embed


def Invasions(client):
    embed = discord.Embed(title="Invasion", description="!invasion", color=0x514430)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url,
                     url='https://discordbots.org/bot/591950764289818634')
    embed.set_thumbnail(
        url="https://vignette.wikia.nocookie.net/warframe/images/2/26/InvasionSplash.png/revision/latest?cb=20140421123118")
    jsonall = json.loads(importjson("https://api.warframestat.us/pc/invasions"))
    for invas in jsonall:
        if "-" not in invas['eta']:
            value = invas['attackerReward']['asString'] + ' vs ' + invas['defenderReward']['asString'] if \
                invas['attackerReward']['asString'] != "" else invas['defenderReward']['asString']
            embed.add_field(name=invas['defendingFaction'] + ' vs ' + invas['attackingFaction'], value=value)
            embed.add_field(name="Time before end", value=invas['eta'])
    return embed
