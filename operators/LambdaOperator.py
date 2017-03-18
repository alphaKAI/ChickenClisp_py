from operators.DynamicOperator import DynamicOperator
from operators.IOperator import IOperator


class LambdaOperator(IOperator):
  def call(self, engine, args):
    funcArgs = args[0]
    funcBody = args[1]

    return DynamicOperator(funcArgs, funcBody)