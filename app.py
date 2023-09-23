import time
from flask import Flask, request, render_template, Response
import cv2
import threading

#app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
# Create a VideoCapture object for capturing video from a camera or file
#cap = cv2.VideoCapture(0)  # Update with the path to your video file

@app.route('/')
def index():
    return render_template('p1.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/more1')
def more1():
    return render_template('more1.html')

@app.route('/pg', methods=['POST'])
def pg():
    if request.method=='POST':
        
        return render_template('pg.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def gen():
    # cap = cv2.VideoCapture(0) 
    # while(cap.isOpened()):
    #     ret,img=cap.read()
    #     if ret == True:
    #         img=cv2.resize(img,(0,0),fx=1.5,fy=1.5)
    #         frame=cv2.imencode('.jpg',img)[1].tobytes()
    #         yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    #         time.sleep(0.1)
    #     else:
    #         break

# Create a VideoCapture object to capture video from the default camera (usually the built-in webcam).
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    # Loop to continuously capture and display frames from the camera
    while True:
        # Read a frame from the camera
        ret, img= cap.read()
        img=cv2.resize(img,(0,0),fx=1.5,fy=1.5)
        frame=cv2.imencode('.jpg',img)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.1)
        # Check if the frame was read successfully
        if not ret:
            print("Error: Could not read frame.")
            break



@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)