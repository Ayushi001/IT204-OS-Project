import cv2
import os
import numpy as np
import urllib.request
import time
import matplotlib.pyplot as plt

start_time = time.time()

y=[] #time on y axis
x = list(range(1, 40)) #num of images on x axis
#for j in range(1, 40):

for i in range(1, 40):
    try:
        url='https://random.imagecdn.app/500/150'
        req=urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        rr = response.read()
        ba = bytearray(rr)
        y.append(time.time() - start_time)
        image = np.asarray(ba, dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
        cv2.imwrite("images/" + '{:04d}'.format(i) + ".png", image)
        print("Saved " + '{:04d}'.format(i) + ".png")
    except Exception as e:
        print("Error Occured for Pokemon " + '{:04d}'.format(i))
        print(str(e))
        
end_time = time.time()
print("Done")
print("Time Taken = ", end_time - start_time, "sec")
plt.plot(x, y)
plt.xlabel('number of images')
plt.ylabel('Time')
plt.show()
os.system('pause')