import glob
import os
import cv2

def get_fnames(folder_path, extension):
    # 構建搜尋的路徑
    search_path = os.path.join(folder_path, f"*.{extension}")
    # 使用 glob 模組進行檔案搜尋
    files = glob.glob(search_path)
    # 取得檔案名稱並存入 list
    file_names = [os.path.basename(file) for file in files]
    return file_names

def resize(img, w): # w 輸入需要的影像寬度
    h = int(img.shape[0] * (w / img.shape[1])) # 依照原比例縮放
    return cv2.resize(img, (w, h))

def crop2(img, prop, loc): # prop 裁切影像高度比例; loc: up 切上面, mid 切中間
    h = int(img.shape[0] * prop)
    if loc == 'up':
        return img[0:h, :]
    elif loc == 'mid':
        y = int(img.shape[0] * ((1 - prop) / 2))
        return img[y:(y + h), :]
    else:
        return img

