from operators.IOperator import IOperator
from Closure import Closure


class RemoveOperator(IOperator):
    def call(self, engine, args):
        efunc = engine.eval(args[0])
        eargs1 = engine.eval(args[1])
        ret = []

        for elem in eargs1:
            cnd = false

            if isinstance(efunc, Closure):
                cnd = efunc.eval([elem])
            else:
                cnd = efunc.call(engine, [elem])

            if not cnd:
                ret.append(elem)

        return ret
