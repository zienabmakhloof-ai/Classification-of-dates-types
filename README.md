# 🌴 Date Fruit Classification App

A **Streamlit** web application that uses a **MobileNet** transfer-learning model to classify **9 types** of Saudi date fruits. After classification, an LLM-powered chatbot generates an interesting fact about the identified fruit.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Image Classification** | Identifies the date fruit type from an uploaded image |
| 🤖 **AI Fun Facts** | Generates interesting facts via LLaMA 3.1 70B (OpenRouter) |
| ✏️ **Annotation Tool** | Draw bounding boxes, crop regions, and manually save labels |

---

## 🍂 Supported Date Varieties

| | | |
|---|---|---|
| Ajwa | Galaxy | Mejdool |
| Meneifi | NabtatAli | Rutab |
| Shaishe | Sokari | Sugaey |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/zienabmakhloof-ai/Classification-of-dates-types.git
cd Classification-of-dates-types
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

```bash
cp .env.example .env
```

Open `.env` and add your [OpenRouter](https://openrouter.ai/keys) API key:

```
OPENROUTER_API_KEY=sk-or-v1-...
```

### 5. Add the trained model weights

Download `model.keras` and place it inside the `app/` folder:

```
app/
└── model.keras   ← place here
```

> **Note:** The model weights are not included in this repository due to file size.  

### 6. Run the app

```bash
streamlit run app/main.py
```

The app will open at `http://localhost:8501`.

---

## 📁 Project Structure

```
date-fruit-classification/
├── app/
│   ├── main.py              # Main Streamlit application
│   ├── model.py             # MobileNet model class
│   ├── chatbot.py           # OpenRouter LLM chatbot
│   └── annotation_tool.py  # Standalone annotation utility
├── notebooks/
│   └── model_training.ipynb # Training pipeline & evaluation
├── samples/
│   └── cropped_image_*.jpg  # Example classified images
├── .env.example             # Environment variable template
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧠 Model Architecture

- **Base model:** MobileNet (pretrained on ImageNet, top layers removed)
- **Custom head:** `Flatten → Dense(512, ReLU) → Dense(9, Softmax)`
- **Input size:** 200 × 200 × 3
- **Training:** Transfer learning with frozen base layers; SGD optimiser

See [`notebooks/model_training.ipynb`](notebooks/model_training.ipynb) for the full training pipeline.

---

## 🖼️ Demo



https://github.com/user-attachments/assets/ae84d2cc-141a-470a-9f5c-6b8f0cf4871a



---
## 🔧 Usage

### Classification Mode
1. Upload a date fruit image (`.jpg`, `.jpeg`, or `.png`)
2. Select **"Classify Date Fruit"**
3. The model predicts the type and the chatbot shares a fun fact

### Annotation Mode
1. Upload an image
2. Select **"Use Annotation Tool"**
3. Draw a bounding box around the fruit
4. Click **Save** to store the cropped region and its label

### Standalone Annotation Tool
```bash
streamlit run app/annotation_tool.py
```

---

## 📦 Dependencies

| Library | Purpose |
|---|---|
| TensorFlow / Keras | Model inference |
| Streamlit | Web interface |
| streamlit-drawable-canvas | Annotation drawing |
| Pillow / OpenCV | Image processing |
| openai (v0.28) | OpenRouter API client |
| python-dotenv | Environment variable management |

---

## ⚠️ Important Notes

- **API Key:** Never commit your `.env` file. The `.gitignore` is already configured to exclude it.
- **Model Weights:** The `model.keras` file is excluded from Git (add to Git LFS or share a download link).
- **Python Version:** Tested on Python 3.10+.
