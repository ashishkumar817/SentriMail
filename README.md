# 🛡️ SentriMail AI-Driven Phishing Email Detection

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-orange?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-Not%20Specified-lightgrey)](#license)

An intelligent email classification system that uses Natural Language Processing and Machine Learning to identify whether an email is **legitimate** or **phishing**.

The project includes data analysis, text preprocessing, TF-IDF feature extraction, model comparison, and an interactive Streamlit web application.

---

## ✨ Key Features

- 🧹 Advanced email text preprocessing
- 🔤 Stop-word removal and lemmatization
- 📊 TF-IDF feature extraction with unigram and bigram support
- 🤖 Comparison of four machine learning models
- 🌲 Random Forest-based phishing detection
- 🖥️ Interactive Streamlit interface
- 📈 Prediction confidence and class probabilities
- 📁 Evaluation charts and model analysis

---

## 📂 Project Structure

```text
AI-Driven-Phishing-Email-Detection/
│
├── 📓 AI- Driven Phishing Email Detection.ipynb
├── 🚀 app.py
├── 📄 phishing_email.csv
├── 🧠 random_forest_phishing_model.pkl
├── 🔤 tfidf_vectorizer.pkl
├── 📦 requirements.txt
└── 📊 results/
    ├── Confusion matrices
    ├── ROC curve
    ├── Precision-recall curve
    ├── Feature importance charts
    └── Model comparison charts
```

---

## 🧾 Dataset

The dataset contains the following columns:

| Column | Description |
|---|---|
| `text_combined` | Email content |
| `label` | Classification label |

### Classification Labels

| Label | Meaning |
|---:|---|
| `0` | ✅ Legitimate email |
| `1` | 🚨 Phishing email |

After preprocessing, the notebook reports **82,077 email records**.

- 🚨 Phishing emails: 52.20%
- ✅ Legitimate emails: 47.80%

---

## ⚙️ Machine Learning Pipeline

```text
📥 Load Dataset
      ↓
🧹 Clean Email Text
      ↓
🔤 Remove Stop Words and Lemmatize
      ↓
📊 Extract TF-IDF Features
      ↓
🤖 Train Classification Models
      ↓
📈 Evaluate Performance
      ↓
💾 Save Best Model
      ↓
🖥️ Deploy with Streamlit
```

---

## 🧠 Models Evaluated

- Logistic Regression
- Multinomial Naive Bayes
- Random Forest
- Neural Network

### 📊 Performance Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 98.01% | 97.83% | 98.37% | 98.10% |
| Multinomial Naive Bayes | 95.23% | 97.90% | 92.86% | 95.31% |
| **Random Forest** | **98.39%** | **98.39%** | **98.52%** | **98.45%** |
| Neural Network | 97.71% | 97.79% | 97.82% | 97.81% |

The **Random Forest classifier** achieved the best overall performance and is used in the deployed application.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd AI-Driven-Phishing-Email-Detection
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages include:

- Streamlit
- Scikit-learn
- Joblib
- NLTK
- BeautifulSoup4
- Pandas
- NumPy

---

## 🚀 Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

Then:

1. Open the local URL provided by Streamlit.
2. Paste an email into the text area.
3. Click **Analyze Email**.
4. View the prediction and confidence score.

### Example Output

```text
🚨 Phishing Email Detected
Confidence: 98.42%
```

or

```text
✅ Legitimate Email
Confidence: 96.18%
```

---

## 📓 Reproduce the Training Process

Open the notebook:

```text
AI- Driven Phishing Email Detection.ipynb
```

The notebook performs:

1. Dataset loading and validation
2. Missing-value and duplicate removal
3. Exploratory data analysis
4. Email text cleaning
5. Feature engineering
6. TF-IDF vectorization
7. Model training
8. Model evaluation
9. Model serialization
10. Visualization generation

---

## 📌 Important Notes

The application requires the following files in the project root:

```text
random_forest_phishing_model.pkl
tfidf_vectorizer.pkl
```

Large files such as the dataset and trained model should be managed with Git LFS:

```bash
git lfs install
git lfs track "phishing_email.csv"
git lfs track "*.pkl"
git add .gitattributes
```

---

## ⚠️ Limitations

- The system analyzes email content only.
- It does not inspect email headers or sender authentication.
- It does not scan attachments or verify live URLs.
- Prediction confidence is an estimate, not a security guarantee.
- The system should support human review and should not replace enterprise security controls.

---

## 🔮 Future Enhancements

- 📧 Direct email inbox integration
- 🔗 URL reputation analysis
- 📎 Attachment scanning
- 🧾 Email header analysis
- 🌐 REST API deployment
- ☁️ Cloud deployment
- 🔐 Explainable AI predictions
- 🗄️ Database-backed prediction history

---

## 📄 License

No license is currently included. Add an appropriate open-source license before publishing the repository.

---

## 👨‍💻 Author

Ashish Kumar

GitHub: @ashishkumar817

Developed as an AI and Machine Learning project for detecting phishing emails using Natural Language Processing.
