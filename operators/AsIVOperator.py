from expression.ImmediateValue import ImmediateValue
from operators.IOperator import IOperator

class AsIVOperator(IOperator):
    def call(self, engine, args):
      return ImmediateValue(engine.eval(args[0]))