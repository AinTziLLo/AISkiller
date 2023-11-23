from skill import Skill

SKILL_MY_SQL = Skill(name="MySQL", sub_skills=[],
                     descr="creation, management, querying, and optimization of MySQL databases")

SKILL_PostgreSQL = Skill(name="PostgreSQL", sub_skills=[],
                         descr="creation, management, querying, and optimization of PostgreSQL databases")

SKILL_RelationalDatabases = Skill(name="Relational Databases", sub_skills=[
    SKILL_MY_SQL,
    SKILL_PostgreSQL
])

SKILL_DBDesign = Skill(name="DB Design", sub_skills=[],
                       descr="knowledge of designing, managing, and querying relational databases, using languages like SQL to manipulate and efficiently retrieve data")

SKILL_ConcurrentProgramming = Skill(name="Concurrent Programming", sub_skills=[],
                                    descr="ability to develop software capable of executing multiple processes or threads simultaneously, optimizing resource use and improving performance, especially in multi-core systems, also through the use of libraries like NumPy, Pandas, Polars, etc.")

SKILL_FunctionalProgramming = Skill(name="Functional Programming", sub_skills=[],
                                    descr="development style based on pure functions, immutability, lambda expressions, and recursion")

SKILL_OOPProgramming = Skill(name="Object-Oriented Programming", sub_skills=[],
                             descr="software development based on classes, encapsulation, inheritance, polymorphism, and abstraction")

SKILL_ProceduralProgramming = Skill(name="Procedural Programming", sub_skills=[],
                                    descr="software development based on procedures/functions, sequentiality, modularity, and reusable code")

SKILL_Python = Skill(name="Python", sub_skills=[],
                     descr="development with Python language: versatile, simple, object-oriented, and with extensive external library support")

SKILL_Programming = Skill(name="Programming", sub_skills=[
    SKILL_ProceduralProgramming,
    SKILL_OOPProgramming,
    SKILL_FunctionalProgramming,
    SKILL_ConcurrentProgramming,
    SKILL_DBDesign,
    SKILL_RelationalDatabases,
    SKILL_Python
], descr="creation of software through coding, with logic, algorithms, and specific languages")

SKILL_IntroToCloudComputing = Skill(name="Introduction to Cloud Computing", sub_skills=[],
                                    descr="basic concepts of Cloud Computing, such as IaaS, PaaS, SaaS")

SKILL_CloudComputing = Skill(name="Cloud Computing", sub_skills=[
    SKILL_IntroToCloudComputing
], descr="management of IT resources on the internet, scalability, remote access, and subscription-based services")

SKILL_Networks = Skill(name="Networks", sub_skills=[
    SKILL_CloudComputing
], descr="study and management of connectivity, protocols, architecture, and security of computer networks.")

SKILL_DataDrivenMindset = Skill(name="Data Driven Mindset", sub_skills=[],
                                descr="making decisions based on analysis and interpretation of data, promoting innovation")

SKILL_DataScience = Skill(name="Data Science", sub_skills=[
    SKILL_DataDrivenMindset
], descr="analysis and interpretation of complex data, using statistics, machine learning, and data visualization")

SKILL_IntroAndDefinitionToMachineLearning = Skill(name="Introduction to Machine Learning", sub_skills=[],
                                                  descr="fundamentals of learning algorithms, models, data analysis, and practical applications")

SKILL_MachineLearning = Skill(name="Machine Learning", sub_skills=[
    SKILL_IntroAndDefinitionToMachineLearning
], descr="development of algorithms that learn from data to make predictions or decisions")
