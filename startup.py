import gradio as gr
import random
from AISkiller import AISkiller
from conf import *

ai_skiller = AISkiller()

with gr.Blocks(theme=gr.themes.Soft(font=[gr.themes.GoogleFont("Roboto"), "Roboto", "Arial", "sans-serif"]), css="""footer{display:none !important}""") as demo:
    gr.Image("dm.jpg", width=36, show_download_button=False, min_width=36, show_label=False)
    gr.Markdown("""# AI-Skiller Demo
Certifica le tue skill.""")

    with gr.Tab("Come funziona?"):
        with gr.Column():
            gr.Markdown("""Il processo di certificazione delle tue Skill è semplice e veloce, segui questi 2 step:
            * inserisci il nome della professione per cui valutare le tue skill e il numero massimo di domande a cui vuoi rispondere nel tab "SETUP";
            * rispondi alle domande proposte dal sistema in modo corretto, completo e conciso;
                
            Lorem ipsum...""")

    with gr.Tab("Setup"):
        with gr.Column():
            student_tbox = gr.Textbox(label='Nominativo:', placeholder='Roberta Bianchi', info="Nome / nickname")
            profession_tbox = gr.Textbox(label='Professione:', placeholder='Python Backend Developer', info="Nome della professione da valutare")
            questions_number_slider = gr.Slider(
                label="n° max domande",
                info="Seleziona un numero massimo di domande tra 6 e 20",
                value=6,
                minimum=6,
                maximum=20,
                step=1
            )
            setup_btn = gr.Button("Conferma (e attendi circa 10 secondi...)")

    chatbot_tab = gr.Tab("SkillBot")
    with chatbot_tab:
        not_ready = gr.Column()
        with not_ready:
            not_ready_text = gr.Markdown("""## Attenzione
            
            devi configurare SkillBot nel **tab SETUP** per accedere alle domande...""")

        skillb = gr.Column(visible=False)
        with skillb:
            chatbot = gr.Chatbot()
            msg = gr.Textbox(placeholder="(inserisci qui le tue risposte)", label="")

            def respond(message, chat_history):
                result = ai_skiller.step(answer=message)
                print(result)
                bot_message = ai_skiller.step()
                if bot_message is not None:
                    chat_history.append((message, bot_message))
                else:
                    chat_history.append((message, 'Ti ringrazio per le tue risposte. Questa sessione è terminata. Ricarica questa pagina per avviare una nuova sessione!'))
                    msg.visible = False
                return "", chat_history

            msg.submit(respond, [msg, chatbot], [msg, chatbot])


    def random_student():
        return random.choice([
            'Mario Rossi',
            'Luigi Bianchi',
            'Roberta Verdi',
            'Luca Neri'
        ])

    def random_profession():
        return random.choice([
            'Data Scientist',
            'Data Analyst',
            'Machine Learning Specialist',
            'Python Developer',
            'AI Researcher',
            'Data Architect',
            'AI Product Manager'
        ])

    def check_setup(student, profession, questions_number):
        if len(profession) < 6:
            profession = random_profession()
        if len(student) < 6:
            student = random_student()
        ai_skiller.setup(
            profession=profession,
            student=student,
            questions_number=int(questions_number / 2),
            fake_data=False,
            verbose=False
        )
        next_question = ai_skiller.step()
        return {
            not_ready: gr.Column(visible=False),
            setup_btn: gr.Button(visible=False),
            skillb: gr.Column(visible=True),
            profession_tbox: gr.Textbox(interactive=False, value=profession),
            student_tbox: gr.Textbox(interactive=False, value=student),
            questions_number_slider: gr.Slider(interactive=False),
            chatbot: gr.Chatbot([[None, "Ciao, sono qui per valutare le tue competenze per la professione di " + profession + ". Partiamo subito con la prima domanda:"], [None, next_question]]),
        }

    setup_btn.click(
        check_setup,
        [student_tbox, profession_tbox, questions_number_slider],
        [not_ready, skillb, profession_tbox, student_tbox, questions_number_slider, chatbot, setup_btn],
    )

demo.launch(show_api=False, auth=(login, password), server_name=server_name, server_port=server_port, share=True)

"""
skill specifiche
    domande simili non uguali
    domande randomm (no ripetute)
"""