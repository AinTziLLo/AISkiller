import numpy as np


class Skill:
    def __init__(self, name="skill name", descr="skill description", sub_skills=None):
        self.name = name
        self.descr = descr
        self.sub_skills = sub_skills if sub_skills else []
        self.score = 0
        self.ai_comment = ""
        self.evaluated = False

    def get_skill_to_evaluate(self):
        """
        Returns a sub-skill to evaluate
        chosen from the skills still to evaluate; if there aren't
        the skill is chosen on a probability distribution
        based on the exponential inverse of the score of each skill
        if there are no sub-skills, the skill itself is returned
        """
        not_evaluated_skills = [skill for skill in self.sub_skills if not skill.evaluated]
        if not_evaluated_skills:
            return np.random.choice(not_evaluated_skills)
        if self.sub_skills:
            inverted_scores = [max(skill.score for skill in self.sub_skills) - skill.score + 1 for skill in
                               self.sub_skills]
            exponential_scores = np.exp(inverted_scores)
            return np.random.choice(self.sub_skills, p=exponential_scores / np.sum(exponential_scores))
        return self
