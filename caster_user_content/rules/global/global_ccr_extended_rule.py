from dragonfly import MappingRule, ShortIntegerRef, Repeat, Pause

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.actions import Key
from castervoice.lib.merge.state.short import R
from castervoice.lib.merge.mergerule import MergeRule
from castervoice.lib.const import CCRType

class GlobalCCRExtendedRule(MergeRule):

    pronunciation = "global ccr extended"

    mapping = {
        "flash": R(Key("f2")),
        "go back [<n>]": R(Key("a-left:%(n)d")),
        "[system | sys] tray": R(Key("w-b")),
        "scratch [<n101>]": R(Key("c-backspace:%(n101)d")),
        "dear [<n101>]": R(Key("c-del:%(n101)d")),
        "snap window one":
            R(Key("w-up") +
            Pause("40") + Key("w-left") +
            Pause("40") + Key("w-left") +
            Pause("40") + Key("escape") +
            Pause("40") + Key("a-tab") +
            Pause("80") + Key("w-up")),
        "snap window two":
            R(Key("w-up") +
            Pause("40") + Key("w-right") +
            Pause("40") + Key("w-right") +
            Pause("40") + Key("escape") +
            Pause("40") + Key("a-tab") +
            Pause("80") + Key("w-up")),
        "snap window three":
            R(Key("w-up") +
            Pause("40") + Key("w-left") +
            Pause("40") + Key("w-left") +
            Pause("40") + Key("escape") +
            Pause("40") + Key("a-tab") +
            Pause("80") + Key("w-down")),
        "snap window four":
            R(Key("w-up") +
            Pause("40") + Key("w-right") +
            Pause("40") + Key("w-right") +
            Pause("40") + Key("escape") +
            Pause("40") + Key("a-tab") +
            Pause("80") + Key("w-down")),
    }
    extras = [
        ShortIntegerRef("n", 1, 10),
        ShortIntegerRef("n101", 1, 101),
    ]
    defaults = {
        "n": 1,
        "n101": 1
    }

def get_rule():
    details = RuleDetails(ccrtype=CCRType.GLOBAL)
    return GlobalCCRExtendedRule, details
