from operators.DynamicOperator import DynamicOperator
from expression.ImmediateValue import ImmediateValue
from operators.IOperator import IOperator

class LetOperator(IOperator):
  def call(self, engine, args):
    if (not isinstance(args[0], list)):
      name  = args[0]
      binds = args[1]
      body  = args[2]
      _engine = engine.clone()

      names = []
      vars_ = []

      for bind in binds:
        name = bind[0]
        val  = bind[1]
        names.append(name)
        vars_.append(val)

      _engine.defineVariable(name, DynamicOperator(names, body))
      ret = _engine.getVariable(name).call(_engine, vars_)

      if ret is None:
        return 0
      else:
        return ret

    else:
      binds   = args[0]
      body    = args[1]
      _engine = engine.clone()

      for bind in binds:
        name = bind[0]
        val  = engine.eval(bind[1])

        _engine.defineVariable(name, val)

      _engine.eval(body)