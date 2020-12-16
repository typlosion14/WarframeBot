import discord
import datetime

from CobraLib import source_html
from StorageConfig import Traduction

def ressource(args):
    data_html = source_html("https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html")
    item = list(' '.join(args[1:]).lower())
    item = "".join(item)
    tab = ""
    pos = 0
    zone = data_html[data_html.find("Resource Drops by Resource:"):data_html.find("Sigil Drops by Enemy:")].lower()
    if zone.count(item) != 0:
        tab = '**' + zone[zone.find(item + '</th></tr><tr><th>'):zone.find(
            '</td></tr><tr class="blank-row"><td class="blank-row" colspan="3"></td></tr><tr><th colspan="3">',
            zone.find(item + '</th></tr><tr><th>'))].replace('</th></tr><tr><th>', '**\n__').capitalize().replace(
            '</th><th>', '__\t\t\t__').replace('</th></tr><tr><td>', '__\n```diff\n').replace('</td><td>',
                                                                                              '\t').replace(
            '</td></tr><tr><td>', '\n') + '```'
    zone = data_html[data_html.find("Missions:"):data_html.find("Relics:")].lower()
    if zone.count(item) != 0:
        Mission = '?????????'
        Rotation = '????????????'
        MissionLimit1 = '<td class="blank-row" colspan="2"></td></tr><tr><th colspan="2">'
        MissionLimit2 = '</th></tr>'
        RotationLimit1 = '<tr><th colspan="2">rotation'
        RotationLimit2 = '</th></tr>'
        for i in range(zone.count(item)):  # </td></tr><tr><th colspan="2">Rotation B</th></tr><tr><td>
            pos = zone.find(item,
                            pos + 5)  # </td></tr><tr class="blank-row"><td class="blank-row" colspan="2"></td></tr><tr><th colspan="2">Mars/Gradivus (Caches)</th></tr><tr><th colspan
            if Mission == zone[zone.rfind(MissionLimit1, 0, pos) + len(MissionLimit1):zone.find(MissionLimit2,
                                                                                                zone.rfind(
                                                                                                    MissionLimit1,
                                                                                                    0, pos) + len(
                                                                                                    MissionLimit1))] and Rotation == zone[
                                                                                                                                     zone.rfind(
                                                                                                                                         RotationLimit1,
                                                                                                                                         0,
                                                                                                                                         pos) + len(
                                                                                                                                         '<tr><th colspan="2">'):zone.find(
                                                                                                                                         RotationLimit2,
                                                                                                                                         zone.rfind(
                                                                                                                                             RotationLimit1,
                                                                                                                                             0,
                                                                                                                                             pos) + len(
                                                                                                                                             '<tr><th colspan="2">'))]:
                objet = zone[zone.rfind('<tr><td>', 0, pos) + len("<tr><td>"):pos + len(item)]  # </td></tr><tr><td>
                chance = zone[zone.find('</td><td>', pos) + len("</td><td>"):zone.find('</td>', zone.find('</td><td>',
                                                                                                          pos) + len(
                    "</td><td>"))]  # </td></tr><tr><td>
                tab = tab + objet.capitalize() + '\t' + chance
            else:
                Mission = zone[zone.rfind(MissionLimit1, 0, pos) + len(MissionLimit1):zone.find(MissionLimit2,
                                                                                                zone.rfind(
                                                                                                    MissionLimit1, 0,
                                                                                                    pos) + len(
                                                                                                    MissionLimit1))]
                if Mission == 'urvival)':
                    Mission = 'Mercury/Apollodorus (Survival)'
                Rotation = zone[
                           zone.rfind(RotationLimit1, 0, pos) + len('<tr><th colspan="2">'):zone.find(RotationLimit2,
                                                                                                      zone.rfind(
                                                                                                          RotationLimit1,
                                                                                                          0, pos) + len(
                                                                                                          '<tr><th colspan="2">'))]
                objet = zone[zone.rfind('<tr><td>', 0, pos) + len("<tr><td>"):pos + len(item)]  # </td></tr><tr><td>
                chance = zone[zone.find('</td><td>', pos) + len("</td><td>"):zone.find('</td>', zone.find('</td><td>',
                                                                                                          pos) + len(
                    "</td><td>"))]  # </td></tr><tr><td>
                if "rotation" not in Rotation:
                    Rotation = "???"
                tab = tab + '\n**' + Mission.capitalize() + '**\n**' + Rotation.capitalize().replace(' b',
                                                                                                     ' B').replace(' c',
                                                                                                                   ' C').replace(
                    ' a', ' A') + '**\n' + objet.capitalize() + '\t' + chance
            if len(tab) >= 1750:
                return tab[:1900 ].replace('%)', "%)\n") + '\n```And more...', 'message.author'
    if tab == "" or item == "region resource":
        return Traduction.bug(item), 'msg'
    else:
        return tab.replace('%)', "%)\n"), 'msg'

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


def relicSearch(args, client):
    data_html = source_html("https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html")
    item = list(' '.join(args[1:3]).lower())
    item[0] = item[0].upper()
    item[len(item) - 2] = item[len(item) - 2].upper()
    item = "".join(item)
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
    limit1 = '</td></tr><tr class="blank-row"><td class="blank-row" colspan="2"></td></tr><tr><th colspan="2">'
    tab = data_html[data_html.find(item + " Relic (" + rarete + ")"):data_html.find(limit1, data_html.find(
        item + " Relic (" + rarete + ")"))].replace("</th></tr><tr><td>", "\n**").replace("</td><td>", "** ").replace(
        "</td></tr><tr><td>", "\n**")
    embed = discord.Embed(title=" Relic "+item+' '+rarete, description=datetime.today().strftime("%d/%m/%Y"),
                          color=0x514430)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url,
                     url='https://discordbots.org/bot/591950764289818634')
    embed.set_thumbnail(url=typeofrelic(rarete, item))
    pos = 0
    for i in range(0, tab.count(" (")):
        pos = tab.find('\n', pos) + len('\n')
        Data = tab[tab.find(')', pos) + len(')'):tab.find(')', tab.find(')', pos) + len(')')) + len(')')]
        name = Data[Data.find('**') + len('**'):Data.find('**', Data.find('**') + len('**'))]
        chance = Data[Data.find('** ') + len('** '):]
        if len(name) > 5:
            embed.add_field(name=name, value=chance, inline=True)
    if tab == "":
        embed.add_field(name=Traduction.bug(item), value=Traduction.bug(item))
        return embed
    else:
        return embed

def MobsModsdrops(args):
    data_html = source_html("https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html")
    item = list(' '.join(args[1:]).lower())
    item = "".join(item)
    zone = data_html[data_html.find("Mod Drops by Enemy:"):data_html.find("Mod Drops by Mod:")].lower()
    tab = "**" + zone[zone.find(item + '</th><th colspan="2">'):zone.find(
        '</td></tr><tr class="blank-row"><td class="blank-row" colspan="3"></td></tr><tr><th>',
        zone.find(item + '</th><th colspan="2">'))].replace("</th></tr><tr><td></td><td>", "\n").replace("</td><td>",
                                                                                                         " ").replace(
        "</td></tr><tr><td>", "\n").replace('</th><th colspan="2">', "\n").replace(item, item + "**```fix").replace(
        "\n ", "\n").capitalize() + "```"
    if tab == "**```":
        return Traduction.bug(item)
    else:
        return tab

def ItemDrops(args):
    data_html = source_html("https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html")
    item = list(' '.join(args[1:]).lower())
    item = "".join(item)
    zone = data_html[
           data_html.find("Blueprint/Item Drops by Blueprint/Item:"):data_html.find("Resource Drops by Enemy:")].lower()
    tab = '**' + zone[zone.find(item + '</th></tr><tr><th>'):zone.find(
        '</td></tr><tr class="blank-row"><td class="blank-row" colspan="3"></td></tr><tr><th colspan="3">',
        zone.find(item + '</th></tr><tr><th>'))].replace('</th></tr><tr><th>', '**\n__').capitalize().replace(
        '</th><th>', '__\t\t__').replace('</th></tr><tr><td>', '__\n```diff\n').replace('</td><td>', '\t\t').replace(
        '</td></tr><tr><td>', '\n') + '```'
    if tab == "**```" and "blueprint" not in item:
        args.append("blueprint")
        return ItemDrops(args)
    elif tab == "**```":
        return Traduction.bug(item)
    else:
        return tab

def mods(args):
    item = list(' '.join(args[1:]).lower())
    item = "".join(item)
    tab = ""
    modslist = source_html('https://wf.snekw.com/mods-wiki').lower()
    if modslist.count(item) == 0:
        return Traduction.bug(item)
    data_html = source_html("https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html")
    zone = data_html[data_html.find("Mod Drops by Mod:"):data_html.find("Blueprint/Item Drops by Enemy:")].lower()
    if zone.count(item) >= 1:
        tab = '**' + zone[zone.find(item + '</th></tr><tr><th>'):zone.find(
            '</td></tr><tr class="blank-row"><td class="blank-row" colspan="3"></td></tr><tr><th colspan="3">',
            zone.find(item + '</th></tr><tr><th>'))].replace('</th></tr><tr><th>', '**\n__').capitalize().replace(
            '</th><th>', '__\t\t\t__').replace('</th></tr><tr><td>', '__\n```diff\n').replace('</td><td>',
                                                                                              '\t').replace(
            '</td></tr><tr><td>', '\n') + '```\n'
    data_html = source_html("https://drops.warframestat.us/data/all.json").lower()
    if data_html.count(item) >= 1:
        tab = tab + '**' + item.capitalize() + '**\n'
        posData = 0
        for i in range(0, data_html.count(item)):
            posData = data_html.find(item, posData + len(item))
            Objectivename = data_html[
                            data_html.rfind('"objectivename":"', 0, posData) + len('"objectivename":"'):data_html.find(
                                '"', data_html.rfind('"objectivename":"', 0, posData) + len('"objectivename":"'))]
            if Objectivename == 'ds':
                zoneb = data_html[data_html.rfind("}]", 0, posData):data_html.rfind(":[{", 0, posData)]
                MissionName = zoneb[zoneb.find('"') + 1:zoneb.find('"', zoneb.find('"') + 2)]
                gamemode = zoneb[zoneb.find('{"gamemode":"') + len('{"gamemode":"'):zoneb.find('"', zoneb.find(
                    '{"gamemode":"') + len('{"gamemode":" '))]
                if MissionName == 'c' or MissionName == 'b' or MissionName == 'a':
                    MissionName2=data_html[data_html.rfind('"',0,data_html.rfind('":{"ga',0,posData))+1:data_html.rfind('":{"ga',0,posData)].capitalize()
                    gamemode=data_html[data_html.rfind('"gamemode":"',0,posData)+len('"gamemode":"'):data_html.find('"',data_html.rfind('"gamemode":"',0,posData)+len('"gamemode":"'))].capitalize()
                    MissionName = 'Rotation ' + MissionName
                    MissionName=MissionName2.capitalize()+'\n'+MissionName
                Objectivename = '\n**' + MissionName + '** : ' + gamemode.capitalize()
            chancedrop = data_html[data_html.find('"chance":', posData) + len('"chance":'):data_html.find('}',
                                                                                                          data_html.find(
                                                                                                              '"chance":',
                                                                                                              posData) + len(
                                                                                                              '"chance":'))]
            tab = tab + Traduction.FindHere() + Objectivename + '\nDrop Chance: ' + chancedrop + '\n'
            if len(tab) >= 1750:
                return tab[:1900 ].replace('%)', "%)\n") + '\nAnd more...', 'message.author'
    if not tab == "":
        return tab,"msg"
    else:
        return Traduction.bug(item),"msg"