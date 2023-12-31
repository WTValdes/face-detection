import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


def detect_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return img
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    return img


cap = cv2.VideoCapture(1)


while True:
    ret, frame = cap.read()
    frame = detect_faces(frame)

    cv2.imshow('Video Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# # smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
# #body_cascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')
# cap=cv2.VideoCapture(1)
# while True:
# 	ret, img=cap.read()
# 	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 	faces = face_cascade.detectMultiScale(gray)
# 	for (x,y,w,h) in faces:
# 		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
# 		# font=cv2.FONT_HERSHEY_SIMPLEX
# 		#cv2.putText(img,'Jeevy',(x+w/2,y+h/2),font,0.5,(0,0,255),1,cv2.LINE_AA)
# 		print(x,y)
# 		roi_gray = gray[y:y+h, x:x+w]
# 		roi_color = img[y:y+h, x:x+w]
# 		eyes=eye_cascade.detectMultiScale(roi_gray)
# 		# smiles=smile_cascade.detectMultiScale(roi_gray)
# 		for(ex,ey,ew,eh) in eyes:
# 			cv2.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh),(0,255,0),2)
# 			print(ex,ey)
# 		# for(sx,sy,sw,sh) in smiles:
# 			# cv2.rectangle(roi_color,(sx, sy),(sx+sw, sy+sh),(0,0,255),2)
# 			# print(sx,sy)
# 	cv2.imshow('img',img)
# 	k=cv2.waitKey(30) & 0xFF
# 	if k==32:
# 		break
#
# cap.release()
# cv2.destroyAllWindows()
