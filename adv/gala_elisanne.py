from core.advbase import *


class Gala_Elisanne(Adv):
    def prerun(self):
        self.s2.autocharge_init(960).on()


class Gala_Elisanne_70MC(Gala_Elisanne):
    SAVE_VARIANT = False
    comment = "70MC"
    conf = {
        "c": {
            "name": "Gala Elisanne",
            "icon": "100002_13_r05",
            "att": 618,
            "hp": 893,
            "ele": "water",
            "wt": "axe",
            "spiral": True,
            "a": [
                ["resself_burn_att", 0.15, 10.0, 15.0],
                ["resself_stun_att", 0.15, 10.0, 15.0],
                ["affres_burn", 100.0],
                ["affres_stun", 100.0],
                ["primed_att", 0.15],
            ],
        },
        "s1": {
            "sp": 4377,
            "startup": 0.1,
            "recovery": 1.23333,
            "attr": [
                {"buff": [["team", 1.2, 15.0, "heal", "buff"], ["ele", 0.15, 15.0, "att", "buff", "water"]], "coei": 1, "iv": 0.5},
                {"buff": ["ele", 0.15, 15.0, "att", "buff", "water"], "iv": 0.5},
            ],
            "energizable": True,
        },
        "s2": {
            "sp": 38400,
            "startup": 0.1,
            "recovery": 2.06667,
            "attr": [{"dmg": 13.75, "iv": 0.2}, {"dmg": 13.75, "iv": 0.53333}, {"dmg": 13.75, "iv": 1.43333}, {"buff": ["energy", 3], "iv": 1.43333}],
        },
    }


variants = {None: Gala_Elisanne, "70MC": Gala_Elisanne_70MC}
