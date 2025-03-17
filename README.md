# 🖼️ Image Classification with ResNet50 – FastAPI Web App

This project is a **FastAPI-powered web application** that allows users to **upload images** and classify them using the **ResNet50 deep learning model** pre-trained on the **ImageNet dataset**. The app processes images, makes **real-time predictions**, and displays the **most likely class** along with its **confidence score**.  

✨ **Upload an image and get instant AI-powered classification!** 🚀  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow"/>
  <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" alt="Keras"/>
  <img src="https://img.shields.io/badge/Uvicorn-FFD43B?style=for-the-badge&logo=python&logoColor=black" alt="Uvicorn"/>
</p>

---

## 🚀 Project Features

### 🧠 **1. Deep Learning Model – ResNet50**
✔ Uses **ResNet50**, a **powerful convolutional neural network (CNN)** pre-trained on **ImageNet**.  
✔ Predicts the **top class** for an uploaded image with a **confidence percentage**.  

### 🌐 **2. FastAPI Web Application**
✔ User-friendly **web interface** where users can upload images.  
✔ **Real-time image processing** and classification powered by FastAPI.  

### 🖼️ **3. Image Preprocessing**
✔ Converts uploaded images into a format suitable for ResNet50.  
✔ **Resizes images to 224×224 pixels**, normalizes input, and prepares data for inference.  

### ☁️ **4. Web-Based Deployment**
✔ Built with **FastAPI** for efficient **backend performance**.  
✔ Uses **Jinja2 templates** for rendering HTML pages dynamically.  
✔ Runs on **Uvicorn**, making it lightweight and scalable.  


## 🏗️ Project Structure

```bash
Image_classifier_ResNet50/
├── 📁 images/              # Sample images 
│   └── 🖼️ [1-2].jpg        # Example images
│
├── 📁 templates/           # Web interface
│   └── 🎨 index.html       # Main template
├── 🐍 main.py              # FastAPI application
│
├── 🐳 Dockerfile           # Container configuration
├── 📛 .dockerignore        # Docker exclusion rules
├── 📛 .gitignore           # Git exclusion rules
└── 📜 requirements.txt     # requirements
```
---

## 🛠️ Technologies Used

| Category            | Tools & Libraries |
|--------------------|------------------|
| **Deep Learning** | `TensorFlow`, `Keras` (ResNet50, ImageNet) |
| **Web Framework** | `FastAPI`, `Jinja2` |
| **Image Processing** | `Pillow (PIL)`, `NumPy` |
| **Deployment** | `Uvicorn` (ASGI server) |

---

## 🏗️ How to Run the Project Locally  

```bash
# Clone repository
git clone https://github.com/marti0001/MNIST-Digit-Classification

# Build Docker image
docker build -t mnist-app .

# Run container
docker run -p 8000:8000 mnist-app
```
