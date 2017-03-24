from operators.IOperator import IOperator


class MulOperator(IOperator):
    def call(self, engine, args):
        ret = 1

        for arg in args:
            v = engine.eval(arg)
            ret *= v

        return ret
