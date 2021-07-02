import cv2
import time
import numpy as np

def run(cam_ind=0):
    cam = cv2.VideoCapture(cam_ind)
    n_frames = 0
    fps = 0
    res = None
    t_start = time.time()
    color = (128,254,128)
    out_str = "Calculating..."
    while True:
        win_name = "Camera - type 'q' to quit."
        cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)
        n, frame = cam.read()
        
        if not n:
            time.sleep(.25)
            continue
            
        n_frames += 1
        if res is None:
            res = frame.shape[:2][::-1]
            
            cv2.resizeWindow(win_name, res)

        if n_frames==26:
            fps = n_frames / (time.time() - t_start)
            out_str = "device=%i, resolution=%s, FPS=%.2f" % (cam_ind, res, fps)
            n_frames = 0
            t_start = time.time()

        font = cv2.FONT_HERSHEY_PLAIN
        font_scale = 1.3
        font_thickness =2
        txt_size = cv2.getTextSize(out_str, font, font_scale,font_thickness)
        pos = 10, txt_size[0][1]+10
        frame = cv2.putText(frame,out_str, pos, font, font_scale, color,font_thickness, cv2.LINE_AA)
        pos = 10, frame.shape[0]-10
        frame = cv2.putText(frame,"'q' to quit", pos, font, font_scale, color,font_thickness, cv2.LINE_AA)
        
        cv2.imshow(win_name, frame)
        k = cv2.waitKey(1)
        if k & 0xff == ord('q'):
            break

if __name__=="__main__":
    run()