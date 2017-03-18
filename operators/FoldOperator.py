from expression.ImmediateValue import ImmediateValue
from operators.IOperator import IOperator
from Closure import Closure

class FoldOperator(IOperator):
  def call(self, engine, args):
    func  = args[0]
    tmp   = args[1]
    eargs = engine.eval(args[2])

    if isinstance(eargs, list):
      array = eargs
      efunc = engine.eval(func)

      if isinstance(efunc, Closure):
        for elem in array:
          tmp = efunc.eval([tmp, elem])
      elif isinstance(efunc, Operator):
        for elem in array:
          tmp = efunc.call(engine, [tmp, elem])

      return tmp
    else:
      if (not (isinstance(eargs, ImmediateValue)) and not (isinstance(eargs, list))):
        raise ValueError("Map requires array and function as a Operator")

      array = eargs.value
      efunc = engine.eval(func)

      if isinstance(efunc, Closure):
        for elem in array:
          tmp = efunc.eval([tmp, elem])
      else:
        for elem in array:
          tmp = efunc.call(engine, [tmp, elem])

      return tmp