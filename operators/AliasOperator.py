from operators.IOperator import IOperator

class AliasOperator(IOperator):
    def call(self, engine, args):
        new  = args[0]
        base = args[1]

        v = engine.variables[base]

        if v is not None:
          engine.variables[new] = v

        return v