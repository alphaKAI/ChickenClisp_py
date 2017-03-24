from operators.IOperator import IOperator


class LengthOperator(IOperator):
    def call(self, engine, args):
        obj = engine.eval(args[0])

        if isinstance(obj, list):
            return len(obj)
        else:
            raise ValueError("Given object is not an Array or List")
