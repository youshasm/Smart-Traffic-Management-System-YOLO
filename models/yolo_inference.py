# models/yolo_inference.py
import cv2
from ultralytics import YOLO
def run_inference_on_frame(frame, task='vehicles_detection',):
    model=YOLO(f'models/{task}.pt')
    results = model.predict(source=frame, conf=0.3, stream=False,verbose=False)
    annotated_frame = results[0].plot()
    return annotated_frame
