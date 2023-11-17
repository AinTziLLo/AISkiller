import random

class Skill:
    def __init__(self, name="skill name", descr="skill description", sub_skills=None):
        self.name = name
        self.descr = descr
        if sub_skills:
            self.sub_skills = sub_skills
        else:
            self.sub_skills = []
        self.score = 0

    def evaluated(self):
        return True if self.score > 0 else False

    def evaluate(self, value=None):
        if value:
            self.score = value
        else:
            if self.evaluated():
                return self.score
            sub_skills_number = len(self.sub_skills)
            if sub_skills_number > 0:
                total_score = 0
                skills_list = []
                for i in range(sub_skills_number):
                    if self.sub_skills[i].evaluate():
                        total_score += self.sub_skills[i].score
                    else:
                        skills_list.append(self.sub_skills[i])
                if len(skills_list) == 0:
                    self.score = int(total_score / sub_skills_number)
                    return self.score
                else:
                    res = random.choice(skills_list)
                    return res
            else:
                return self