# AI Website Generator

## Overview
This is a simple tool that lets you create websites using the Gemini AI model. You can easily generate HTML and CSS code to design and customize your website. Whether you're new to web development or an experienced coder, this tool streamlines the process of building fast, stylish, and efficient websites using AI.

## Features

**Easy to Use**: This app provides a straightforward interface, making it accessible to beginners and experienced developers alike.
**HTML and CSS Generation**: Generate HTML and CSS code effortlessly, eliminating the need to write code from scratch.
**Customization**: Customize your website's design, layout, fonts, and colors to match your preferences and brand identity.

## Requirements
- Python 3
- Gemini API Key [from here](https://aistudio.google.com/app/apikey)
- DSPy

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/tinatissing/ai-website-generator.git
    cd ai-website-generator
    ```
2. Setup Virtual Environment (Alternative to Conda):
    ```
    python -m venv blog_env (name of the virtual environment)
    cd blog_env
    Scripts/Activate (for Windows)
    cd ..
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run the app:
    ```
    python ai-website-generator.py
    ```
5. Add app to Jupyter Kernel:
    ```
    python -m ipykernel install --user --name=blog_env
    ```

## Configuration
- Gemini API Key: Replace YOUR_API_KEY with your Gemini API key.

## Usage
To change the theme of the website, update the website subject.

## Troubleshooting:
If you encounter the following error after ensuring the API Key is working:

`IndexError: list index out of range`

Then you must navigate to: 

`blog_env/lib/pythonXXXX/site-packages/dsp/modules/google.py`

And go to line 160:

`completions.append(response.parts[0].text)`

And replace with the following:

```
try:
    completions.append(response.parts[0].text)
except:
    print("Expected Error")

```

### If the above does not fix it then you may have to keep changing the prompt until it works.
