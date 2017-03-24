class CallOperator:
    def __init__(self, operator, args):
        self.operator = operator
        self.args = args

    def eval(self, engine):
        closure = engine.eval(self.operator)
        return closure.eval(self.args)
