#license_plate_ocr.py
import streamlit as st
from models.yolo_inference import run_inference_on_frame
import cv2
import tempfile
st.markdown("# License Plate OCR")
st.sidebar.markdown("# OCR")
# Upload video
video_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

if video_file is not None:
    st.video(video_file)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_file.read())
        temp_video_path = temp_video.name

    if st.button("Run YOLO Inference"):
        stframe = st.empty()
        cap = cv2.VideoCapture(temp_video_path)

        st.spinner("Running inference... (streaming frame-by-frame)")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Run inference on the current frame
            result_frame = run_inference_on_frame(frame, task='license_plate_model')  # Your custom frame-level function

            # Convert BGR (OpenCV) to RGB (Streamlit)
            result_frame = cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB)

            # Display the frame
            stframe.image(result_frame, channels="RGB", use_container_width=True)

        cap.release()
        st.success("Inference complete!")
