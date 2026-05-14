import numpy as np
import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas

from model import Model
from chatbot import chat_with_bot

# ── Page configuration ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Date Fruit Classification",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🌴 Date Fruit Classification App")
st.markdown(
    """
    This app uses a **MobileNet** transfer-learning model to classify **9 types** of Saudi date fruits.
    Upload an image and choose between **automatic classification** or **manual annotation**.
    """
)

# ── Load model (cached so it's only loaded once) ──────────────────────────────
@st.cache_resource
def load_model() -> Model:
    return Model()


model = load_model()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("About")
    st.markdown(
        """
        **Supported Date Types**
        - Ajwa  
        - Galaxy  
        - Mejdool  
        - Meneifi  
        - NabtatAli  
        - Rutab  
        - Shaishe  
        - Sokari  
        - Sugaey  
        """
    )

# ── Main content ──────────────────────────────────────────────────────────────
uploaded_file = st.file_uploader(
    "Choose an image…", type=["jpg", "jpeg", "png"], accept_multiple_files=False
)

option = st.radio(
    "Choose an option:",
    ("Classify Date Fruit", "Use Annotation Tool"),
    horizontal=True,
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=300)

    # ── Classification mode ───────────────────────────────────────────────────
    if option == "Classify Date Fruit":
        with st.spinner("Classifying…"):
            label = model.predict(image)

        st.success(f"**Predicted class:** {label}")

        with st.spinner("Fetching a fun fact…"):
            response = chat_with_bot(label)
        st.info(f"🤖 **Fun Fact:** {response}")

    # ── Annotation mode ───────────────────────────────────────────────────────
    elif option == "Use Annotation Tool":
        st.write("Draw a rectangle around the date fruit you want to classify:")

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
                st.image(cropped_image, caption="Cropped Region", width=300)

                with st.spinner("Classifying cropped image…"):
                    cropped_label = model.predict(Image.fromarray(cropped_image))

                st.success(f"**Predicted class:** {cropped_label}")

                if st.button("💾 Save Cropped Image and Label"):
                    filename = f"cropped_image_{cropped_label}.jpg"
                    Image.fromarray(cropped_image).save(filename)
                    with open("labels.txt", "a") as f:
                        f.write(
                            f"Image: {filename}, Label: {cropped_label}, "
                            f"Coordinates: ({x0}, {y0}), ({x1}, {y1})\n"
                        )
                    st.success(f"Saved as **{filename}** with label **{cropped_label}**.")
