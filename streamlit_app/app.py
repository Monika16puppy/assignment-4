import streamlit as st
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from tensorflow.keras.applications.efficientnet import preprocess_input

model = load_model(r"D:\vscode\aerial_obj_det_proj\models\best_efficientnet_model.keras")
class_names = ['bird', 'drone']
st.title("Aerial Bird vs Drone Classification")

uploaded_file = st.file_uploader(
    "Upload an aerial image",
    type=['jpg', 'jpeg', 'png']
)

if uploaded_file is not None:

    # Display Uploaded Image
    st.image(
        uploaded_file,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Load Image
    img = image.load_img(
        uploaded_file,
        target_size=(224,224)
    )

    # Convert to Array
    img_array = image.img_to_array(img)

    # Expand Dimensions
    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    # Preprocess
    img_array = preprocess_input(img_array)

    # Prediction
    prediction = model.predict(img_array)

    predicted_class = np.argmax(prediction)

    confidence = np.max(prediction) * 100

    # Show Results
    st.subheader(
        f"Prediction: {class_names[predicted_class]}"
    )

    st.subheader(
        f"Confidence: {confidence:.2f}%"
    )