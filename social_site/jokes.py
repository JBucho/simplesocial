from bs4 import BeautifulSoup
import requests
from random import choice


def get_joke_img():
    url = "https://hackernoon.com/30-jokes-only-programmers-will-get-a901e1cea549"

    page_response = requests.get(url, timeout=5)

    page_content = BeautifulSoup(page_response.content, "html.parser")

    joke_images = page_content.find_all("img", {"class": "graf-image"})

    jokes = []
    for image in joke_images:
        jokes.append(image["src"])

    return choice(jokes)
