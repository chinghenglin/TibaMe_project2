# 所有路牌的影像資料夾放進 board_imgs 資料夾

'''
圖像大小:
P 1920*1080 (16:9)
S 1920*1080 (16:9)
W 1920*1080 (16:9)
Y 1080*720 (3:2)
'''

# step 1. 固定寬調整大小
# step 2. 調整 (裁切) 寬高比為 16:9
# step 3. 裁切高 (W, Y 上面; P, S 中間)

import os
import cv2
# import numpy as np
# from PIL import Image
import img_func

os.mkdir('./board_imgs_processed')

# 所有的路牌名稱讀成一個 list
with open('board_names.txt', 'r') as f:
    folders = [line.rstrip('\n') for line in f]
# print(folders)

for folder in folders:
    # 指定資料夾路徑和附檔名
    folder_path = f'./board_imgs/{folder}'
    extension = "png"

    # 取得檔案名稱 list
    file_names = img_func.get_fnames(folder_path, extension)
    # print(file_names)

    for file_name in file_names:
        # 讀取影像
        img = cv2.imread(f'./board_imgs/{folder}/{file_name}', 3)
        print('處理中影像:', file_name)

        # 調整影像大小
        img = img_func.resize(img, w = 512)
        # print(img.shape) # (288, 512, 3)

        # 裁切成 16:9
        img = img[0:int(img.shape[1] * 9 / 16), :]
        # print(img.shape) # (288, 512, 3)

        # 裁切影像: P, S 取中間; W, Y 取上面
        if file_name.split('_')[1] in ['P', 'S']:
            img = img_func.crop2(img, 0.4, 'mid')
        elif file_name.split('_')[1] in ['W', 'Y']:
            img = img_func.crop2(img, 0.4, 'up')

        # 儲存影像
        folder_path_to_save = f'./board_imgs_processed/{folder}'
        if not os.path.exists(folder_path_to_save):
            os.mkdir(folder_path_to_save)
        cv2.imwrite(f'{folder_path_to_save}/{file_name}', img)


