from core.advbase import *
from slot.d import *

def module():
    return Orsem

class Orsem(Adv):
    comment = 'no s2'
    a1 = ('cc',0.10,'hit15')
    a3 = ('cc',0.06,'hp70')
    
    conf = {}
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon(c3-s-end), self.afflics.frostbite.get() or (not self.afflics.frostbite.get() and fsc)
        `s3
        `s4
        `s1
        `fs, x=5
    """
    conf['coabs'] = ['Blade', 'Xander', 'Summer_Estelle']
    conf['share'] = ['Gala_Elisanne', 'Ranzal']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
