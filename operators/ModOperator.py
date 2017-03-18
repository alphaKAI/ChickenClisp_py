from operators.IOperator import IOperator

class ModOperator(IOperator):
  def call(self, engine, args):
    ret = engine.eval(args[0])

    for arg in args[1:]:
      v = engine.eval(arg)
      ret %= v

    return ret