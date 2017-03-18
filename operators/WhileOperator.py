from operators.IOperator import IOperator

class WhileOperator(IOperator):
  def call(self, engine, args):
    ret = nil

    while engine.eval(args[0]):
      ret = engine.eval(args[1])

    return ret