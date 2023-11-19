from random import randint


class CarrierPath:
    def __init__(self, name="[Carrier path name]", modules=None):
        self.name = name
        if modules is None:
            self.modules = []
        else:
            self.modules = modules

    def get_skills_to_evaluate(self):
        """
        Generate a list of skills to evaluate.

        This method returns a list of tuples, each consisting of a module and a sub-skill.
        The sub-skill is randomly selected from each module.

        Returns:
            List[Tuple[Module, str]]: A list of tuples with each tuple containing a module
            and a randomly selected sub-skill.

        Example:
            [('Programming', 'Python'), ('Networking', 'Cloud Computing'),
            ('Data Science', 'Data Driven Mindset'),
            ('Machine Learning', 'Introduction to Machine Learning')]
        """
        skills_list = []
        for module in self.modules:
            skills_list.append((module, module.get_skill_to_evaluate()))
        return skills_list
