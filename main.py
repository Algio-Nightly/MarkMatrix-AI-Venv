from dotenv import load_dotenv
load_dotenv()

import csv
import os

from google import genai
from google.genai import types

class csvModel():
    def __init__(self):
        self.f = open("QuestionList.csv","r")
        pass
    def read_from_csv(self):
        reader = csv.DictReader(self.f)
        return reader
    
    def file_name(self):
        f_name=input("What file should the data be stored in:  ")
        f_name=f_name+".csv"
        return f_name
    def write_data_to_csv(self,file_name,dictionary):
        with open(f"./Responses/{file_name}","w") as write_file:
            writer=csv.writer(write_file)
            writer.writerow(dictionary.keys())
            for iteration in range(5):
                writer.writerow([val[iteration] for val in dictionary.values()])

class AIModel():   
    def get_response(self,prompt):
        api_key = os.getenv("API_KEY")
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are Test Grader which has to grade quiz questions from a csv file. \
                You will be given the Questions Answers(by students) and the max marks of the question that can be given.\
                    The output should be a \"text\" in the form of a python dictionary"),
        contents=[prompt]
    )
        return response.text
    def prompt(self,question):
        prompt=f"Grade this On the Basis of maximum marks \nThe maximum Marks for This Question is \
            {question["max_marks"]} \n Question:{question["question"]}\n Answer:{question["answer"]} \n \n Give The\
                  answer in the form of a python dictionary with the keys 'Question', 'Answer', 'Max Marks',\
                      'Marks Evaluated', 'Areas of Improvement', 'Reasoning for Marks' (The Keys \
                      should be exactly as given here). Give the answer only as Text not a code snippet the \
                        response should contain nothing but a python dictionary remove everything else remove the python\
                            '''from the start and ''' from the end and dont use underscores in the keys of the dictionary"
        return prompt
    

class Control():
    def __init__(self):
        self.ques_list=[]
        self.ans_list=[]
        self.max_marks_list=[]
        self.marks_evaluated_list=[]
        self.area_of_improvement_list=[]
        self.reasoning_for_marks_list=[] 

    def looper(self,ques_file):
            prompt=AI.prompt(question=ques_file)            
            response=AI.get_response(prompt)
            try:
                dict_response=eval(response)
                self.ques_list.append(dict_response["Question"])
                self.ans_list.append(dict_response["Answer"])
                self.max_marks_list.append(dict_response["Max Marks"])
                self.marks_evaluated_list.append(dict_response["Marks Evaluated"])
                if (dict_response["Areas of Improvement"]) is not None:
                    self.area_of_improvement_list.append(dict_response["Areas of Improvement"])
                else:
                    self.area_of_improvement_list.append("None")
                self.reasoning_for_marks_list.append(dict_response["Reasoning for Marks"])
                print("Complete")
            except:
                self.looper(ques_file)
                print("Error")

    def dict_looper(self):
        for ques in CSV.read_from_csv():
            print("Analysing Question no. ",ques['s_no'],end='...')
            self.looper(ques_file=ques)

    def main(self):            
        if input("Do you wanto analyse the file?  ")=="y":
            self.dict_looper()
        self.table_dict={
                'Question': self.ques_list, 
                'Answer': self.ans_list,
                'Max Marks':self.max_marks_list,
                'Marks Obtained':self.marks_evaluated_list,
                'Areas of Improvement':self.area_of_improvement_list,
                'Reasoning for Marks':self.reasoning_for_marks_list
            }
        CSV.write_data_to_csv(CSV.file_name(),self.table_dict)
        
AI = AIModel()
CSV = csvModel()    
Controller = Control()
Controller.main()

CSV.f.close()