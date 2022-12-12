import cv2
import numpy as np
import requests
from time import sleep

URL = "https://api.wazirx.com/api/v2/tickers"
PAIR = 'btcinr'
WAITING_TIME = 60
WINDOW_SIZE = (300, 500, 3)


def get_data():
    response = requests.get(URL)
    _ = response.json()

    buy = float((_[PAIR]['buy']))
    sell = float((_[PAIR]['sell']))
    avg = float((buy+sell)/2)

    return [buy, sell, avg]


def change(old):
    new = get_data()[2]

    delta = (new-old)
    if delta >= 0:
        col = (0, 150, 0)

    else:
        col = (0, 0, 150)

    return [delta, col]


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
    old_avg = (data[0] + data[1])/2
    delta_attr = change(old_avg)
    deltacolor = delta_attr[1]
    deltavalue = delta_attr[0]

    img = np.zeros(WINDOW_SIZE, dtype=np.uint8)

    add_text(PAIR,
             (10, 100),
             scale=3,
             color=(175, 90, 55))

    add_text(f'Buying Price = {data[0]}',
             (10, 150))

    add_text(f'Selling Price = {data[1]}',
             (10, 200))

    add_text(f'Change Since Last = {deltavalue}',
             (10, 250),
             color=deltacolor)

    cv2.imshow(PAIR.upper(), img)
    cv2.waitKey(1)
    sleep(WAITING_TIME)
    cv2.destroyAllWindows()
