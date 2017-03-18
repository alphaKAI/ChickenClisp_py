from operators.IOperator import IOperator

class DefvarOperator(IOperator):
  def call(self, engine, args):
    return engine.defineVariable(args[0], engine.eval(args[1]))