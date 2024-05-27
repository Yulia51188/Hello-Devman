import requests

URL_TEMPLATE = 'https://wttr.in/{}'


def main():
    headers = {'Accept-Language': 'ru-RU'}
    params = {
        'lang': 'ru',
        'M': '',
        'm': '',
        'T': '',
        'n': '',
        'q': '',
    }

    url = URL_TEMPLATE.format('Москва')
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    main()
