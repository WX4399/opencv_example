import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# 載入灰度圖像
img = cv2.imread("S.png", cv2.IMREAD_GRAYSCALE)

if img is not None:
    # 將灰度圖像轉換為三通道的彩色圖像
    img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # 應用鉛筆素描效果
    img1, img2 = cv2.pencilSketch(img_color)

    # 顯示原始灰度圖像
    cv2_imshow(img_color)

    # 顯示兩種鉛筆素描效果
    cv2_imshow(img1)
    cv2_imshow(img2)

    cv2.waitKey(0)
else:
    print("無法讀取圖像文件。請確保圖像存在並具有正確的路徑。")
