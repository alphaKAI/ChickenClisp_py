from operators.IOperator import IOperator

class EqualOperator(IOperator):
  def call(self, engine, args):
    return engine.eval(args[0]) == engine.eval(args[1])

class NotEqualOperator(IOperator):
  def call(self, engine, args):
    return engine.eval(args[0]) != engine.eval(args[1])

class LessOperator(IOperator):
  def call(self, engine, args):
    return engine.eval(args[0]) < engine.eval(args[1])

class GreatOperator(IOperator):
  def call(self, engine, args):
    return engine.eval(args[0]) > engine.eval(args[1])

class LEqOperator(IOperator):
  def call(self, engine, args):
    return engine.eval(args[0]) <= engine.eval(args[1])

class GEqOperator(IOperator):
  def call(self, engine, args):
    return engine.eval(args[0]) >= engine.eval(args[1])