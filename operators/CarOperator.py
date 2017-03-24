from operators.IOperator import IOperator


class CarOperator(IOperator):
    def call(self, engine, args):
        obj = engine.eval(args[0])

        if isinstance(obj, list):
            if len(obj) > 1:
                return obj[0]
            else:
                raise ValueError("pair required, but got ()")
