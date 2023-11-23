from skills_eng import *
from carrier_path import CarrierPath


class PythonDeveloperCP(CarrierPath):
    """
    Python Developer Carrier-path
    """

    def __init__(self):
        super(PythonDeveloperCP, self).__init__(
            name="Python Developer",
            modules=[
                SKILL_Programming,
                SKILL_Networks,
                SKILL_DataScience,
                SKILL_MachineLearning
            ])
