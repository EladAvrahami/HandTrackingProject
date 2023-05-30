import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)


mpHands = mp.solutions.hands
hands= mpHands.Hands() #1 readme commant realted
#mediapipe method helps draw points on the hands and lines between them
mpDraw = mp.solutions.drawing_utils

pTime = 0 #previos time
cTime = 0 #current time
#fps - frame per seconde

while True:
    success, img =cap.read()
    imgRGB =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#convert to rgb because hands obj only use rgb images
    results =hands.process(imgRGB) #process method -will process the frame for me and give results
    #print(results.multi_hand_landmarks)#to chack if any hand detected or not we use multi_hand_landmarks

    if results.multi_hand_landmarks:
        print("id", "cx", "cy")
        for handLms in results.multi_hand_landmarks: #for each hand loop recogmized
            for id, landMark in enumerate(handLms.landmark):
               # print(id,landMark)#it will print me decimal x y z of my hand
                h, w, channels =img.shape #this will give me the width and hight of each landmark (points on my hand)
                cx, cy =int(landMark.x*w), int(landMark.y*h)
                print(id, cx ,cy)
                #if id == 4 :
                cv2.circle(img, (cx, cy), 15, (255,0,250), cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS ) #img -is the live camera stream handLms-is the item of the loop in this case hands, mpHands.HAND_CONNECTIONS- is obj model that add lines between dots
    cTime =time.time()
    fps =1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,5 ,(0, 0, 255),6 ) #put FPS TEXT ON CAMERA as string chosse the position,text shape size color and bolt
    cv2.putText(img,"Elad Avrahami Hands Tracking",(10 ,450),cv2.FONT_HERSHEY_PLAIN ,2,(0, 0, 0),2 )

    cv2.imshow("image",img)
    cv2.waitKey(1)