"""
Standalone annotation tool for manually labelling date fruit images.
Run with:  streamlit run annotation_tool.py
"""

import numpy as np
import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas

CLASS_NAMES = [
    "Ajwa",
    "Galaxy",
    "Mejdool",
    "Meneifi",
    "NabtatAli",
    "Rutab",
    "Shaishe",
    "Sokari",
    "Sugaey",
]

st.set_page_config(page_title="Date Fruit Annotation Tool", page_icon="🌴")
st.title("🌴 Date Fruit Annotation Tool")

uploaded_file = st.file_uploader("Choose an image…", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.write("Draw a rectangle around the area of interest:")

    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0)",
        background_image=image,
        width=image.width,
        height=image.height,
        drawing_mode="rect",
        key="canvas",
        stroke_width=2,
        stroke_color="rgba(255, 0, 0, 1)",
    )

    if canvas_result.json_data is not None:
        objects = canvas_result.json_data.get("objects", [])

        if objects:
            obj = objects[0]
            x0 = int(obj["left"])
            y0 = int(obj["top"])
            x1 = int(obj["left"] + obj["width"])
            y1 = int(obj["top"] + obj["height"])

            cropped_image = np.array(image)[y0:y1, x0:x1]
            st.image(cropped_image, caption="Cropped Region", use_container_width=True)

            label = st.selectbox("Select a label for the cropped image:", CLASS_NAMES)

            if st.button("💾 Save Cropped Image and Label"):
                filename = f"cropped_image_{label}.jpg"
                Image.fromarray(cropped_image).save(filename)
                with open("labels.txt", "a") as f:
                    f.write(
                        f"Image: {filename}, Label: {label}, "
                        f"Coordinates: ({x0}, {y0}), ({x1}, {y1})\n"
                    )
                st.success(f"Saved as **{filename}** with label **{label}**.")
