from operators.IOperator import IOperator


class ConsOperator(IOperator):
    def call(self, engine, args):
        car = engine.eval(args[0])
        cdr = engine.eval(args[1])

        ret = [car]

        if isinstance(cdr, list):
            for elem in cdr:
                ret.append(engine.eval(elem))
        else:
            ret.append(cdr)

        return ret
