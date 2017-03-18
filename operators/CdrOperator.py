from operators.IOperator import IOperator

class CdrOperator(IOperator):
  def call(self, engine, args):
    obj = engine.eval(args[0])

    if isinstance(obj, list):
      if len(obj) == 1:
        return []
      elif len(obj) > 1:
        return obj[1:]
      else:
        raise ValueError("pair required, but got ()")