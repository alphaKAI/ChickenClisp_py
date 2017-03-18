from operators.IOperator import IOperator

class IfOperator(IOperator):
  def call(self, engine, args):
    idx = 0

    if engine.eval(args[0]):
      idx = 1
    else:
      idx = 2

    return engine.eval(args[idx])
