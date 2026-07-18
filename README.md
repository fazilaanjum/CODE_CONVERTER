# 💻 AI Programming Language Converter

An AI-powered web application that converts source code from one programming language to another using **Google Gemini AI** and **Gradio**.

## 🚀 Features

- Convert code between multiple programming languages
- Powered by Google Gemini 2.5 Flash
- Simple and interactive Gradio interface
- Preserves the original program logic
- Generates clean and readable code
- Supports multiple popular programming languages

## 🛠️ Technologies Used

- Python
- Google Gemini AI (`google-genai`)
- Gradio

## 📂 Supported Languages

- Python
- Java
- C
- C++
- JavaScript
- C#
- Go
- PHP

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-programming-language-converter.git
cd ai-programming-language-converter
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Gemini API Key

#### Windows (Command Prompt)

```cmd
set GEMINI_API_KEY=YOUR_API_KEY
```

#### Windows (PowerShell)

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

#### Linux / macOS

```bash
export GEMINI_API_KEY=YOUR_API_KEY
```

### 4. Run the application

```bash
python app.py
```

The application will start and display a local Gradio URL in your terminal.

## 📸 How to Use

1. Select the **Source Language**.
2. Select the **Target Language**.
3. Paste your source code.
4. Click **Submit**.
5. View the converted code.

## 📁 Project Structure

```
AI-Programming-Language-Converter/
│── app.py
│── requirements.txt
│── README.md
```

## ⚠️ Security

Never upload your Gemini API key to GitHub.

Use an environment variable instead:

```
GEMINI_API_KEY=YOUR_API_KEY
```

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome. Feel free to fork this repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Developed using **Python**, **Gradio**, and **Google Gemini AI**.
