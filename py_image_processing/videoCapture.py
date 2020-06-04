import cv2 

video=cv2.VideoCapture(0)

video.release()

check, frame = video.read()

print(check)
print(frame)

gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
time.sleep(3)
cv2.imshow("Capturing", gray)

cv.waitKey(0)
video.release()
cv2.destroyAllWindows
