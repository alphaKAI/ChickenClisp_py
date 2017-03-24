from operators.IOperator import IOperator
from Transpiler import Transpiler
import os


class LoadOperator(IOperator):
    def call(self, engine, args):
        loaded = []
        eargs0 = engine.eval(args[0])

        if isinstance(eargs0, list):
            args = eargs0

        fpaths = list(map(lambda arg: engine.eval(arg) + ".ore", args))

        for fpath in fpaths:
            if not os.path.exists(fpath):
                raise FileExistsError("No such file - " + fpath)
            else:
                engine.eval(Transpiler.transpile(open(fpath).read()))
                loaded.append(fpath)

        return loaded
