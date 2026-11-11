from fastapi import FastAPI
import uvicorn

klu = FastAPI(title="AI Tutor", 
description="AI Tutor Pbl Project",
version="1.0.0")

@klu.get("/")
def home():
    return {"message": "Welcome to the AI Tutor Project!"}

@klu.get("/demo")
def demo(): 
        return {"message": "KL university"} 

@klu.get("/askquestion")
def ask():
            return {"message": "What is LLM?" ,"Answer": "Large Language Model" }

@klu.get("/student")
def student():
    return {"id":1,"name":"Ram","gender":"male","course":"DSA"}

@klu.get("/students")
def getstudents():
    return[{"id":1,"name":"Ram","gender":"male","course":"DSA"},
           {"id":2,"name":"klu","gender":"male","course":"DSA"},
              {"id":3,"name":"seetha","gender":"female","course":"DSA"}
              ]
if __name__ == "__main__" :
      uvicorn.run("main:klu",host="127.0.0.1",port=2027,reload=True)