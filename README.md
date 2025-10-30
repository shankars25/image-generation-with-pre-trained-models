# Image Generation using Stable Diffusion

###  Prodigy Infotech Internship Task – Task 2
**Author:** shnakar sutar
**Project:** Image Generation with Pre-trained Models  

---

##  Objective

To generate high-quality, realistic images from textual prompts using **Stable Diffusion**, a powerful text-to-image model from the **Hugging Face diffusers** library.

---

##  Project Description

This project demonstrates how to create images using **pre-trained diffusion models**.  
By providing a text prompt, the model generates a visually coherent and detailed image that represents the described scene.  
The implementation leverages **Stable Diffusion v1.5**, one of the most popular open-source text-to-image models available.  

This project is developed as part of **Prodigy Infotech – Task 2** under the internship program.

---

## ⚙️ Key Features

-  Uses **Stable Diffusion (v1.5)** for high-quality image generation  
-  Powered by the **Hugging Face diffusers** library  
-  Supports **GPU acceleration (CUDA)** for faster inference  
-  Automatically saves generated images  
-  Easy to run on **Google Colab** or any local environment with PyTorch support  

---

##  How to Run

1. Open the notebook **`Task_02_Image_Generation.ipynb`** in **Google Colab**.  
2. Install the required libraries using:
   ```bash
   pip install diffusers transformers accelerate safetensors torch
