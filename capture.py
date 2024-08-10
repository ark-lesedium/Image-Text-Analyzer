import pygetwindow as gw
from PIL import Image, ImageGrab
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions
import pytesseract

# Update this path to your Tesseract installation
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_window():
    """Captures the current active window."""
    active_window = gw.getActiveWindow()
    if active_window:
        bbox = (active_window.left, active_window.top, active_window.right, active_window.bottom)
        screenshot = ImageGrab.grab(bbox)
        screenshot.save('current_window.png')

def analyze_image():
    """Analyzes the captured image using a pre-trained model."""
    # Load pre-trained model with weights from a local file
    model = VGG16(weights=None, include_top=True)  # Define model architecture
    model.load_weights('C:/Users/Lesedi Skosana/.keras/datasets/vgg16_weights_tf_dim_ordering_tf_kernels.h5')  # Load weights from your local file

    # Load and preprocess the image
    img = image.load_img('current_window.png', target_size=(224, 224))
    x = image.img_to_array(img)
    x = preprocess_input(x)
    x = tf.expand_dims(x, axis=0)

    # Predict
    predictions = model.predict(x)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # Print top 3 predictions
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        print(f"{i + 1}: {label} ({score:.2f})")

def extract_text():
    """Extracts text from the captured image using OCR."""
    img = Image.open('current_window.png')
    text = pytesseract.image_to_string(img)
    print("Extracted text:", text)

def main():
    capture_window()
    analyze_image()
    extract_text()

if __name__ == "__main__":
    main()
