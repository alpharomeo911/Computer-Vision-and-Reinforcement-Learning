import numpy as np
import cv2
from PIL import ImageGrab
import time

last_time = time.time()

while(True):
    imageGrab = ImageGrab.grab(bbox=(0, 22, 800, 620))
    print(time.time()-last_time)
    last_time = time.time()
    cv2.imshow('window', cv2.cvtColor(np.array(imageGrab), cv2.COLOR_BGR2RGB))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    