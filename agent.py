from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

model = LiteLlm(
    model="groq/llama-3.3-70b-versatile",  
)
resume_parser_agent = Agent(
    name="Resume_Parser",
    model=model,
    description="Resume Parser Agent is responsible to analyze the candidate's resume.",
    instruction=("1.Check whether the resume is in .txt format or not.\n"
    "2.If it is in .pdf format convert it into .txt format.\n"
    "3.Check all details carefully.\n"
    "4.Check all skills,experience,profile and contact details.\n"
    "5.Display all details.\n"
    "6.Identify the domain and display it.\n"
    "7.If you did not observe experience consider it as Fresher."
)
)
question_generator_agent = Agent(
    name="Question_Generator",
    model=model,
    description="Questoion Generator is responsible for generating questions depending upon candidate's resume.",
    instruction=("1.Know about domain from the resume_parser_agent.\n"
    "2.Need to generate questions one after the another.\n"
    "3.Need to generate question after recieving the answer from candidate.\n"
    "4.Need to generate 5 questions based on responses of the candidate.\n"
    "5.Questions should be based on responses of the candidate and difficulty.\n"
    "6.Display every question."
)
)

interview_agent = Agent(
    name="Interview_Agent",
    model=model,
    description="Interview Agent is responsible for taking interview to the candidate.",
    instruction=("1.Listen greetings of the candidate.\n"
    "2.Examine the resume from the resume_parser_agent.\n"
    "3.Ask only one clear question which is generated from the question_generator and wait for the response from candidate and then ask next question.\n"    "4.Don't ask all questions at a time without getting answers from the candidate.\n"
    "4.Every answer should be relevant to your question\n."
    "5.Don't move to next question until you receive relevant answer.\n"
    "6.Observe the answers and responses from the candidate and then select."
)
)
evaluate_agent = Agent(
    name="Evaluate_Agent",
    model=model,
    description="Evaluate Agent is responsible for evaluating answers from the candidate.",
    instruction=("1.Need to remember every single question and answer.\n"
    "2.Need to manage a chat conversation.\n"
    "3.Need to give explaination and better solution for each and every question and answer.\n"
    "4.Express correct answers and also give explaination why it is correct.\n"
    "5.Exptress wrong answers and also give explaination why it is wrong.\n"
    "6.Finally give suggestions and better solutions for next interview."
)
)

feedback_agent = Agent(
    name="Feedback_Agent",
    model=model,
    description="Feedback Agent is responsible for giving feedbacks to the candidates.",
    instruction=("1.Need to give feedback for each and every question and answer.\n"
    "2.Need to give explaination for feedback given.\n"
    "3.Need to have overall feedback.\n"
    "4.It should be present in percentage form."
)
)
root_agent = Agent(
    name="my_agent",
    model=model,
    description="Mock Technical Interview Agent.",
    instruction=("You are the root orchestrator for a mock technical interview system.\n"
        "Coordinate the following agents in order:\n"
        "1. resume_parser_agent   - Parse and validate the candidate's resume.\n"
        "2. question_generating_agent - Generate questions based on resume and skills.\n"
        "3. interview_agent       - Conduct the mock interview with the candidate.\n"
        "4. evaluate_agent        - Evaluate the interview questions and candidate answers.\n"
        "5. feedback_agent        - Provide overall feedback and performance percentage.\n\n"
        "Project dependencies (from requirements.txt):\n"
),
    sub_agents=[
        resume_parser_agent,
        question_generator_agent,
        interview_agent,
        evaluate_agent,
        feedback_agent
    ],
)
