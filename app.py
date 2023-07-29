import djitellopy as tello
from tkinter import *
from PIL import ImageTk, Image
import time
import cv2

root = Tk()
root.title("Delight Drone")
root.geometry('1050x420')
root.resizable(False, False)

lbl = Label(root, text="Tello Drone Control", font=("Helvetica", 20, "bold"))
lbl.place(x=720, y=20)

# Create a frame
app = Frame(root, bg="white")
app.grid()
# Create a label in the frame
lmain = Label(app)
lmain.grid()

# Capture from camera
#cap = cv2.VideoCapture(0)

drone = tello.Tello()

drone.connect()

print(drone.get_battery())

drone.streamon()

global img

def moveDrone(move):
    lr, fb, ud, yv = 0, 0, 0, 0

    speed = 50

    if move == "takeoff":
        drone.takeoff()
    elif move == "forward":
        fb = speed
    elif move == "backward":
        fb = -speed
    elif move == "up":
        ud = speed
    elif move == "down":
        ud = -speed
    elif move == "left":
        lr = -speed
    elif move == "right":
        lr = speed
    elif move == "yaw_left":
        yv = -speed
    elif move == "yaw_right":
        yv = speed
    elif move == "land":
        drone.land()
    elif move == "screenshot":
        cv2.imwrite(f"CameraFeed/Images/{time.time()}.jpg", img)
        time.sleep(0.3)
    drone.send_rc_control(lr, fb, ud, yv)
    time.sleep(1)
    drone.send_rc_control(0, 0, 0, 0)


btn = Button(root, text="▲", fg="white", background="purple", borderwidth=0, font=("Helvetica", 14, "bold"), command=lambda: moveDrone("forward"))
btn2 = Button(root, text="◄", fg="white", background="purple", borderwidth=0, font=("Helvetica", 14, "bold"), command=lambda: moveDrone("left"))
btn3 = Button(root, text="►", fg="white", background="purple", borderwidth=0, font=("Helvetica", 14, "bold"), command=lambda: moveDrone("right"))
btn4 = Button(root, text="▼", fg="white", background="purple", borderwidth=0, font=("Helvetica", 14, "bold"), command=lambda: moveDrone("backward"))

btn9 = Button(root, text="↶", fg="white", background="black", borderwidth=0, font=("Helvetica", 20,), command=lambda: moveDrone("yaw_left"))
btn10 = Button(root, text="↻", fg="white", background="black", borderwidth=0, font=("Helvetica", 20,), command=lambda: moveDrone("yaw_right"))

btn5 = Button(root, text="Take Off", fg="white", background="black", borderwidth=0, font=("Helvetica", 10,), command=lambda: moveDrone("takeoff"))
btn7 = Button(root, text="↑", fg="white", background="black", borderwidth=0, font=("Helvetica", 20), command=lambda: moveDrone("up"))
btn8 = Button(root, text="↓", fg="white", background="black", borderwidth=0, font=("Helvetica", 20), command=lambda: moveDrone("down"))
btn6 = Button(root, text="Land", fg="white", background="black", borderwidth=0, font=("Helvetica", 10), command=lambda: moveDrone("land"))


btn.place(height=70, width=70, x=820, y=90)
btn2.place(height=70, width=70, x=720, y=170)
btn3.place(height=70, width=70, x=920, y=170)
btn4.place(height=70, width=70, x=820, y=250)
btn5.place(height=40, width=80, x=760, y=370)
btn6.place(height=40, width=80, x=850, y=370)
btn7.place(height=40, width=40, x=940, y=370)
btn8.place(height=40, width=40, x=990, y=370)
btn9.place(height=40, width=40, x=660, y=370)
btn10.place(height=40, width=40, x=710, y=370)

# function for video streaming
def video_stream():
    frame = drone.get_frame_read().frame
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    cv2image = cv2.resize(cv2image, (640, 420))
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream) 

video_stream()

root.mainloop()