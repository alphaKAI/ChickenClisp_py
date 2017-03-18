from operators.IOperator import IOperator

class NotOperator(IOperator):
  def call(self, engine, args):
    return not engine.eval(args[0])

class AndOperator(IOperator):
  def call(self, engine, args):
    return engine.eval(args[0]) and engine.eval(args[1])

class OrOperator(IOperator):
  def call(self, engine, args):
    return engine.eval(args[0]) or engine.eval(args[1])