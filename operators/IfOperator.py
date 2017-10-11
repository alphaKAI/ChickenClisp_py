from operators.IOperator import IOperator


class IfOperator(IOperator):
    def call(self, engine, args):
        ret = None

        if engine.eval(args[0]):
            ret = engine.eval(args[1])
        else:
            if len(args) != 3:
                ret = None
            else:
                ret = engine.eval(args[2])

        return ret
