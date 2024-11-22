import cv2
import numpy as np
import pyautogui
import time

duration = 10

output_file = "screen_recording.avi"

screen_size = pyautogui.size()

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_file, fourcc, 20.0, (screen_size.width, screen_size.height))

start_time = time.time()
while True:
    img = pyautogui.screenshot()

    frame = np.array(img)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    out.write(frame)

    if time.time() - start_time > duration:
        break

out.release()

print(f"Screen recording saved as {output_file}")