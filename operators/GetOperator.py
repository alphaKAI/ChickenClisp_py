from operators.IOperator import IOperator

class GetOperator(IOperator):
  def call(self, engine, args):
    return engine.getVariable(args[0])