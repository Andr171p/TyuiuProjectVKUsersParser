import requests
import pandas as pd
import random

import warnings
warnings.filterwarnings("ignore")


# this function return dict of proxies:
def fake_free_proxy_dict():
    response = requests.get('https://free-proxy-list.net/')
    proxy_dataframe = pd.read_html(response.text)[0]

    ip = proxy_dataframe['IP Address']
    port = proxy_dataframe['Port']

    proxy_table = []
    for i in range(ip.shape[0]):
        if proxy_dataframe['Https'][i] == 'yes':
            proxy_table.append([ip[i], str(port[i])])

    return proxy_table


# this function return random proxy:
def random_free_proxy(proxy_table):
    proxy = random.choice(proxy_table)

    return proxy


# this function return fake proxy:
def get_fake_free_proxy():
    proxies = fake_free_proxy_dict()
    proxy = random_free_proxy(proxies)

    ip = proxy[0]
    port = proxy[1]

    return ip, port

