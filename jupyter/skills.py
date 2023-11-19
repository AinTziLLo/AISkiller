from skill import Skill

SKILL_MY_SQL = Skill(name="MySQL", sub_skills=[],
                     descr="creazione, gestione, interrogazione e ottimizzazione di database MySQL")

SKILL_PostgreSQL = Skill(name="PostgreSQL", sub_skills=[],
                         descr="creazione, gestione, interrogazione e ottimizzazione di database PostgreSQL")

SKILL_BasiDiDatiRelazionali = Skill(name="Basi di Dati Relazionali", sub_skills=[
    SKILL_MY_SQL,
    SKILL_PostgreSQL
])

SKILL_ProgettazioneDiDB = Skill(name="Progettazione di DB", sub_skills=[],
                                descr="conoscenza della progettazione, gestione e interrogazione di database strutturati in modo relazionale, utilizzando linguaggi come SQL per manipolare e recuperare dati in modo efficiente")

SKILL_ProgrammazioneConcorrente = Skill(name="Programmazione Concorrente", sub_skills=[],
                                        descr="capacità di sviluppare software in grado di eseguire più processi o thread simultaneamente, ottimizzando l'uso delle risorse e migliorando le prestazioni, specialmente in sistemi multi-core, anche tramite l'utilizzo di librerie come NumPy, Pandas, Polars, ecc.")

SKILL_ProgrammazioneFunzionale = Skill(name="Programmazione Funzionale", sub_skills=[],
                                       descr="stile di sviluppo basato su funzioni pure, immutabilità, espressioni lambda e ricorsione")

SKILL_ProgrammazioneOOP = Skill(name="Programmazione ad Oggetti", sub_skills=[],
                                descr="sviluppo software basato su classi, incapsulamento, ereditarietà, polimorfismo e astrazione")

SKILL_ProgrammazioneProcedurale = Skill(name="Programmazione Procedurale", sub_skills=[],
                                        descr="sviluppo software basato su procedure/funzioni, sequenzialità, modularità e codice riutilizzabile")

SKILL_Python = Skill(name="Python", sub_skills=[],
                     descr="sviluppo con linguaggio Python: versatile, semplice, orientato agli oggetti e con ampio supporto di librerie esterne")

SKILL_Programmazione = Skill(name="Programmazione", sub_skills=[
    SKILL_ProgrammazioneProcedurale,
    SKILL_ProgrammazioneOOP,
    SKILL_ProgrammazioneFunzionale,
    SKILL_ProgrammazioneConcorrente,
    SKILL_ProgettazioneDiDB,
    SKILL_BasiDiDatiRelazionali,
    SKILL_Python
], descr="creazione di software tramite codice, con logica, algoritmi e linguaggi specifici")

SKILL_IntroduzioneAlCloudComputing = Skill(name="Introduzione al Cloud Computing", sub_skills=[],
                                           descr="concetti di base del Cloud Computing, come IaaS, PaaS, SaaS")

SKILL_CloudComputing = Skill(name="Cloud Computing", sub_skills=[
    SKILL_IntroduzioneAlCloudComputing
], descr="gestione di risorse IT su internet, scalabilità, accesso remoto e servizi basati su abbonamento")

SKILL_Reti = Skill(name="Reti", sub_skills=[
    SKILL_CloudComputing
], descr="studio e gestione della connettività, protocolli, architettura e sicurezza delle reti informatiche.")

SKILL_DataDrivenMindset = Skill(name="Data Driven Mindset", sub_skills=[],
                                descr="prendere decisioni basate su analisi e interpretazione di dati, promuovendo l'innovazione")

SKILL_DataScience = Skill(name="Data Science", sub_skills=[
    SKILL_DataDrivenMindset
], descr="analisi e interpretazione di dati complessi, usando statistica, machine learning e visualizzazione dati")

SKILL_IntroEDefinizioneAlMachineLearning = Skill(name="Introduzione al Machine Learning", sub_skills=[],
                                                 descr="fondamenti di algoritmi di apprendimento, modelli, analisi dati e applicazioni pratiche")

SKILL_MachineLearning = Skill(name="Machine Learning", sub_skills=[
    SKILL_IntroEDefinizioneAlMachineLearning
], descr="sviluppo di algoritmi che apprendono da dati per fare previsioni o decisioni")
