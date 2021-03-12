import cv2

class Camera():
    def __init__(self):
        self.dispCamera = True
    
    def set_camera(self, pos):
        self.dispCamera = pos
        
    def gen_frames(self):
        """
        Return the frames from the camera

        :yield: Camera Frames for the HTML
        :rtype: bytes
        """
        camera = cv2.VideoCapture(0)
        
        while self.dispCamera:
            success, frame = camera.read()
            
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                
        camera.release()
        return None
