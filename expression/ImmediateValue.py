class ImmediateValue:
    def __init__(self, value):
        self.value = value

    def eval(self, engine):
        return self.value
