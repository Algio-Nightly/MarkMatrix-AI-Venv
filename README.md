# MarkMatrixAI V1.0

## Overview:
- MarkMatrix AI is a Basic Terminal Based Automation which takes  Questions, Answers and Max Marks as an Input in the form of a `.csv` file.
- It Analyses the file using Google Gemini given a fixed prompt.
- After Analyzing the Output is stored in a user-defined file name in the Responses.csv folder
- The Gemini Output gives the following fields by analyzing the file
	- Obtained Marks out of Max Marks Specified
	- Reasoning for Obtained Marks
	- Areas of Improvement




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
