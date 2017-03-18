class Closure:
  def __init__(self, engine, operator):
    self.engine   = engine
    self.operator = operator

  def eval(self, args):
    return self.operator.call(self.engine, args)