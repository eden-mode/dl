from core.advbase import *
from core.acl import CONTINUE
from module.template import SigilAdv
import random

S2_AFFS = {
    "poison": (110, 0.436),
    "burn": (110, 0.727),
    "flashburn": (110, 0.31),
    "stormlash": (110, 0.31),
    "shadowblight": (110, 0.31),
    "scorchrend": (110, 0.31),
    "paralysis": (110, 0.727),
}


class Regina(SigilAdv):
    comment = "expected value s2 affliction"

    def prerun(self):
        self.config_sigil(duration=300)
        self._protocol = 0
        self.sigil_listeners = [
            Listener("aff_relief", lambda e: self.a_update_sigil(-30)),
            Listener("fs_end", self.check_protocol, order=0),
            Listener("repeat", self.check_protocol, order=0),
        ]

    def s1_proc(self, e):
        self.a_update_sigil(-9)

    def s2_hit1(self, *args):
        name, dtype = args[0], args[4]
        for aff, affargs in S2_AFFS.items():
            getattr(self.afflics, aff).on(name, *affargs, dtype=dtype, very_speshul_regina_number=2/len(S2_AFFS))

    def check_protocol(self, e):
        fs_action = self.action.getdoing()
        if not isinstance(fs_action, Fs):
            fs_action = self.action.getprev()
        if isinstance(fs_action, Repeat):
            fs_action = fs_action.parent
        fs_elapsed = now() - fs_action.startup_start - fs_action.last_buffer + 0.0001  # float shenanigans
        if fs_elapsed > 1.5:
            self._protocol = (self._protocol + 1) % 3

    @property
    def preservation_protocol(self):
        return int(self._protocol == 0 or self.unlocked)

    @property
    def restoration_protocol(self):
        return int(self._protocol == 1 or self.unlocked)

    @property
    def purification_protocol(self):
        return int(self._protocol == 2 or self.unlocked)


class Regina_RNG(Regina):
    comment = "random s2 affliction"

    def s2_hit1(self, *args):
        name, dtype = args[0], args[4]
        for aff, affargs in random.sample(S2_AFFS.items(), 2):
            getattr(self.afflics, aff).on(name, *affargs, dtype=dtype)


class Regina_UNLOCKED(Regina):
    SAVE_VARIANT = False

    def prerun(self):
        super().prerun()
        self.a_update_sigil(-300)


variants = {None: Regina, "RNG": Regina_RNG, "UNLOCKED": Regina_UNLOCKED}
