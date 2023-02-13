import cv2
import mediapipe as mp
import time
import random
from pifun.distanttest import ifInHand

# 图片导入

imgRat = cv2.imread('rat.png', cv2.IMREAD_UNCHANGED)
imgRat = cv2.resize(imgRat, dsize=(80, 80))
# OpenCV摄像头调用
cap = cv2.VideoCapture(0)  # 选择摄像头的编号

# 定义并引用mediapipe中的hands模块
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,        # 是静态图片还是连续视频帧
                      max_num_hands=1,                # 最多检测几只手
                      min_detection_confidence=0.6,   # 置信度阈值
                      min_tracking_confidence=0.5)    # 追踪阈值


mpDraw = mp.solutions.drawing_utils    # 一个mediapipe自带的绘制函式
handLine = mpDraw.DrawingSpec(color=(255, 255, 255),thickness=3)  # 设置线的样式
handPoint = mpDraw.DrawingSpec(color=(0, 0, 0),thickness=10)  # 设置点的样式
pTime = 0
cTime = 0
"""蚊子坐标与行动时间初始化"""
Time = 0
mx = 0
my = 0
rant =10
p=0
while True:
    success, img = cap.read()  # 读取cap（摄像头）
    img = cv2.flip(img, 1)  # 镜像反转
    imgHeight = img.shape[0]
    imgWidth = img.shape[1]
    ranY = int(random.uniform(0, imgHeight))
    ranX = int(random.uniform(0, imgWidth))
    listX = []
    listY = []
    Time =Time+1
    if success:                # 如果读取成功
        # RGB转化
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)
        """生成随机蚊子"""
        if Time%(rant+1)==0:
            mx = ranX
            my = ranY
            rant = int(random.uniform(0, 50))
        cv2.circle(img,(mx,my),10, (0, 0, 255),cv2.FILLED)

        if result.multi_hand_landmarks:    # 如果检测到关键点
            for handLms in result.multi_hand_landmarks:  # 遍历每个点
                # print(result.multi_hand_landmarks)
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS, handPoint, handLine)  # 在每一帧上画出点
                for i,lm in enumerate(handLms.landmark):  # i第几个点，lm点的坐标
                    print(i, lm.x, lm.y)
                    # 打印的坐标是按比例来算，乘视窗宽度和高度是真正的坐标
                    xPos = int(lm.x * imgWidth)
                    yPos = int(lm.y * imgHeight)
                    cv2.putText(img, str(i), (xPos-5, yPos+5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
                    print(i, xPos, yPos)
                    """存储手掌边缘点位"""
                    if(i in [0,4,8,12,16,20]):
                        listX.append(xPos)
                        listY.append(yPos)
                """检测蚊子是否被抓住"""
                if ifInHand(listX[0],listY[0],listX[1],listY[1],listX[2],listY[2],listX[3],listY[3],listX[4],listY[4],listX[5],listY[5],mx,my):
                    p=p+1
            """计算FPS模块"""
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, f"FPS:{int(fps)}",(30,50),cv2.FONT_HERSHEY_PLAIN,2 ,(0,0,0), 3)
        cv2.putText(img, f"point:{int(p)}", (100, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)
        cv2.imshow('img', img)   # 显示每一帧

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

