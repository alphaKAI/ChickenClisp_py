from operators.DynamicOperator import DynamicOperator
from operators.IOperator import IOperator


class DeffunOperator(IOperator):
    def call(self, engine, args):
        funcName = engine.eval(args[0])
        funcArgs = args[1]
        funcBody = args[2]

        return engine.defineVariable(funcName, DynamicOperator(funcArgs, funcBody))
