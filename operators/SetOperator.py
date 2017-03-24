from operators.IOperator import IOperator


class SetOperator(IOperator):
    def call(self, engine, args):
        return engine.setVariable(args[0], engine.eval(args[1]))
