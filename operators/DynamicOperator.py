from operators.IOperator import IOperator

class DynamicOperator(IOperator):
  def __init__(self, funcArgs, funcBody):
    self.funcArgs = funcArgs
    self.funcBody = funcBody

  def call(self, engine, args):
    i = 0
    newEngine = engine.clone()

    for arg in self.funcArgs:
      newEngine.defineVariable(arg, engine.eval(args[i]))
      i += 1

    return newEngine.eval(self.funcBody)