from operators.IOperator import IOperator

class GetfunOperator(IOperator):
  def call(self, engine, args):
    return engine.variables[engine.eval(args[0])]