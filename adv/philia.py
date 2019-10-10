if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv

def module():
    return Philia

class Philia(adv.Adv):
    conf = {}
    a1 = ('a',0.1,'hp100')
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=4
        """
    conf['cond_afflict_res'] = 0

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.paralysis.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.paralysis.resist=100

    def s2_proc(this, e):
        this.afflics.paralysis('s2',90,0.60)


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

