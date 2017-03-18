from expression.ImmediateValue import ImmediateValue
from operators.IOperator import IOperator

class SetIdxOperator(IOperator):
  def call(self, engine, args):
    if (not (isinstance(args[0], ImmediateValue)) and not isinstance(args[0].value, list)):
      raise ValueError("set-idx requires array")

    arr   = args[0].value
    idx   = args[1]
    value = args[2]

    if (0 < idx and idx < len(arr)):
      arr[idx] = value

      return ImmediateValue(arr)
    else:
      raise ValueError("Invalid")