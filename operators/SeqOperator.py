from operators.IOperator import IOperator

class SeqOperator(IOperator):
  def call(self, engine, args):
    n   = args[0]
    return list(range(n))