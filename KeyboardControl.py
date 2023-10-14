from djitellopy import tello
import KeyPressModule as kP
import time
import cv2

kP.init()
me = tello.Tello()
me.connect()
print(me.get_battery())


def get_keyboard_input():
    lr, fb, ud, yv = 0, 0, 0, 0

    if kP.get_key("LEFT"):
        lr = -50
    elif kP.get_key("RIGHT"):
        lr = 50

    if kP.get_key("UP"):
        fb = 50
    elif kP.get_key("DOWN"):
        fb = -50

    if kP.get_key("w"):
        ud = 50
    elif kP.get_key("s"):
        ud = -50

    if kP.get_key("a"):
        yv = -50
    elif kP.get_key("d"):
        yv = 50

    if kP.get_key("q"):
        me.takeoff()
    elif kP.get_key("e"):
        me.land()

    if kP.get_key("p"):
        cv2.imwrite(f'Images/{time.time}.jpg', img)

    return [lr, fb, ud, yv]


while True:
    values = get_keyboard_input()
    me.send_rc_control(values[0], values[1], values[2], values[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
