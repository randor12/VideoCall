from flask import *
from models.Camera import *
import json

app = Flask(__name__)
app.secret_key = 'S3CR3T_K3Y'

people = {}

cam = Camera()

@app.route('/turn_on_camera', methods=['GET', 'POST'])
def turn_on_camera():
    try:
        cam.set_camera(True)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except Exception as e:
        print(e.with_traceback())
        return json.dumps({'success': False}), 500, {'ContentType': 'application/json'}

@app.route('/turn_off_camera', methods=['GET', 'POST'])
def turn_off_camera():
    try:
        cam.set_camera(False)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except Exception as e:
        print(e.with_traceback())
        return json.dumps({'success': False}), 500, {'ContentType': 'application/json'}

@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html') 

@app.route('/video_feed')
def video_feed():
    """
    Return the video feed of your camera

    :return: Video feed
    :rtype: Response
    """
    # track which video is "my" video
    if 'temp-id' in session.keys():
        id_val = session['temp-id']
    else:
        id_val = len(people) + 1
        session['temp-id'] = id_val
    
    video = Response(cam.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
    people[id_val] = video
    
    return video

if __name__ == '__main__':
    app.run(debug=True)