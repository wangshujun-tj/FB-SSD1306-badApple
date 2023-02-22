import cv2 as cv
import numpy as np
from PIL import Image
import os
#加载的库，opencv pillow numpy
#如果不是第一次运行，最好先删除after目录下的所有图片
v_cap = cv.VideoCapture('Bad Apple.avi')  # 打开视频
f_total = v_cap.get(cv.CAP_PROP_FRAME_COUNT)

print("视频总长度",f_total)

f_skip = 4  # 隔3帧截一次图，数字越小，播放越细腻

if v_cap.isOpened():  # 判断是否正常打开
    frame_count=0
    file_count = 0

    while True:  # 循环读取视频帧
        v_cap.set(cv.CAP_PROP_POS_FRAMES,frame_count)
        rval, frame = v_cap.read()
        if rval==False:
            break
        frame = cv.resize(frame, (128, 64))  # 调整尺寸
        gray=Image.fromarray(cv.cvtColor(frame,cv.COLOR_RGB2BGR))
        new=gray.convert("1")
        new.save(f"after/%4.4d.bmp"%file_count, 'bmp')
        file_count += 1
        frame_count += f_skip
    print("总共转换了%d张图片"%file_count)
