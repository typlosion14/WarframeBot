import discord
import json

from CobraLib import source_html, StringBetween, importjson
from StorageConfig import Traduction, ConvertPart


def searchPrice(args, orderSearch, marketSize):
    item = ConvertPart(' '.join(args[1:]).lower()).replace(' ', '_')
    # https://warframe.market/items/bo_prime_handle
    # https://api.warframe.market/v1/items/akbronco_prime_blueprint/orders
    try:
        data_json = json.loads(importjson("https://api.warframe.market/v1/items/" + item + "/orders"))['payload']
    except json.decoder.JSONDecodeError:
        if "set" in item:
            return discord.Embed(title="WTB/WTS " + str(' '.join(args[1:]).lower().replace('set', '')),
                                 description=Traduction.bug(item),
                                 color=0xFF0000)
        else:
            args.append("set")
            return searchPrice(args, orderSearch, marketSize)

    image = ""
    image_json = {}

    try:
        image_json = json.loads(importjson("https://api.warframe.market/v1/items/" + item))['payload']['item'][
            'items_in_set']
    except json.decoder.JSONDecodeError:
        image = "https://warframe.market/static/assets/frontend/logo_icon_only.png"

    # https://warframe.market/static/assets/icons/en/thumbs/akbronco_prime_blueprint.34b5a7f99e5f8c15cc2039a76c725069.128x128.png
    if image == "":
        for data in image_json:
            if 'set' in item:
                if item.replace('set', '')[-1] in data['thumb']:
                    image = "https://warframe.market/static/assets/" + data['thumb']
            elif item in data['thumb']:
                image = "https://warframe.market/static/assets/" + data['thumb']
        if image == "":
            image = "https://warframe.market/static/assets/" + image_json[0]['thumb']
    if orderSearch == "sell":
        json_sorted = sorted(data_json['orders'], key=lambda k: k['platinum'], reverse=False)
    else:
        json_sorted = sorted(data_json['orders'], key=lambda k: k['platinum'], reverse=True)

    orderList = []
    for data in json_sorted:
        plat = data['platinum']

        status = data['user']['status']

        username = data['user']['ingame_name']

        reputation = str(data['user']['reputation'])

        order = data['order_type']

        region = data['user']['region']

        quantity = str(data['quantity'])

        if status == "ingame" and order == orderSearch and region == "en":
            orderList.append(
                {"platinium": plat, "player": username, "reputation": reputation, "amount": quantity, "image": image,
                 "item": item})
        if len(orderList) >= marketSize:
            break
    return orderList


def ducats(client):
    data = source_html('https://warframe.market/tools/ducats')
    dicducats = json.loads(StringBetween(data, '"payload": ', '}]}') + '}]}')
    dicitem = json.loads('{"items": ' + StringBetween(data, '"items": ', '}], ').replace('\\', '') + '}]}')
    ducatsparplatinium = dicducats['previous_hour'][0]['ducats_per_platinum_wa']
    ducats = dicducats['previous_hour'][0]['ducats']
    id = dicducats['previous_hour'][0]['item']
    item=""
    for i in range(len(dicitem['items'])):
        if dicitem['items'][i]['id'] == id:
            item = dicitem['items'][i]['item_name']
            break
    embed = discord.Embed(title="Ducats", description=" ".join("!ducats"), color=0xDFB85E)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url,
                     url='https://discordbots.org/bot/591950764289818634')
    return Traduction.ducats(item, ducats, ducatsparplatinium, embed)
