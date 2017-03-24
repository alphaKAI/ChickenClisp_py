from operators.IOperator import IOperator


class PrintOperator(IOperator):
    def call(self, engine, args):
        for arg in args:
            print(arg, end='')

        return 0
