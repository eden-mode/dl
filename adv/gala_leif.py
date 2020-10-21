from core.advbase import ModeManager
from module.template import StanceAdv

def module():
    return Gala_Leif

class Gala_Leif(StanceAdv):        
    def prerun(self):
        self.config_stances({
            'striking': ModeManager(group='striking', x=True, s1=True, s2=True),
            'shielding': ModeManager(group='shielding', x=True, s1=True, s2=True),
        }, hit_threshold=5)

variants = {None: Gala_Leif}
