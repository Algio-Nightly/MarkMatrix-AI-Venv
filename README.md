# MarkMatrixAI V1.0

## Overview:
MarkMatrix AI is a **terminal-based automation tool** that evaluates answers using the **Google Gemini API**.  
It takes **questions, answers, and maximum marks** from a `.csv` file, analyzes them with a fixed AI prompt, and saves the evaluation results in the **`Responses`** folder.  

---

## ✨ Features
- ✅ Automated answer evaluation  
- ✅ AI-powered marking with Google Gemini  
- ✅ CSV input and structured output  
- ✅ Includes reasoning and improvement suggestions  
- ✅ Simple retry mechanism for failed AI responses  

---

## 📌 Output Fields
After analysis, Gemini provides:
- **Obtained Marks** (out of the specified maximum marks)  
- **Reasoning** for the awarded marks  
- **Areas for Improvement**  

---

## 📂 Project Structure
MarkMatrix-AI/
│── main.py
│── requirements.txt
│── .env.example
│── QuestionList.csv
│── Responses/ # Output folder
└── .gitignore




## Instructions:
1. Install `.venv` environment
2. Make an Output Folder called "Responses" -- All the Output Files will be stored in this folder
3. Make a `.env` file according to the `.env.example` file
4. Put your `Google Gemini API Key` in the `.env` file
5. There is a Demo Question List in the file `QuestionList.csv`, It can be Changed As Needed to as many question but the format must stay the same.
6. Run the file `main.py`.
7. Type y to run the file and Analyze the `QuestionList.csv` file.
8. It will take a few seconds to some minutes to Analyze the file and produce an output.
9. The Terminal might say 'Error' sometimes. This is because AI model sometimes dont give the desired output. This isn't a cause for concern as the same question will be put back for evaluation immediately and automatically.
10. After the evaluation, you need to input a file name into the terminal (without extension) to save the response.
---
