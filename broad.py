import cv2
rtsp_url_base = "rtsp://admin:Kody@1.2.3@192.168.0.100:554/Streaming/Channels/101"
rtsp_url = f"{rtsp_url_base}robot_2_camera_0?byPassMe=true"
video = cv2.VideoCapture(rtsp_url)

cap=cv2.VideoCapture(r"rtsp://192.168.1.86:8554/robot_1_camera_0?byPassMe=true",cv2.CAP_DSHOW)
while True:
    ret,frame=cap.read()
    if not ret:
        print("OOPS!!")
        break
    cv2.imshow("Broad",frame)

    if cv2.waitKey(1)& 0XFF==ord("q"):
        print("Quit")
        break
cap.release()
cv2.destroyAllWindows()