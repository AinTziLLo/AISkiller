from random import randint

class CarrierPath:
    def __init__(self, name="[Carrier path name]", modules=None):
        self.modules = []
        self.name = name
        self.modules = modules

    def get_skill_to_evaluate(self):
        skills_list = []
        for i in range(len(self.modules)):
            res = self.modules[i].evaluate()
            if not res:
                skills_list.append(self.modules[i])
            else:
                skills_list.append(self)
        ids_max = randint(0, len(skills_list) - 1)
        return skills_list[ids_max]
