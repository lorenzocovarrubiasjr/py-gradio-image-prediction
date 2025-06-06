# Image Classification with ResNet18 and Gradio
This project demonstrates a simple image classification application using a pre-trained ResNet18 model from PyTorch, with a user-friendly interface built using Gradio. The model classifies images into one of the 1,000 ImageNet classes, displaying the top three predicted classes along with their confidence scores.

## Features

- Uses a pre-trained ResNet18 model for image classification.
- Fetches human-readable ImageNet labels from a remote source.
- Provides a web-based interface via Gradio for uploading and classifying images.
- Includes example images for quick testing.

## Prerequisites
To run this project, ensure you have the following installed:

Python 3.7+
PyTorch (torch and torchvision)
Gradio
PIL (Pillow)
Requests

You can install the required dependencies using pip:
```bash
pip install torch torchvision gradio pillow requests
```

## Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```


2. Ensure the example images (lion.jpg, cheetah.jpg, armadillo.jpg, bear.jpg, gorilla.jpg) are placed in the ./content/ directory, or provide your own images for testing.

3. Run the script to launch the Gradio interface:
```bash
python main.py
```

## Usage

- After running the script, a Gradio interface will launch in your default web browser.
- Upload an image or select one of the provided example images.
- The interface will display the top three predicted classes with their confidence scores.

## Code Overview

- Model: Loads a pre-trained ResNet18 model from PyTorch's model hub and sets it to evaluation mode.
- Labels: Fetches ImageNet class labels from a remote URL for human-readable output.
- Prediction Function: Processes the input image, applies necessary transformations, and uses the model to predict class probabilities.
- Gradio Interface: Creates a web interface for uploading images and displaying predictions.

## File Structure
```plain 
<repository-directory>/
├── content/            # Directory for example images
│   ├── lion.jpg
│   ├── cheetah.jpg
│   ├── armadillo.jpg
│   ├── bear.jpg
│   └── gorilla.jpg
├── main.py              # Main script containing the code
└── README.md           # This file
```

## Limitations

The model is pre-trained on ImageNet, so it is limited to the 1,000 classes in the ImageNet dataset.
Internet access is required to fetch the ImageNet labels during the first run.
The Gradio interface runs locally by default; for public access, additional configuration is needed (e.g., setting share=True in gr.Interface.launch()).

### Acknowledgments

PyTorch for the pre-trained ResNet18 model.
Gradio for the easy-to-use interface.
ImageNet for the dataset and labels.

