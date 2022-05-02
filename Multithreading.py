import cv2
import os
import numpy as np
import urllib.request
import time
import threading
import math
import matplotlib.pyplot as plt

y=[] #time on y axis
x = list(range(1, 41)) #num of images on x axis
def getImage(start, end):
    print("Started worker for image number ranged :", start, "to", end)
    for i in range(start, end):
        try:
            url='https://random.imagecdn.app/500/150'
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            binary_str = response.read()
            byte_array = bytearray(binary_str)
            y.append(time.time()-start_time)
            numpy_array = np.asarray(byte_array, dtype="uint8")
            image = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)
            cv2.imwrite("images_multithreading/" + '{:04d}'.format(i) + '.png', image)
            print("Saved " + '{:04d}'.format(i) + '.png')
        except Exception as e:
            print(str(e))

print("Done")
start_time = time.time()
thread_count = 8
image_count = 40
thread_list = []

for i in range(thread_count):
    start = math.floor(i * image_count / thread_count) + 1
    end = math.floor((i + 1) * image_count / thread_count) + 1
    thread_list.append(threading.Thread(target=getImage, args=(start, end)))

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()


end_time = time.time()
print("Done")
print("Time taken : " + str(end_time - start_time) + "sec")
plt.plot(x, y)
plt.xlabel('number of images')
plt.ylabel('Time')
plt.show()
os.system('pause')