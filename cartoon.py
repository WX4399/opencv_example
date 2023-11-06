import cv2
from google.colab.patches import cv2_imshow

# ... 在這裡執行圖像處理代碼 ...

# 顯示卡通效果
cv2_imshow(cartoon)


# 載入圖片
input_path = 'output.png'
image = cv2.imread(input_path)

# 將圖片轉換為灰度圖
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 應用高斯模糊以平滑圖像
gray_blurred = cv2.GaussianBlur(gray, (15, 15), 0)

# 檢測邊緣
edges = cv2.adaptiveThreshold(gray_blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# 創建卡通效果
color = cv2.bilateralFilter(image, d=9, sigmaColor=300, sigmaSpace=300)

# 合併邊緣和彩色圖像以獲得卡通效果
cartoon = cv2.bitwise_and(color, color, mask=edges)

# # 顯示卡通效果
# cv2.imshow("Cartoon Image", cartoon)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 顯示卡通效果
cv2_imshow(cartoon)
