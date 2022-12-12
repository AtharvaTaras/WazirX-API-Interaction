import cv2
import numpy as np
import requests

URL = "https://api.wazirx.com/api/v2/tickers"

def add_text(text, location, color=(255, 255, 255), scale=1):

    cv2.putText(img,
                org=location,
                text=text,
                fontFace=0,
                fontScale=scale,
                thickness=2,
                lineType=2,
                color=color)


img = np.zeros((300, 700, 3), dtype=np.uint8)


add_text('CRYPTO NAME', (10, 100), scale=3)
add_text('Buy Price = ', (10, 150))
add_text('Sell Price =', (10, 200))


cv2.imshow('API', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
