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
---

## 📊 Model Performance | أداء النموذج

<div align="center">

### 🏆 Overall Accuracy: 92%

![Python](https://img.shields.io/badge/Accuracy-92%25-brightgreen?style=flat-square)
![Classes](https://img.shields.io/badge/Classes-9_Date_Varieties-blue?style=flat-square)
![Model](https://img.shields.io/badge/Model-MobileNet_Transfer_Learning-orange?style=flat-square)

</div>

---

### 📉 Training Curves 

<div align="center">

| Training & Validation Accuracy | Training & Validation Loss |


<img width="547" height="435" alt="acc" src="https://github.com/user-attachments/assets/69111160-5b47-4b14-a690-fd733483b752" /> | <img width="547" height="435" alt="loss" src="https://github.com/user-attachments/assets/3ab57b57-f814-406c-81d4-7a355784e0de" />

</div>

> The model converges steadily with no signs of overfitting — validation accuracy closely follows training accuracy throughout all epochs.

---

### 🔢 Confusion Matrix 

<div align="center">

<img width="734" height="547" alt="cm" src="https://github.com/user-attachments/assets/d4847d09-8d8b-4efe-9f4a-2f8e7d868182" />

*Each row represents the actual class — each column represents the predicted class.*

</div>

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
