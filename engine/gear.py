"""
Provides archetypes and engine with gear classes and functions
"""


class GearSet:
    """
    Container for a full set of gear, may also serve as a base class for
    special gear sets
    """
    def __init__(self, name):
        self.name = name

class ArcaneSet(GearSet):
    """
    Base class for arcane gearsets
    """
    def __init__(self, name):
        super().__init__(name)
        self.arcane_focus = None
        self.hood = None
        self.robe = None
        self.gloves = None

    def __repr__(self) -> str:
        return f"""
        Hood: {self.hood}
        Robe: {self.robe}
        Gloves: {self.gloves}
        Arcane Focus: {self.arcane_focus}
        """
class QuantumGearSet(ArcaneSet):
    """
    Gear set specifically for Quantum
    """

    def __init__(self):
        super().__init__("Quantum Set")

    def __repr__(self) -> str:
        return super().__repr__()
