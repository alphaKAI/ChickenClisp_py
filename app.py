from Interpreter import Interpreter
from Transpiler import Transpiler
from Engine import Engine
import sys
import os

args = sys.argv[1:]


if len(args) == 1:
  fpath = args[0]

  if not (os.path.exists(fpath)):
    print("No such file - ", fpath)
  else:
    engine = Engine()

    engine.eval(Transpiler.transpile(open(fpath).read()))

elif len(args) == 0:
  itpr = Interpreter()

  itpr.interpreter()
else:
  print("error")