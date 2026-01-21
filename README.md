# ♻️ Garbage Classification Project

## 📌 Overview
This project aims to classify garbage images into predefined categories using machine learning / deep learning techniques. The system helps automate waste sorting and supports efficient recycling and waste management.

---

## 🎯 Objectives
- Classify garbage into multiple categories automatically
- Reduce manual effort in waste segregation
- Improve recycling efficiency using AI-based solutions

---

## 🗂️ Dataset
- **Dataset Source:** (e.g., Kaggle / Custom dataset)
- **Total Images:**
- **Classes:**
 
    - battery
    - biology
    - cardboard
    - clothes
    - glass
    - metal
    - paper
    - plastic
    - shoes
    - trash

- **Image Size:** 299 × 299
- **Data Split:**
  - Training: 70%
  - Validation: 15%
  - Testing: 15%

  
---

## 🧠 Methodology
1. Data preprocessing (resizing, normalization, augmentation)
2. Model selection and architecture design
3. Model training and validation
4. Performance evaluation
5. Prediction on new images


---

## 📊 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to better understand the dataset characteristics, class distribution, and image properties before model training.

### 1. Class Distribution Analysis
- Analyzed the number of images per garbage category
- Identified class imbalance across different waste types
- Helped in deciding data augmentation strategies

<img src="Capture EDA.PNG" width="600"/>



### 2. Sample Visualization
- Visualized random images from each class
- Verified labeling correctness
- Observed visual similarities between classes (e.g., plastic vs glass)

### 3. Image Dimension Analysis
- Checked image height, width, and channels
- Identified varying image sizes
- Standardized all images to **299 × 299** pixels


### 6. Insights from EDA
- Some classes contained fewer samples, causing imbalance
- Data augmentation was required to improve model generalization

---



---

## 🏗️ Model Architecture
- Convolutional Neural Network (CNN)
- Transfer Learning (xception)
- Softmax activation for multi-class classification

---

## ⚙️ Technologies Used
- **Language:** Python
- **Frameworks & Libraries:**
  - TensorFlow / keras
  - NumPy
  - Matplotlib
  - Scikit-learn
- **Tools:** Jupyter Notebook 

---


<img src="Capture EDA.PNG" width="600"/>

## 🚀 Installation & Setup
Clone the repository and install dependencies:

```bash
git clone https://github.com/YohanaTeweldemedhin/Garbage_Classification
cd garbage-classification
pip install -r requirements.txt














