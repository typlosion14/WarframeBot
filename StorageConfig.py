from CobraLib import StringToDate


class Settings:
    language = "en"
    commandbegin = "!"
    moderatorRole = []
    timer = 0
    marketSize = 1


class Traduction:
    def ducats(item, ducatsitem, ducatsparplatinium, embed):
        embed.set_author(name='warframe.market',
                         icon_url='https://warframe.market/static/assets/frontend/logo_icon_only.png')
        embed.set_thumbnail(
            url='https://vignette.wikia.nocookie.net/warframe/images/8/86/Ducats.png/revision/latest/scale-to-width-down/250?cb=20170518152555&path-prefix=ja')
        embed.set_footer(text=Settings.commandbegin + 'wtb ' + item)
        if Settings.language == "fr":
            embed.add_field(name='Objet', value=item, inline=True)
            embed.add_field(name='Ducats', value=ducatsitem, inline=True)
            embed.add_field(name='Ducats/Platinum', value=ducatsparplatinium, inline=True)
            return embed
        elif Settings.language == "pt":
            embed.add_field(name='Recurso', value=item, inline=True)
            embed.add_field(name='Ducats', value=ducatsitem, inline=True)
            embed.add_field(name='Ducats/Platinum', value=ducatsparplatinium, inline=True)
            return embed
        else:
            embed.add_field(name='Item', value=item, inline=True)
            embed.add_field(name='Ducats', value=ducatsitem, inline=True)
            embed.add_field(name='Ducats/Platinum', value=ducatsparplatinium, inline=True)
            return embed

    def optioncommandbegin(newbegin):
        if Settings.language == "fr":
            return "Les commandes commenceront par " + newbegin + " Ã  partir de maintenant."
        elif Settings.language == "pt":
            return 'Os comandos comeÃ§am agora com ' + newbegin
        else:
            return "Commands start now with " + newbegin

    def bug(self=''):
        if Settings.language == "fr":
            return "Objet Introuvable."
        elif Settings.language == "pt":
            return "O objeto nÃ£o foi encontrado."
        else:
            return "Item not found."

    def Loading(self=''):
        if Settings.language == "fr":
            return "Chargement des donnÃ©es..."
        elif Settings.language == "pt":
            return "Carregando..."
        else:
            return "Loading..."

    def WTB(player, amount, item, plat0, reputation, embed, url):
        amount = str(amount)
        plat0 = str(plat0)
        reputation = str(reputation)
        embed.set_author(name='warframe.market',
                         icon_url='https://warframe.market/static/assets/frontend/logo_icon_only.png', url=url)
        embed.set_footer(
            text='/w ' + player + ' Hi! I want to buy: ' + item + ' for ' + plat0 + ' platinum. (warframe.market)')
        if Settings.language == "pt":
            embed.add_field(name='Jogador', value=player, inline=True)
            embed.add_field(name='Quantidade X PreÃ§o', value=amount + ' X ' + plat0, inline=True)
            embed.add_field(name='ReputaÃ§Ã£o', value=reputation, inline=True)
            return embed  # "Le joueur **" + player + "** vend " + amount + " " + item.replace("_"," ").capitalize() + " Ã  **" + str(plat0) + "** platinium, il a " + reputation + " de reputation."
        elif Settings.language == "fr":
            embed.add_field(name='Joueur', value=player, inline=True)
            embed.add_field(name='Nombre X Prix', value=amount + ' X ' + plat0, inline=True)
            embed.add_field(name='RÃ©putation', value=reputation, inline=True)
            return embed
        else:
            embed.add_field(name='Player', value=player, inline=True)
            embed.add_field(name='Amount X Price', value=amount + ' X ' + plat0, inline=True)
            embed.add_field(name='Reputation', value=reputation, inline=True)
            return embed

    def WTS(player, amount, item, plat0, reputation, embed, url):
        amount = str(amount)
        plat0 = str(plat0)
        reputation = str(reputation)
        embed.set_footer(
            text='/w ' + player + ' Hi! I want to sell: ' + item + ' for ' + plat0 + ' platinum. (warframe.market)')
        embed.set_author(name='warframe.market',
                         icon_url='https://warframe.market/static/assets/frontend/logo_icon_only.png', url=url)
        if Settings.language == "fr":
            embed.add_field(name='Joueur', value=player, inline=True)
            embed.add_field(name='Nombre X Prix', value=amount + ' X ' + plat0, inline=True)
            embed.add_field(name='RÃ©putation', value=reputation, inline=True)
            return embed
        elif Settings.language == "pt":
            embed.add_field(name='Jogador', value=player, inline=True)
            embed.add_field(name='Quantidade X PreÃ§o', value=amount + ' X ' + plat0, inline=True)
            embed.add_field(name='ReputaÃ§Ã£o', value=reputation, inline=True)
            return embed
        else:
            embed.add_field(name='Player', value=player, inline=True)
            embed.add_field(name='Amount X Price', value=amount + ' X ' + str(plat0), inline=True)
            embed.add_field(name='Reputation', value=reputation, inline=True)
            return embed

    def platformfail(self=''):
        if Settings.language == "fr":
            return "Erreur de platforme veuillez rentrez : `pc,xb1,swi,ps4`"
        elif Settings.language == "pt":
            return "Erro de plataforma, introduza:`pc,xb1,swi,ps4`"
        else:
            return "Error platform, input: `pc,xb1,swi,ps4`"

    def baro_arrive(dicbaro, embed):
        if Settings.language == "fr":
            time = str(dicbaro['startString']).replace("d", " jour(s)")
            embed.add_field(name="Baro Ki'Teer arrivera dans", value=time)
            return embed
        elif Settings.language == "pt":
            time = str(dicbaro['startString']).replace("d", " dia(s)")
            embed.add_field(name="O Baro Ki'Teer chegarÃ¡ em", value=time)
            return embed
        else:
            time = str(dicbaro['startString']).replace("d", " day(s)")
            embed.add_field(name="Baro Ki'Teer will come in", value=time)
            return embed

    def baro_depart(dicbaro, embed):
        # http://content.warframe.com/MobileExport/Lotus/Interface/Icons/Player/BaroKiteerAvatar.png
        pos = 0
        inventory = dicbaro['inventory']
        for i in range(len(inventory)):
            nameitem = inventory[i]['item']
            price = 'Ducats: ' + str(inventory[i]['ducats']) + '\nCredits: ' + str(inventory[i]['credits'])
            embed.add_field(name=nameitem, value=price)
        if Settings.language == "fr":
            time = str(dicbaro['endString']).replace("d", " jour(s)")
            embed.set_footer(text="Baro Ki'Teer partira dans " + time)
            return embed
        elif Settings.language == "pt":
            time = str(dicbaro['endString']).replace("d", " dia(s)")
            embed.set_footer(text="O Baro Ki'Teer partirÃ¡ em " + time)
            return embed
        else:
            time = str(dicbaro['endString']).replace("d", " day(s)")
            embed.set_footer(text="Baro Ki'Teer will leave in " + time)
            return embed

    def Nightwave(nightdic, embed):
        Challenges = nightdic['activeChallenges']
        Date = StringToDate(nightdic['expiry'])
        Fin = Date[2] + "/" + Date[1] + "/" + Date[0]
        embed.set_thumbnail(
            url='https://vignette.wikia.nocookie.net/warframe/images/9/95/Nora_Night_transmission.png/revision/latest?cb=20190301081607')
        embed.set_author(name="Nora",
                         icon_url="https://vignette.wikia.nocookie.net/warframe/images/9/95/Nora_Night_transmission.png/revision/latest?cb=20190301081607")
        if Settings.language == "fr":
            embed.set_footer(text='Les ondes nocturnes finissent le: ' + Fin)
            for i in range(len(Challenges)):  # reputation,isElite,isDaily,desc,expiry,title
                dictemp = Challenges[i]
                Date = StringToDate(dictemp['expiry'])
                expiry = Date[2] + "/" + Date[1] + "/" + Date[0]
                if len(dictemp['desc']) > 18:
                    postemp = dictemp['desc'].find(' ', 16)
                    dictemp['desc'] = dictemp['desc'][:postemp] + '\n' + dictemp['desc'][postemp + 1:]
                embed.add_field(name="Mission " + dictemp['title'], value=dictemp['desc'], inline=True)
                embed.add_field(name="Reputation: " + str(dictemp['reputation']), value="Fini le " + expiry,
                                inline=True)
            return embed
        elif Settings.language == "pt":
            embed.set_footer(text='A Nightwave termina em: ' + Fin)
            for i in range(len(Challenges)):  # reputation,isElite,isDaily,desc,expiry,title
                dictemp = Challenges[i]
                Date = StringToDate(dictemp['expiry'])
                expiry = Date[2] + "/" + Date[1] + "/" + Date[0]
                if len(dictemp['desc']) > 18:
                    postemp = dictemp['desc'].find(' ', 16)
                    dictemp['desc'] = dictemp['desc'][:postemp] + '\n' + dictemp['desc'][postemp + 1:]
                embed.add_field(name="MissÃ£o " + dictemp['title'], value=dictemp['desc'], inline=True)
                embed.add_field(name="ReputaÃ§Ã£o: " + str(dictemp['reputation']), value="Tempo restante: " + expiry,
                                inline=True)
            return embed
        else:
            embed.set_footer(text='Nightwaves end at: ' + Fin)
            for i in range(len(Challenges)):  # reputation,isElite,isDaily,desc,expiry,title
                if i + 1 == 7:
                    return embed
                dictemp = Challenges[i]
                Date = StringToDate(dictemp['expiry'])
                expiry = Date[2] + "/" + Date[1] + "/" + Date[0]
                if len(dictemp['desc']) > 18:
                    postemp = dictemp['desc'].find(' ', 16)
                    dictemp['desc'] = dictemp['desc'][:postemp] + '\n' + dictemp['desc'][postemp + 1:]
                embed.add_field(name="Mission " + dictemp['title'], value=dictemp['desc'], inline=True)
                embed.add_field(name="Reputation: " + str(dictemp['reputation']), value="Time Left: " + str(expiry),
                                inline=True)
            return embed

    def credit(self=''):
        if Settings.language == "fr":
            return "Ce bot n'est pas liÃ© Ã  Digital Extreme.\n" \
                   "Il a Ã©tÃ© crÃ©Ã© par Typlosion#7189 https://patreon.com/Typlosion \n" \
                   "Les donnÃ©es sont recuperes depuis:\n" \
                   "https://warframe.market/ \n" \
                   "https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html \n" \
                   "https://api.warframestat.us/ \n" \
                   "https://wf.snekw.com/\n" \
                   "Discord.py crÃ©e par Rapptz"
        elif Settings.language == "pt":
            return "Este bot nÃ£o Ã© de qualquer maneira afiliado com a Digital Extremes.\nFoi criado pelo Typlosion#7189 https://patreon.com/Typlosion.\nPara mais informaÃ§Ãµes:\n" \
                   "https://warframe.market/ \n" \
                   "https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html \n" \
                   "https://api.warframestat.us/ \n" \
                   "https://wf.snekw.com/\n" \
                   "Traduzido por Morim e DaemonFloors\n" \
                   "Discord.py criado por Rapptz"
        else:
            return "This bot is not affiliated with Digital Extreme.\n" \
                   "It has been created by Typlosion#7189 https://patreon.com/Typlosion \n" \
                   "Obtain informations from:\n" \
                   "https://warframe.market/ \n" \
                   "https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html \n" \
                   "https://api.warframestat.us/ \n" \
                   "https://wf.snekw.com/\n" \
                   "Discord.py create by Rapptz"

    def fissure(dicfissure, embed, TierCible):
        time = dicfissure['eta']
        tier = dicfissure['tier']
        missionType = dicfissure['missionType']
        mission = dicfissure['node']
        if TierCible == tier or TierCible == "":
            embed.add_field(name='Tier', value=tier, inline=True)
            if Settings.language == "fr":
                embed.add_field(name='Type de Mission:', value=missionType, inline=True)
                embed.add_field(name='Mission:', value=mission, inline=True)
                embed.add_field(name='Temps restant:', value=time, inline=False)
            elif Settings.language == "pt":
                embed.add_field(name='Tipo da MissÃ£o:', value=missionType, inline=True)
                embed.add_field(name='MissÃ£o:', value=mission, inline=True)
                embed.add_field(name='Tempo restante:', value=time, inline=False)
            else:
                embed.add_field(name='Mission type:', value=missionType, inline=True)
                embed.add_field(name='Mission:', value=mission, inline=True)
                embed.add_field(name='Time left:', value=time, inline=False)
        return embed

    def IssueParameter(self=''):
        if Settings.language == "fr":
            return 'Exemple: !issue !resource Ne trouve pas Lephantis Nav'
        elif Settings.language == "pt":
            return 'Exemplo: !issue !resource nÃ£o foi encontrado Lephantis Nav'
        else:
            return "Example: !issue !resource Don't find Lephantis Nav"

    def IssueSend(self=''):
        if Settings.language == "fr":
            return 'ProblÃ¨me envoyÃ© au serveur Discord!'
        elif Settings.language == "pt":
            return 'Problema enviado!'
        else:
            return 'Issue send!'

    def Day(self):
        if Settings.language == "fr":
            if self == 'Day':
                return 'Actuellement: Jour'

            else:
                return 'Actuellement: Nuit'
        elif Settings.language == "pt":
            if self == 'Day':
                return 'Agora: Dia'
            else:
                return 'Agora: Noite'
        else:
            return 'Now: ' + self

    def timeleft(self=''):
        if Settings.language == "fr":
            return 'Temps restant: '
        elif Settings.language == "pt":
            return 'Tempo restante:'
        else:
            return 'Time Left: '

    def MoreIG(self=''):
        if Settings.language == "fr":
            return 'Aller voir en jeu pour les autres...'
        elif Settings.language == 'pt':
            return 'Verificar no jogo para outros...'
        else:
            return 'Go check ingame for the other...'

    def FindHere(self=''):
        if Settings.language == "fr":
            return 'A trouver ici: '
        elif Settings.language == 'pt':
            return 'Encontrar aqui: '
        else:
            return 'Find here: '

    def notiferror(self=''):
        if Settings.language == 'fr':
            return 'Vous devez Ã©crire !notif on ou !notif off'
        elif Settings.language == 'pt':
            return 'Deve escrever !notif on ou !notif off'
        else:
            return 'You must write !notif on or !notif off'

    def NotifOn(self=''):
        if Settings.language == 'fr':
            return 'Vous serez notifier quand un nouveau patch note sortira.'
        elif Settings.language == 'pt':
            return 'SerÃ¡ notificado quando as Patch Notes forem lanÃ§adas.'
        else:
            return 'You will be notified when Patch notes will be release.'

    def NotifOff(self=''):
        if Settings.language == 'fr':
            return 'Vous ne serez plus notifier quand un nouveau patch note sortira.'
        elif Settings.language == 'pt':
            return 'NÃ£o serÃ¡ notificado quando as Patch Notes forem lanÃ§adas.'
        else:
            return 'You will no longer be notified when Patch notes will be release.'

    def optionTimer(self: str):
        if self != "0":
            if Settings.language == 'fr':
                return 'Le bot va maintenant autodelete ces messages aprÃ¨s:' + self + ' secondes.'
            elif Settings.language == 'pt':
                return 'O bot agora autodeteta essas mensagens apÃ³s' + self + ' segundos.'
            else:
                return 'Bot will autodelete his messages after ' + self + ' seconds.'
        else:
            if Settings.language == 'fr':
                return 'Le bot ne va plus autodelete ces messages.'
            elif Settings.language == 'pt':
                return 'O bot nÃ£o irÃ¡ mais autodetectar essas mensagens.'
            else:
                return 'Bot stop autodelete his messages'

    def optionError(self=''):
        if Settings.language == 'fr':
            return '```diff\nExample:\n+ ' + Settings.commandbegin + 'settings commandbegin "!"\n+ ' + Settings.commandbegin + 'settings language "en"\n+ ' + Settings.commandbegin + 'settings timer 5\n+ ' + Settings.commandbegin + 'settings market 2```'
        elif Settings.language == 'pt':
            return '```diff\nExemplo:\n+ ' + Settings.commandbegin + 'settings commandbegin "!"\n+ ' + Settings.commandbegin + 'settings language "en"\n+ ' + Settings.commandbegin + 'settings timer 5\n+ ' + Settings.commandbegin + 'settings market 2```'
        else:
            return '```diff\nExemple:\n+ ' + Settings.commandbegin + 'settings commandbegin "!"\n+ ' + Settings.commandbegin + 'settings language "en"\n+ ' + Settings.commandbegin + 'settings timer 5\n+ ' + Settings.commandbegin + 'settings market 2```'

    def optionMarket(self: str):
        if Settings.language == "fr":
            return 'Le bot affichera '+self+' offres.'
        elif Settings.language == 'pt':
            return 'O bot irÃ¡ exibir '+self+' ofertas'
        else:
            return 'The bot will display '+self+' offers.'


def ConvertPart(part):
    part = part.lower()
    if part == 'diagrama' or part == "schema":
        return "blueprint"
    elif part == 'canon' or part == "cano":
        return "barrel"
    elif part == "culasse" or part == "receptor":
        return "receiver"
    elif part == "crosse" or part == "coronha":
        return "stock"
    elif part == "poignÃ©e" or part == "poignee" or part == "empunhadora":
        return "grip"
    elif part == "partie infÃ©rieure" or part == "membro inferior" or part == "part inf":
        return "lower limb"
    elif part == "corde" or part == "corda":
        return "string"
    elif part == "partie supÃ©rieure" or part == "membro superior" or part == "part sup":
        return "upper limb"
    elif part == "garde":
        return "hilt"
    elif part == "lame":
        return "blade"
    elif part == "botte":
        return "boot"
    elif part == "gantelet":
        return "gauntlet"
    elif part == "ornement":
        return "ornament"
    elif part == "manche":
        return "handle"
    elif part == "systÃ¨mes" or part == "systemes":
        return "systems"
    elif part == "neuroptique" or part == "neuro":
        return "neuroptics"
    elif part == "chÃ¢ssis":
        return "chassis"
    else:
        return part


def help(args):
    msg = ''
    try:
        commandname = ''.join(args[1]).lower()

    except:
        commandname = ''
    if commandname == 'WTB' or commandname == 'wtb':
        if Settings.language == "en":
            msg = "Show the best price for buy item.\nExample: !wtb rubico prime barrel"
        elif Settings.language == 'pt':
            msg = "Mostrar o melhor preÃ§o para comprar um item.\nExemplo: !wtb rubico prime Cano"
        else:
            msg = "Montre le meilleur prix pour acheter un objet.\nExemple: !wtb rubico prime barrel"
    elif commandname == 'WTS' or commandname == 'wts':
        if Settings.language == "en":
            msg = 'Show the best price for sell item.\nExample: !wts rubico prime barrel'
        elif Settings.language == "pt":
            msg = 'Mostrar o melhor preÃ§o para vender um item.\nExemplo: !wts rubico prime Cano'
        else:
            msg = "Montre le meilleur prix pour vendre un objet.\nExemple: !wts rubico prime barrel"
    elif commandname == 'WTT' or commandname == 'wtt':
        if Settings.language == "en":
            msg = 'Show the best price for sell and buy item.\nExample: !wtt rubico prime barrel'
        elif Settings.language == "pt":
            msg = 'Mostrar o melhor preÃ§o para vender e comprar um item.\nExemplo: !wtt rubico prime Cano'
        else:
            msg = "Montre le meilleur prix pour vendre et acheter un objet.\nExemple: !wtt rubico prime barrel"
    elif commandname == 'relic':
        if Settings.language == "en":
            msg = 'Show the drop loot table of the relic.\nExample: !relic axi s3\nExample: !relic lith b4 3'
        elif Settings.language == "pt":
            msg = 'Mostrar a tabela de chance de recursos da reliquia.\nExemplo: !relic axi s3\nExample: !relic lith b4 3'
        else:
            msg = "Montre la table de loot de la relique.\nExample: !relic axi s3\nExample: !relic lith b4 3"
    elif commandname == 'mobmodsdrops':
        if Settings.language == "en":
            msg = 'Show what mods drop the mob\nExample: !mobmodsdrops kubrow'
        elif Settings.language == "pt":
            msg = 'Mostrar que mods o inimigo droppa.\nExemplo: !mobmodsdrops kubrow'
        else:
            msg = 'Montre quels mods drop le mob\nExemple: !mobmodsdrops kubrow'
    elif commandname == 'mods':
        if Settings.language == "en":
            msg = 'Show where the mod is dropped\nExample: !mods Ravage'
        elif Settings.language == "pt":
            msg = 'Mostrar onde o mod vai cair.\nExemplo: !mods Ravage'
        else:
            msg = 'Montre oÃ¹ le mod est droppÃ©\nExemple: !mods Ravage'
    elif commandname == 'resource':
        if Settings.language == "en":
            msg = 'Show where you can find the resource\nExample: !resource Oxium'
        elif Settings.language == "pt":
            msg = 'Mostrar onde Ã© possÃ­vel encontrar o recurso.\nExemplo: !resource Oxium'
        else:
            msg = 'Montre oÃ¹ on peut trouver la ressource\nExample: !resource Oxium'
    elif commandname == 'itemdrops':
        if Settings.language == "en":
            msg = 'Show what mobs drop the item(works with blueprint)\nExample: !itemdrops hildryn neuroptics'
        elif Settings.language == "pt":
            msg = 'Mostra que inimigos droppam o item (funciona com diagramas)\nExemplo: !itemdrops hildryn neuroptics'
        else:
            msg = "Montre quels mobs drop l'objet(fonctionne avec les blueprint)\nExemple: !itemdrops hildryn neuroptics"
    elif commandname == 'baro' or commandname == "voidtrader":
        if Settings.language == "en":
            msg = "Show if baro arrived and him inventory if its the case\nExample:!baro\nExample:!baro xb1"
        elif Settings.language == "pt":
            msg = "Mostra se o Baro chegou e o inventÃ¡rio dele se esse for o caso\nExemplo:!baro\nExemplo:!baro xb1"
        else:
            msg = "Montre si baro est arrivÃ© ainsi que son inventaire si c'est le cas\nExample:!baro xb1"
    elif commandname == 'nora' or commandname == 'nightwave':
        if Settings.language == "en":
            msg = "Show the actual challenge for nightwave\nExample:!nora\nExample:!nora xb1"
        elif Settings.language == "pt":
            msg = 'Mostrar os desafios da Nightwave.\nExemplo:!nora\nExemplo:!nora xb1'
        else:
            msg = 'Montre les challenges de Nora\nExemple:!nora\nExemple:!nora xb1'
    elif commandname == 'fissure':
        if Settings.language == "en":
            msg = 'Show the actual fissures'
        elif Settings.language == "pt":
            msg = 'Mostrar as fissuras atualmente ativas.'
        else:
            msg = 'Montre les fissures actuels'
    elif commandname == 'sortie':
        if Settings.language == "en":
            msg = 'Show the actual sortie'
        elif Settings.language == "pt":
            msg = 'Mostrar as sortie atualmente ativas.'
        else:
            msg = 'Montre la sortie actuel'
    else:
        if Settings.language == "en":
            msg = '```diff\n' \
                  '+ ' + Settings.commandbegin + 'helpW\n' \
                                                 'Show this help\n' \
                                                 '--Market Command--\n' \
                                                 '+ ' + Settings.commandbegin + 'ducats\n' \
                                                                                'Show the best item part to buy for ducats/plat.\n' \
                                                                                '+ ' + Settings.commandbegin + 'WTB "item"\n' \
                                                                                                               'Show the best price for buy item.\n' \
                                                                                                               '+ ' + Settings.commandbegin + 'WTS "item"\n' \
                                                                                                                                              'Show the best price for sell item.\n' \
                                                                                                                                              '+ ' + Settings.commandbegin + 'WTT "item"\n' \
                                                                                                                                                                             'Show the best price for sell and buy item.\n' \
                                                                                                                                                                             '--Drops command--\n' \
                                                                                                                                                                             '+ ' + Settings.commandbegin + 'relic "relic_name" [level of upgrade 0-3]\n' \
                                                                                                                                                                                                            'Show the drop loot table of the relic.\n' \
                                                                                                                                                                                                            '+ ' + Settings.commandbegin + 'searchrelic "relic"\n' \
                                                                                                                                                                                                                                           'Shows where you can loot the relic.\n' \
                                                                                                                                                                                                                                           '+ ' + Settings.commandbegin + 'search "item_name"\n' \
                                                                                                                                                                                                                                                                          'Show where you can drop the ressource\n' \
                                                                                                                                                                                                                                                                          '+ ' + Settings.commandbegin + 'baro [platform] or ' + '+' + Settings.commandbegin + 'voidtrader [platform]\n' \
                                                                                                                                                                                                                                                                                                                                                               "Show if baro arrived and him inventory if its the case\n" \
                                                                                                                                                                                                                                                                                                                                                               '+ ' + Settings.commandbegin + 'nora [platform] or ' + Settings.commandbegin + "nightwave [platform]\n" \
                                                                                                                                                                                                                                                                                                                                                                                                                                              'Show the actual challenge for nightwave\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                              '+ ' + Settings.commandbegin + 'fissure [platform]\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                             'Show the actual fissures\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                             '+ ' + Settings.commandbegin + "earth\nShow if it's day or night on earth.\n" \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            '+ ' + Settings.commandbegin + "cetus\nShow if it's day or night on cetus.\n" \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           '+ ' + Settings.commandbegin + 'sortie\nShow the actual sortie\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          '+ ' + Settings.commandbegin + 'invasion\nShow the actual invasions\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         '\n--Other command--\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         '+ ' + Settings.commandbegin + 'settings\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'Change the settings of the bot (need manage role permissions)\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        '+ !defaultconfig\nChange the commandbegin to default (!)\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        '+ ' + Settings.commandbegin + 'credits\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       'Show credits\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       '+ ' + Settings.commandbegin + 'issue(commandname)(description)\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'Send your issue to the main discord Warframe bot.\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      '+ ' + Settings.commandbegin + 'vote\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'Vote for Warframe bot on discord bot.\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     '```'
        elif Settings.language == "pt":
            msg = '```diff\n' \
                  '+ ' + Settings.commandbegin + 'helpW\n' \
                                                 'Mostrar esta ajuda\n' \
                                                 '--Comando do Mercado--\n' \
                                                 '+ ' + Settings.commandbegin + 'ducats\n' \
                                                                                'Mostra a melhor parte para comprar por ducats/plat.\n' \
                                                                                '+ ' + Settings.commandbegin + 'WTB "recurso"\n' \
                                                                                                               'Mostra o melhor preÃ§o para comprar um item.\n' \
                                                                                                               '+ ' + Settings.commandbegin + 'WTS "recurso"\n' \
                                                                                                                                              'Mostra o melhor preÃ§o para vender um item.\n' \
                                                                                                                                              '+ ' + Settings.commandbegin + 'WTT "recurso"\n' \
                                                                                                                                                                             'Mostra o melhor preÃ§o para vender e comprar um item.\n' \
                                                                                                                                                                             '--Comandos de Drops--\n' \
                                                                                                                                                                             '+ ' + Settings.commandbegin + 'searchrelic "reliquia"\n' \
                                                                                                                                                                                                            'Mostra-me onde podes perder a relÃ­quia.\n' \
                                                                                                                                                                                                            '+ ' + Settings.commandbegin + 'relic "reliquia" [NÃ­vel de melhoria 0-3]\n' \
                                                                                                                                                                                                                                           'Mostra a tabela de chance de recursos da reliquia.\n' \
                                                                                                                                                                                                                                           '+ ' + Settings.commandbegin + 'search "item"\n' \
                                                                                                                                                                                                                                                                          'Mostra que inimigos droppam o item (funciona com diagramas)\n' \
                                                                                                                                                                                                                                                                          '+ ' + Settings.commandbegin + 'baro [Plataforma] ou ' + '+' + Settings.commandbegin + 'voidtrader [Plataforma]\n' \
                                                                                                                                                                                                                                                                                                                                                                 "Mostra se o Baro chegou e o inventÃ¡rio dele se esse for o caso.\n" \
                                                                                                                                                                                                                                                                                                                                                                 '+ ' + Settings.commandbegin + 'nora [Plataforma] ou ' + Settings.commandbegin + "nightwave [Plataforma]\n" \
                                                                                                                                                                                                                                                                                                                                                                                                                                                  'Mostra os desafios da Nightwave.\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                  '+ ' + Settings.commandbegin + 'fissure [Plataforma]\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'Mostra as atuais fissuras\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 '+ ' + Settings.commandbegin + 'invasion\nMostrar a invasÃ£o\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                '+ ' + Settings.commandbegin + "earth\nMostra se Ã© dia ou noite na Terra.\n" \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               '+ ' + Settings.commandbegin + "cetus\nMostra se Ã© dia ou noite em cetus.\n" \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              '+ ' + Settings.commandbegin + ' sortie\nMostra as atuais sortie\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             '\n--Outros Comandos--\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             '+ ' + Settings.commandbegin + 'settings\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'Altera as definiÃ§Ãµes do bot (necessÃ¡rio permissÃµes de cuidador/dono)\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            '+ !defaultconfig\nPÃµe o comando de inicio no padrÃ£o (!)\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            '+ ' + Settings.commandbegin + 'credits\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           'Mostra os crÃ©ditos\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           '+ ' + Settings.commandbegin + 'issue(commando)(descriÃ§Ã£o)\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'Envia o problema para o bot do Discord principal de Warframe Bot\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          '+ ' + Settings.commandbegin + 'vote\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'Vota no Warframe bot no discord bot.\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         '```'

        else:
            msg = '```diff\n' \
                  '+ ' + Settings.commandbegin + 'helpW\n' \
                                                 'Montre cette aide\n' \
                                                 '--Market Commandes--\n' \
                                                 '+ ' + Settings.commandbegin + 'ducats\n' \
                                                                                "Montre l'objet a achetÃ© pour le meilleur taux ducats/plat.\n" \
                                                                                '+ ' + Settings.commandbegin + 'WTB "item"\n' \
                                                                                                               'Montre le meilleur prix pour cette objet pour achat.\n' \
                                                                                                               '+ ' + Settings.commandbegin + 'WTS "item"\n' \
                                                                                                                                              'Montre le meilleur prix pour cette objet pour vente.\n' \
                                                                                                                                              '+ ' + Settings.commandbegin + 'WTT "item"\n' \
                                                                                                                                                                             'Montre le meilleur prix pour cette objet pour vente et achat.\n' \
                                                                                                                                                                             '--Drops command--\n' \
                                                                                                                                                                             '+ ' + Settings.commandbegin + "relic 'relic_name' [niveau d'amelioration 0-3]\n" \
                                                                                                                                                                                                            'Montre tous les loots de la relique.\n' \
                                                                                                                                                                                                            '+ ' + Settings.commandbegin + 'searchrelic "relic"\n' \
                                                                                                                                                                                                                                           "Montre oÃ¹ l'on peut loot la relique .\n" \
                                                                                                                                                                                                                                           '+ ' + Settings.commandbegin + 'search "item_name"\n' \
                                                                                                                                                                                                                                                                          "Montre oÃ¹ on peut loot l'item\n" \
                                                                                                                                                                                                                                                                          '+ ' + Settings.commandbegin + 'baro [platform] ou ' + Settings.commandbegin + 'voidtrader [platform]\n' \
                                                                                                                                                                                                                                                                                                                                                         "Montre si baro est arrivÃ© ainsi que son inventaire si c'est le cas\n" \
                                                                                                                                                                                                                                                                                                                                                         '+ ' + Settings.commandbegin + 'nora [platform] or ' + Settings.commandbegin + "nightwave [platform]\n" \
                                                                                                                                                                                                                                                                                                                                                                                                                                        'Montre les challenges de Nora\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                        '+ ' + Settings.commandbegin + 'invasion\nMontre les invasions\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                       '+ ' + Settings.commandbegin + 'fissure [platform]\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'Montre les fissures actuels\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      '+ ' + Settings.commandbegin + 'earth\nMontre si il fait jour ou nuit sur terre.\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     '+ ' + Settings.commandbegin + 'cetus\nMontre si il fait jour ou nuit sur Cetus.\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    '+ ' + Settings.commandbegin + ' sortie\nMontre la sortie actuel\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   '--Commandes autre--\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   '+ ' + Settings.commandbegin + 'issue(nom de commande)(description)\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'Envoie le problÃ¨me au serveur discord Warframe bot.\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  '+ ' + Settings.commandbegin + 'settings\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'Modifie les options du bot (besoin de pouvoir gere les roles comme permission)\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 '+ !defaultconfig\nChange le debut de commande en !\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 '+ ' + Settings.commandbegin + 'credits\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'Montre les credits\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                '+ ' + Settings.commandbegin + 'vote\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'Votez pour Warframe bot sur Discord bots.\n' \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               '```'
    if commandname != "":
        return msg, "here"
    else:
        return msg