from operators.IOperator import IOperator

class StepOperator(IOperator):
  def call(self, engine, args):
    ret = None

    for arg in args:
      ret = engine.eval(arg)

    return ret