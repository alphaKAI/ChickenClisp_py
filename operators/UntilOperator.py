from operators.IOperator import IOperator

class UntilOperator(IOperator):
  def call(self, engine, args):
    ret = None

    while not engine.eval(args[0]):
      ret = engine.eval(args[1])

    return ret