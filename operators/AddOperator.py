from operators.IOperator import IOperator


class AddOperator(IOperator):
    def call(self, engine, args):
        ret = 0

        for arg in args:
            v = engine.eval(arg)
            ret += v

        return ret
