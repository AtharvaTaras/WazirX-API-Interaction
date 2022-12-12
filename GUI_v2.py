import cv2
import numpy as np
import requests
from time import sleep

URL = "https://api.wazirx.com/api/v2/tickers"
PAIR = 'btcinr'
WAITING_TIME = 1


def get_data():
    response = requests.get(URL)
    _ = response.json()

    buy = (_[PAIR]['buy'])
    sell = (_[PAIR]['sell'])

    return [buy, sell]


def add_text(text, location, color=(255, 255, 255), scale=1):

    cv2.putText(img,
                org=location,
                text=text,
                fontFace=0,
                fontScale=scale,
                thickness=2,
                lineType=2,
                color=color)


while True:
    data = get_data()

    img = np.zeros((300, 700, 3), dtype=np.uint8)
    add_text(PAIR, (10, 100), scale=3)
    add_text(f'Buy Price = {data[0]}', (10, 150))
    add_text(f'Sell Price = {data[1]}', (10, 200))

    cv2.imshow(PAIR.upper(), img)
    cv2.waitKey(1)
    sleep(WAITING_TIME)
    cv2.destroyAllWindows()
