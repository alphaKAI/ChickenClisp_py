from operators.IOperator import IOperator

class WhenOperator(IOperator):
  def call(self, engine, args):
    if engine.eval(args[0]):
      ret = None

      for arg in args[1:]:
        ret = engine.eval(arg)

      return ret
    else:
      return None