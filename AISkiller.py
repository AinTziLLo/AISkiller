import os
import re
import openai
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.output_parsers import CommaSeparatedListOutputParser, PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.pydantic_v1 import BaseModel, Field


class AISkiller:
    def setup(self, profession="Machine Learning Engineer", student="Mario Rossi", questions_number=3, verbose=True,
              fake_data=False):
        # ---
        class StepInfo(BaseModel):
            ai_evaluation: str = Field(description="evaluation of the Student's answer")
            score: str = Field(description="score of the Student's answer")
            finished: bool = Field(
                description="if the answer provided is sufficient for an objective evaluation of the student's skills")

        self.step_info_parser = PydanticOutputParser(pydantic_object=StepInfo)

        openai.api_key = os.getenv("openai_key")

        self.open_ai_model = OpenAI(temperature=0., openai_api_key=os.getenv("openai_key"), max_tokens=512)
        self.chat_open_ai_model = ChatOpenAI(temperature=0., openai_api_key=os.getenv("openai_key"), max_tokens=512)

        self.comma_separated_list_output_parser = CommaSeparatedListOutputParser()
        self.comma_separated_format_instructions = self.comma_separated_list_output_parser.get_format_instructions()
        # ---
        self.questions_number = questions_number
        self.student = student
        self.verbose = verbose
        self.retry_question = False

        if fake_data:
            self.profession = "Frontend Developer"
            self.field = "Web Development"
            self.skills = ['HTML/CSS', 'JavaScript', 'Responsive Design.']
            self.q_a = [
                {
                    'skill': 'HTML/CSS',
                    'question': 'What is the purpose of the "z-index" property in CSS?',
                    'ai_reference': 'The purpose of the "z-index" property in CSS is to specify the stack order of an element, relative to other elements on the same page. It is used to control the overlapping of elements on the page, with higher values indicating higher priority.',
                    'answer': None,
                    'score': None,
                    'evaluation': None
                },
                {
                    'skill': 'JavaScript',
                    'question': 'What is the difference between a function expression and a function declaration in JavaScript?',
                    'ai_reference': 'A function expression is a function that is assigned to a variable, whereas a function declaration is a function that is declared with the function keyword.',
                    'answer': None,
                    'score': None,
                    'evaluation': None
                },
                {
                    'skill': 'Responsive Design.',
                    'question': 'What is the difference between a mobile-first and a desktop-first approach to Responsive Design?',
                    'ai_reference': 'The main difference between a mobile-first and a desktop-first approach to Responsive Design is that the mobile-first approach prioritizes the design of the mobile version of the website, while the desktop-first approach prioritizes the design of the desktop version of the website.',
                    'answer': None,
                    'score': None,
                    'evaluation': None
                }
            ]
        else:
            self.profession = profession
            self.profession = self.translate(profession)
            self.field = self.get_field()
            self.skills = self.get_skills()
            self.q_a = []
            self.get_questions()

        if self.verbose:
            print("-" * 9, "init", "-" * 9)
            print("skills related to a " + self.profession + " in the field of " + self.field + ":")
            for i, s in enumerate(self.skills):
                print("\n", s, "\nQ:", self.q_a[i]["question"], "- A:", self.q_a[i]["ai_reference"])
            print("-" * 24, "\n")

    def get_field(self):
        return self.chat_open_ai_model([
            SystemMessage(
                content="You are a bot specialized in finding the scope of a particular profession in one short sentence"),
            HumanMessage(content="Data Scientist"),
            AIMessage(content="Data Science"),
            HumanMessage(content="carpenter"),
            AIMessage(content="industry"),
            HumanMessage(content="teacher"),
            AIMessage(content="instruction"),
            HumanMessage(content="Lawyer"),
            AIMessage(content="Law"),
            HumanMessage(content="employee"),
            AIMessage(content="work"),
            HumanMessage(content="Carpenter"),
            AIMessage(content="Industry"),
            HumanMessage(content="nurse"),
            AIMessage(content="medicine"),
            HumanMessage(content="operator"),
            AIMessage(content="operator"),
            HumanMessage(content=self.profession)
        ]).content

    def translate(self, message, to_eng=True):
        if to_eng:
            language_from = "italian"
            language_to = "english"
        else:
            language_from = "english"
            language_to = "italian"
        try:
            result = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-1106",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert translator from " + language_from + " to " + language_to + " with experience in texts related to the " + self.profession + " profession.\nTranslate the user input into " + language_to + "."
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                temperature=0,
                max_tokens=1024,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            ).choices[-1].message.content
        except:
            result = ".:ERR:."
        return result

    def get_skills(self):
        prompt = PromptTemplate(
            template="""Act as an expert recruiter in the field of {field}.
Identify and list the top {selected_skills_number} skills a {profession} should have.
The selected skills must be easily measurable in a short interview.

{format_instructions}""",
            input_variables=["field", "top_skills_number", "profession"],
            partial_variables={"format_instructions": self.comma_separated_format_instructions}
        )

        output = self.open_ai_model(
            prompt.format(field=self.field, profession=self.profession, selected_skills_number=self.questions_number))
        return [re.sub(r"^\n?\d+\.\s+", "", x) for x in self.comma_separated_list_output_parser.parse(output)]

    def get_question(self, skill):
        llm = OpenAI(temperature=0.33, openai_api_key=openai.api_key, max_tokens=512)
        new_question_prompt = PromptTemplate(
            template="""Act like an expert {field} teacher who has taught a course that delves into {skill}.
    Generate a question on a theoretical {skill} topic in the form of a short, formal text; the question must be in such a form as to require a very short answer and to allow an unambiguous evaluation; only those who have a profound knowledge of the {skill} should be able to answer this question correctly and completely. Don't add comments of any kind, just write the question.""",
            input_variables=["field", "skill"]
        )
        ai_answer_prompt = PromptTemplate(
            template="""Act like an expert {field} teacher who has taught a course that delves into {skill}.
    Reply to the question \"\"\"{question}\"\"\"
    The answer must be in the form of a short, formal text; the answer must be a short, correct and complete answer. Don't add comments of any kind, just write the answer.""",
            input_variables=["field", "skill", "question"]
        )
        question = llm(new_question_prompt.format(field=self.field, skill=skill)).strip()
        return {
            "skill": skill,
            "question": question,
            "ai_reference": llm(ai_answer_prompt.format(field=self.field, skill=skill, question=question)).strip(),
            "answer": None,
            "eng_answer": None,
            "score": None,
            "evaluation": None,
            "finished": None
        }

    def get_questions(self):
        for skill in self.skills:
            self.q_a.append(self.get_question(skill))

    def get_next_question(self):
        idx = 0
        question_found = False
        question = None
        ai_reference = None
        skill_analyzed = None
        while not question_found and idx < len(self.q_a):
            q_a = self.q_a[idx]
            if not q_a["score"]:
                question_found = True
                question = q_a["question"]
                ai_reference = q_a["ai_reference"]
                skill_analyzed = q_a["skill"]
            else:
                idx += 1
        return question, ai_reference, skill_analyzed, idx

    def step(self, answer=None):
        question, ai_reference, skill_analyzed, q_a_idx = self.get_next_question()
        if not question:
            return None
        else:
            if not answer:
                return self.translate(question, to_eng=False)
            else:
                eng_answer = self.translate(answer)
                prompt = PromptTemplate(
                    template="Follow these steps to answer the user queries.\n\nStep 1 - First analyze the question and the AI-Assistant answer. Don't rely on the Student's answer since it may be incorrect.\n\nStep 2 - Compare the AI-Assistant answer to the Student's answer and evaluate the Student's answer in detail, explaining how the response can be improved.\n\nStep 3 - Score the Student's answer compared to the AI-Assistant's answer on a scale from 1 to 5.\n\n{format_instructions}\n\n{query}\n",
                    input_variables=["query"],
                    partial_variables={"format_instructions": self.step_info_parser.get_format_instructions()},
                )
                prompt_and_model = prompt | self.open_ai_model
                result = self.step_info_parser.invoke(prompt_and_model.invoke({
                                                                                  "query": "Question: \"\"\"" + question + "\"\"\"\n\nAI-Assistant answer: \"\"\"" + ai_reference + "\"\"\"\n\nStudent answer: \"\"\"" + eng_answer + "\"\"\""}))
                self.q_a[q_a_idx]["answer"] = answer
                self.q_a[q_a_idx]["eng_answer"] = eng_answer
                self.q_a[q_a_idx]["score"] = result.score
                self.q_a[q_a_idx]["evaluation"] = result.ai_evaluation
                self.q_a[q_a_idx]["finished"] = result.finished
                if not result.finished:
                    if not self.retry_question:
                        self.q_a.insert(q_a_idx + 1, self.get_question(self.q_a[q_a_idx]["skill"]))
                        self.retry_question = True
                    else:
                        self.retry_question = False
                return self.q_a[q_a_idx]