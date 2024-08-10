<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Window Capture and Analysis Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #eee;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
        a {
            color: #1a0dab;
        }
    </style>
</head>
<body>

    <h1>Window Capture and Analysis Tool</h1>

    <h2>Overview</h2>
    <p>This Python script captures the current active window on your desktop, analyzes the captured image using a pre-trained VGG16 model, and extracts text from the image using OCR (Optical Character Recognition).</p>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>TensorFlow</li>
        <li>Keras</li>
        <li>Pillow (PIL Fork)</li>
        <li>pygetwindow</li>
        <li>pytesseract</li>
        <li>Tesseract-OCR</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li><strong>Clone the repository:</strong>
            <pre><code>git clone https://github.com/yourusername/repository-name.git
cd repository-name</code></pre>
        </li>
        <li><strong>Create and activate a virtual environment:</strong>
            <pre><code>python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`</code></pre>
        </li>
        <li><strong>Install required Python packages:</strong>
            <pre><code>pip install tensorflow pillow pygetwindow pytesseract</code></pre>
        </li>
        <li><strong>Install Tesseract-OCR:</strong>
            <p>Download and install Tesseract-OCR from <a href="https://github.com/tesseract-ocr/tesseract" target="_blank">here</a>. Follow the installation instructions for your operating system.</p>
        </li>
        <li><strong>Update Tesseract Path:</strong>
            <p>Update the <code>tesseract_cmd</code> path in the script to point to the location where Tesseract-OCR is installed on your system.</p>
            <pre><code>pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'</code></pre>
        </li>
        <li><strong>Download VGG16 Weights:</strong>
            <p>Download the VGG16 weights file from <a href="https://github.com/keras-team/keras/blob/v2.9.0/keras/applications/vgg16.py" target="_blank">here</a> and save it to the specified path in the script.</p>
            <pre><code>model.load_weights('C:/Users/<username>/.keras/datasets/vgg16_weights_tf_dim_ordering_tf_kernels.h5')</code></pre>
        </li>
    </ol>

    <h2>Usage</h2>
    <p>Run the script using:</p>
    <pre><code>python capture.py</code></pre>
    <p>The script performs the following tasks:</p>
    <ol>
        <li><strong>Capture the Active Window:</strong> Captures the current active window and saves it as <code>current_window.png</code>.</li>
        <li><strong>Analyze the Image:</strong> Uses the VGG16 model to classify the content of the image. The top 3 predictions are printed to the console.</li>
        <li><strong>Extract Text:</strong> Extracts and prints text from the captured image using OCR.</li>
    </ol>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE" target="_blank">LICENSE</a> file for details.</p>

    <h2>Acknowledgements</h2>
    <ul>
        <li><a href="https://www.tensorflow.org/" target="_blank">TensorFlow</a></li>
        <li><a href="https://keras.io/" target="_blank">Keras</a></li>
        <li><a href="https://python-pillow.org/" target="_blank">Pillow</a></li>
        <li><a href="https://pygetwindow.readthedocs.io/en/latest/" target="_blank">pygetwindow</a></li>
        <li><a href="https://pypi.org/project/pytesseract/" target="_blank">pytesseract</a></li>
        <li><a href="https://github.com/tesseract-ocr/tesseract" target="_blank">Tesseract-OCR</a></li>
    </ul>

</body>
</html>
