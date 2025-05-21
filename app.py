import os
import base64
import tensorflow as tf
from flask import Flask, request, render_template

# Import functions from the newly created functions.py
from functions import decode_batch_predictions

# Load the model
model_path = 'captcha_model.h5'
prediction_model = tf.keras.models.load_model(model_path, compile=False)

# Image dimensions
img_width = 200
img_height = 50

# Flask app configuration
app = Flask(__name__, template_folder='templates')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB file limit

def recognize_captcha(image_path):
    """Recognize captcha text from an image using the loaded model."""
    try:
        # Load and preprocess the image
        img = tf.io.read_file(image_path)
        img = tf.io.decode_png(img, channels=1)  # Ensure it's grayscale
        img = tf.image.convert_image_dtype(img, tf.float32)  # Normalize to [0, 1]
        img = tf.image.resize(img, [img_height, img_width])  # Resize to correct dimensions
        img = tf.transpose(img, perm=[1, 0, 2])  # Transpose for HWC to CHW format

        # Create a batch with a single image
        batch_images = tf.convert_to_tensor([img])

        # Make predictions using the loaded model
        preds = prediction_model.predict(batch_images)

        # Decode the predictions into text
        decoded_text = decode_batch_predictions(preds)

        # Return recognized text (removing unknown characters)
        return decoded_text[0].replace("[UNK]", "")
    except Exception as e:
        print(f"Error recognizing captcha: {e}")
        return ''

@app.route('/', methods=['GET', 'POST'])
def solve():
    """Handle captcha file uploads and solve them using the model."""
    rc = None
    encoded_image = None
    error_message = None

    if request.method == 'POST':
        file = request.files['file']

        if file.filename == '':
            error_message = "No file uploaded. Please upload an image."
            return render_template('captcha.html', error_message=error_message)

        image_data = file.read()
        encoded_image = base64.b64encode(image_data).decode('utf-8')

        # Save the uploaded file
        directory = "user_uploads"
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, file.filename)

        file.seek(0)
        file.save(file_path)

        # Recognize captcha
        rc = recognize_captcha(file_path)

        if rc == '':
            error_message = "Captcha could not be recognized."
            return render_template('captcha.html', error_message=error_message)

    return render_template('captcha.html', rc=rc, encoded_image=encoded_image, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
