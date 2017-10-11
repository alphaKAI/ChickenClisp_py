from operators.IOperator import IOperator


class PrintlnOperator(IOperator):
    def call(self, engine, args):
        for arg in args:
            obj = engine.eval(arg)
            if isinstance(obj, IOperator):
                obj = arg

            if isinstance(obj, list):
                print("(", " ".join(map(lambda x: str(x), obj)), ")", end="")
            else:
                print(obj, end='')

        print("")

        return 0
