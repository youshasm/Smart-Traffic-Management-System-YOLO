#app.py
import streamlit as st
st.title(":rainbow[Smart Traffic Management System]")
st.markdown(
    """ 
    **Play with :rainbow[YOLO]**
    """
)

main_page=st.Page("main.py",title="Home",icon="🎈")
page_1=st.Page("features/vehicles_detection.py",title="Page 1",icon = "❄️")
page_2=st.Page("features/crosswalk_pedestrians.py",title="Page 2",icon = "❄️")
page_3=st.Page("features/signal_color.py",title="Page 3",icon = "❄️")
page_4=st.Page("features/license_plate_ocr.py",title="Page 4",icon = "❄️")
pg=st.navigation([main_page,page_1,page_2,page_3,page_4])
pg.run()
