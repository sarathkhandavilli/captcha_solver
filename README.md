# CAPTCHA Solver

A Flask-based web application that uses machine learning to solve CAPTCHA images. This project is a simple web-based CAPTCHA solver built with Flask (Python web framework). Users can upload a CAPTCHA image through a web interface.

## Features

- Upload CAPTCHA images
- Real-time CAPTCHA recognition
- Modern UI with Tailwind CSS
- Copy recognized text to clipboard

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **ML**: TensorFlow/Keras
- **Deployment**: Netlify

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/sarathkhandavilli/captcha_solver.git
cd captcha_solver
```

2. Create and activate virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

## Usage

1. Open your browser and navigate to `http://localhost:5000`
2. Upload a CAPTCHA image
3. The application will process the image and display the recognized text
4. Click the "Copy" button to copy the recognized text to clipboard

## License

MIT License 
