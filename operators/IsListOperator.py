from operators.IOperator import IOperator


class IsListOperator(IOperator):
    def call(self, engine, args):
        return isinstance(engine.eval(args[0]), list)
