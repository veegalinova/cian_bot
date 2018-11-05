import requests
import json
import re


def _parse_page(url):
    flats = []
    search_page = requests.get(url)
    search = re.search(r'\"products\":\[{(.*)}\]};', search_page.text)
    if search:
        for flat in search.group(1).split('},{'):
            flats.append(json.loads('{' + flat.replace(r'\u002F', '') + '}'))

    return flats


def get_new(url, save_file):
    flats = _parse_page(url)
    result = []

    with open(save_file, 'a+') as file:
        file.seek(0)
        lines = file.read()
        content = {}
        if len(lines) != 0:
            content = json.loads(lines)
        for flat in flats:
            if str(flat['cianId']) not in content.keys():
                content.update({flat['cianId']: flat})
                id = flat['cianId']
                link = f'https://www.cian.ru/rent/flat/{id}'
                result.append({'price': flat['price'], 'owner': flat['owner'], 'url': link})

    with open(save_file, 'w')as file:
        json.dump(content, file)

    return result
