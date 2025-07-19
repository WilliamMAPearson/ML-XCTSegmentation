# ML-XCT Segmentation

This project provides tools for XCT (X-ray Computed Tomography) segmentation aimed at tracking the evolution of corrosion growth on the sides of metal samples. This method is designed to perform effective segmentation of corrosion growth in XCT scans using only a single training image.

## Overview

This project implements a pretrained model combined with data augmentation techniques to enhance the training process. After training, the model can accurately segment additional images, enabling detailed tracking of corrosion evolution with minimal annotated data. This method allows a user to automatically segment complex XCT datasets with very limited training material.

## Project Example
During the corrosion process, various features can appear on the metal surface, including corrosion scale (redeposited material) and hydrogen bubbles. By tracking and analyzing the growth and evolution of these features over time using XCT segmentation, researchers can gain a deeper understanding of the corrosion system and its progression. This XCT data is often captured at very small spatial resolutions and, in some cases, in real time. This high-resolution and rapid acquisition can introduce significant noise and artifacts into the images, making accurate segmentation challenging. The presence of noise complicates the identification of product boundaries, requiring robust segmentation methods capable of handling imperfect data. 

### The Project
The below segmentation shows the aim of this project. The image on the left shows products growing on the metal surface during a corrosion process, the metal is the bright circular shape, the blobs on the surface are the product of the corrosion process, the outer circular ring is an artefact of the XCT recontruction algorithm, and the black background in the corners is absence of any data. The right image shows the ultimate aim of segmenting and clustering the indiviudal blobs, where each color represents an individual product of interest, the size over time is what is of interest.
<p align="center">
  <img src="https://github.com/WilliamMAPearson/ML-XCTSegmentaion/blob/main/ML-XCT/Description/images/Aim of Segmentation.png" width="500">
</p>

The next image shows the affect of applying traditional segmentation algorithms to the original image. The top row shows the original image next to attempts to segment the image using global thresholding, otsu thresholding, and K-means clustering techniques. The bottom row shows the ground truth overlaid on the original image and shows what the aim of the segmentation is, the other images on the bottom row show the segmentations overlaid on the original image. They show that they lack in both their ability to segment only the blobs but also splitting the unique blobs.
<p align="center">
  <img src="https://github.com/WilliamMAPearson/ML-XCTSegmentaion/blob/main/ML-XCT/Description/images/Segmentaion_Of_Example_Image.png" width="500">
</p>

The aim of this project then, is to provide a more robust method of segmentation, this will be done in two steps, segmenting out all the blobs followed by clustering to seperate the blobs. As can be seen in the next image, once the blobs have been segmented, splitting into unique blobs is trivial.
<p align="center">
  <img src="https://github.com/WilliamMAPearson/ML-XCTSegmentaion/blob/main/ML-XCT/Description/images/Clustering_A_Segmented_Image.png" width="500">
</p>



---

## Setup Instructions

This guide explains how to set up and run this project using a virtual environment and the provided `requirements.txt` file.

---

## 1. Check Python Version

This project works with python 3.13

## 2. Create Virtual Environment

Run the following in your terminal **from the root of the repo**:

```sh
python -m venv .venv
```

## 3. Activate Virtual Environment 

Run the following in your terminal **from the root of the repo**:

```sh
.venv\Scripts\activate
```

## 4. Ensure pip is up to date

Run the following in the terminal:

```sh
python.exe -m pip install --upgrade pip
```

## 5. Install Dependancies

Run the following in the terminal:

```sh
pip install -r requirements.txt
```

## 6. Run Test Files

Run the following in the terminal:

```sh
python main.py
```

## 7. Deactivate the Virtual Environment

Run the following in the terminal:

```sh
deactivate
```

## Exmaple

```sh
# Clone the repo
git clone https://github.com/your-username/your-repo.git
cd your-repo

# Create and activate venv
python -m venv .venv
source .venv/bin/activate

# Install packages
pip install -r requirements.txt

# Run the app
python main.py
```


## 99. Notes

Automatically Add Pakcages to Requirements, from within the virtual environment:

```sh
pip freeze > requirements.txt
```