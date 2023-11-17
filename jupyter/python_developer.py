from python_developer_skills import *
from carrier_path import CarrierPath

class PythonDeveloperCP(CarrierPath):
    def __init__(self):
        super(PythonDeveloperCP, self).__init__(modules = [
            SKILL_Programmazione,
            SKILL_Reti,
            SKILL_DataScience,
            SKILL_MachineLearning
        ])