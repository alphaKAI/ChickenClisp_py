from operators.IOperator import IOperator


class CondOperator(IOperator):
    def call(self, engine, args):
        for state in args:
            pred = state[0]
            expr = state[1]

            if (engine.eval(pred) or pred == "else"):
                return engine.eval(expr)

        return None
