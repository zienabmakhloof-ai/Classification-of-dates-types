import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.preprocessing.image import img_to_array

MODEL_PATH = "model.keras"
INPUT_SIZE = (200, 200)
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


class Model:
    """
    MobileNet-based transfer learning model for date fruit classification.

    Classifies images into one of 9 date fruit categories:
    Ajwa, Galaxy, Mejdool, Meneifi, NabtatAli, Rutab, Shaishe, Sokari, Sugaey.
    """

    def __init__(self, model_path: str = MODEL_PATH):
        # Build the model architecture
        # Note: load_model() is bypassed here due to a known Keras serialization
        # issue with this specific MobileNet configuration. We rebuild the
        # architecture manually and load only the weights.
        base_model = MobileNet(weights=None, include_top=False, input_shape=(200, 200, 3))
        base_model.trainable = False

        self.model = Sequential(
            [
                base_model,
                Flatten(),
                Dense(512, activation="relu"),
                Dense(len(CLASS_NAMES), activation="softmax"),
            ]
        )

        # Build the model by passing a dummy input before loading weights
        dummy_input = np.zeros((1, 200, 200, 3))
        self.model(dummy_input)

        # Load the pre-trained weights
        self.model.load_weights(model_path)
        self.class_names = CLASS_NAMES

    def predict(self, image: Image.Image) -> str:
        """
        Predict the date fruit type from a PIL image.

        Args:
            image: A PIL Image object.

        Returns:
            The predicted class label as a string.
        """
        img = image.resize(INPUT_SIZE)
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0
        probabilities = self.model.predict(img_array)
        class_index = np.argmax(probabilities)
        return self.class_names[class_index]


# Quick test
if __name__ == "__main__":
    model = Model()
    test_image = Image.open("test/NabtatAli/NabtatAli001.jpg")  # Expected: 'NabtatAli'
    label = model.predict(test_image)
    print(f"Predicted label: {label}")
