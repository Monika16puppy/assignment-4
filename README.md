# Bird vs Drone Detection using Deep Learning

## Project Overview

This project focuses on classifying aerial images as either birds or drones using deep learning techniques.
The system was developed using a Custom CNN model and an EfficientNetB0 transfer learning model.
A web application was also built using Streamlit for real-time image prediction.

---

## Objectives

- Detect and classify birds and drones from aerial images
- Compare the performance of deep learning models
- Build a real-time prediction system using Streamlit
- Evaluate model performance using multiple metrics

---

## Models Used

### 1. Custom CNN
A Convolutional Neural Network (CNN) model was developed for binary image classification.

### 2. EfficientNetB0
Transfer learning was implemented using the EfficientNetB0 pretrained model for improved accuracy and better feature extraction.

---

## Technologies Used

- Python
- TensorFlow / Keras
- Streamlit
- NumPy

---

## Dataset

The dataset contains aerial images belonging to two classes:

- Bird
- Drone

The dataset was divided into:
- Training set
- Validation set
- Testing set

Due to GitHub file size limitations, the dataset is not uploaded to this repository.

---

## Data Preprocessing

The following preprocessing techniques were applied:

- Image resizing (224 × 224)
- Data augmentation
- Image normalization
- Rotation
- Zooming
- Horizontal flipping

---

## Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score

---

## Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|------|------|------|------|------|
| Custom CNN | 80.46% | 80.46% | 80.46% | 80.21% |
| EfficientNetB0 | 97.67% | 97.67% | 97.67% | 97.67% |

The EfficientNetB0 model achieved significantly better performance compared to the Custom CNN model.

---

## Streamlit Web Application

A Streamlit-based web application was developed to allow users to:

- Upload aerial images
- Predict whether the image contains a bird or drone
- Display prediction confidence

---

## Project Structure

```plaintext
bird-drone-detection/
│
├── dataset/
├── models/
├── notebooks/
├── streamlit_app/
├── images/
├── reports/
├── README.md
```

---

---

## Results

The EfficientNetB0 transfer learning model outperformed the Custom CNN model in all evaluation metrics and achieved high classification accuracy on unseen test data.

---

## Future Improvements

- Real-time video detection
- YOLOv8 object detection
- Cloud deployment
- Larger aerial image datasets
- Real-time surveillance integration

---

## Conclusion

This project demonstrates the effectiveness of deep learning and transfer learning techniques for aerial object classification.
The EfficientNetB0 model achieved excellent performance and the Streamlit application provided a simple interface for real-time predictions.

