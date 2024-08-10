# Image-Text Analyzer

Welcome to the repository!

## Cloning the Repository

To clone this repository to your local machine, use the following command:

```
git clone https://github.com/ark-lesedium/Image-Text-Analyzer.git
```

## Installation

Ensure you have the following dependencies installed:

- Python 3.x
- TensorFlow
- Pillow
- pygetwindow
- pytesseract

## Usage

Run the script with the following command:

```
python capture.py
```


## Contributing

Feel free to submit issues and pull requests!

---

### Notes:
Here's an explanation of how the code works and its uses:

---

### How the Code Works

1. **Imports and Setup**:
   - `pygetwindow` is used to interact with the active window on your computer.
   - `Pillow` (PIL) is used for capturing screenshots and handling images.
   - `TensorFlow` and `Keras` are used for loading and using a pre-trained VGG16 model.
   - `pytesseract` is used for Optical Character Recognition (OCR) to extract text from images.

2. **Function Definitions**:
   - **`capture_window()`**:
     - Captures a screenshot of the currently active window.
     - Uses `pygetwindow` to get the coordinates of the active window.
     - Uses `Pillow` to capture and save the screenshot as 'current_window.png'.

   - **`analyze_image()`**:
     - Loads the VGG16 model architecture without pre-trained weights initially.
     - Loads the pre-trained weights from a local file.
     - Preprocesses the captured image to fit the input requirements of the VGG16 model.
     - Uses the model to predict the content of the image.
     - Decodes and prints the top 3 predictions, including labels and confidence scores.

   - **`extract_text()`**:
     - Uses `pytesseract` to perform OCR on the captured image.
     - Extracts and prints any text found in the image.

3. **`main()` Function**:
   - Executes the sequence of actions: captures a screenshot, analyzes the image using the VGG16 model, and extracts text from the image.

4. **Script Execution**:
   - When the script is run, the `main()` function is called, performing all the above operations in sequence.

---

### Uses

1. **Image Analysis**:
   - This script is useful for analyzing the content of the currently active window on your desktop. It can identify objects or scenes using the VGG16 model, which is pre-trained on a large dataset of images.

2. **OCR (Optical Character Recognition)**:
   - Extracts text from screenshots. This can be useful for extracting information from documents, reading text from images, or processing data from applications that don’t offer a direct text export feature.

3. **Automation**:
   - Can be used as part of an automation workflow to capture, analyze, and process information from your desktop environment. This can be useful for tasks like monitoring, logging, or data extraction in automated systems.

---

Mind trick: Now you're breathing manually
