from expression.ImmediateValue import ImmediateValue
from operators.IOperator import IOperator
from Closure import Closure


class MapOperator(IOperator):
    def call(self, engine, args):
        func = args[0]
        eargs1 = engine.eval(args[1])

        if isinstance(eargs1, list):
            array = eargs1
            ret = []
            efunc = engine.eval(func)

            if isinstance(efunc, Closure):
                for elem in array:
                    ret.append(efunc.eval([elem]))
            else:
                for elem in array:
                    ret.append(efunc.call(engine, [elem]))

            return ret
        else:
            if (not (isinstance(eargs1, ImmediateValue)) and not isinstance(eargs1.value, list)):
                raise ValueError(
                    "Map requires array and function as a Operator")

            array = eargs1.value
            ret = []
            efunc = engine.eval(func)

            if isinstance(efunc, Closure):
                for elem in array:
                    ret.append(efunc.eval([elem]))
            else:
                for elem in array:
                    ret.append(efunc.call(engine, [elem]))

            return ret
