# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------

import requests

from bs4 import BeautifulSoup


URL = "https://www.crous-lille.fr/restaurant/r-u-de-lens/"

def get_text() -> str:

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, features="html.parser")

    div = soup.findAll('div', {'class': 'meal'}).pop(0)

    titre = div.findAll('div', {'class': 'meal_title'}).pop().get_text()
    text = f"__{titre}__"

    for liste in div.findAll('ul', {'class': 'meal_foodies'}):
        for element in liste.findAll('li', recursive=False):
            text += f"\n> **{element.contents[0]}**"
            for produit in element.findAll('li'):
                text += f"\n- {produit.get_text()}"

    return text
