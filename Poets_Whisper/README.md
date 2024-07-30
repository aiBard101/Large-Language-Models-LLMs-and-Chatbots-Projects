# Poetry Generator with FastAPI and GoogleAI

Welcome to the Poetry Generator project! This application leverages Large Language Models (LLMs) to create beautiful, personalized poems based on user input. The backend is built with FastAPI, and the GoogleAI library is used to harness the power of generative AI.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This project demonstrates how to build a web-based poetry generator using FastAPI and the Google Generative AI model. Users can input a word or phrase, and the application will generate a poem along with a loading message. The frontend is designed to be user-friendly, providing an engaging experience.

## Features

- **Poetry Generation**: Generate poems based on user input using AI.
- **Loading Animation**: Displays a loading message while the poem is being generated.
- **Responsive Design**: The web application is designed to be responsive and visually appealing.
- **User-Friendly Interface**: Simple input field and intuitive interaction.

## Installation

To get started with the Poetry Generator, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/aiBard101/Large-Language-Models-LLMs-and-Chatbots-Projects/Poets_Whisper.git
   cd Poets_Whisper
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes the necessary libraries such as FastAPI and langchain_google_genai.

5. **Set Up Environment Variables**

   Create a `.env` file in the root directory of the project and add your Google API key:

   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

6. **Run the Application**

   ```bash
   uvicorn main:app --reload
   ```

   Open your browser and go to `http://127.0.0.1:8000` to see the Poetry Generator in action.

## Usage

1. **Enter a Word or Phrase**: Input a word or phrase in the text field and click the send button.
2. **View Loading Message**: A loading animation and message will be displayed while the poem is being generated.
3. **Read the Poem**: Once generated, the poem will appear on the screen along with its title.
4. **Try Again**: If you want to generate another poem, click the "Try Again" button to reset the application.

## Project Structure

```
poetry-generator/
├── main.py                # FastAPI application
├── app.py          # GoogleAI class
├── static/
│   ├── styles.css        # CSS for styling
│   └── script.js         # JavaScript for interactivity
└── templates/
    └── index.html        # HTML for the frontend
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, please follow these steps:

1. **Fork the Repository**
2. **Create a New Branch**
3. **Make Your Changes**
4. **Submit a Pull Request**

Please ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact:

- **Email**: [aibard.annonymousasquare@gmail.com](aibard.annonymousasquare@gmail.com)
- **GitHub**: [aiBard](https://github.com/aiBard101/)
- **X**: [aiBard001](https://x.com/aiBard001)
- **LinkedIn**: [aiBard](https://www.linkedin.com/in/george-junior-alainengiya-5b44b5251/)
- **WhatsApp**: [aiBard](https://%20https://wa.me/message/AL5IJZCUYD6LG1)
Visit my Website[Website](https://aibard.code.blog/).

---
Watch the [YouTube video](https://youtu.be/4bnG9TnrOag) demonstrating the application.

