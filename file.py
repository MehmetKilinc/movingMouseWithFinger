import cv2
import pyautogui as pg
import mediapipe as mp

cap = cv2.VideoCapture(0)
el_nesnesi = mp.solutions.hands
eller = el_nesnesi.Hands()
cizgiler = mp.solutions.drawing_utils

while True:
	ret , frame = cap.read()
	resimRGB = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
	sonuc = eller.process(resimRGB)
	if sonuc.multi_hand_landmarks:
		for i in sonuc.multi_hand_landmarks:
			cizgiler.draw_landmarks(frame , i , el_nesnesi.HAND_CONNECTIONS)
			for id,j in enumerate(i.landmark):
				h,w,c = frame.shape
				cx,cy = int(j.x*w),int(j.y*h)
				if id == 8:
					cv2.circle(frame,(cx,cy),9,(255,0,0),cv2.FILLED)
					pg.moveTo(cx , cy)

	cv2.imshow("video",frame)
	if cv2.waitKey(1) & 0XFF == ord("q"):
		break
