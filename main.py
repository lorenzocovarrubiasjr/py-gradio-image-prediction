import gradio as gr
import requests
import torch
from PIL import Image
from torchvision import transforms


model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()

# Human-readable labels for ImageNet
response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

def predict(input):
    input = transforms.ToTensor()(input).unsqueeze(0)
    with torch.no_grad():
        prediction = torch.nn.functional.softmax(model(input)[0], dim=0)
        confidences = {labels[i]: float(prediction[i]) for i in range(1000)}
    return confidences

gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3),
    examples=["./content/lion.jpg", "./content/cheetah.jpg","./content/armadillo.jpg","./content/bear.jpg","./content/gorilla.jpg"]
).launch()