from Engine import Engine
from Transpiler import Transpiler

class Interpreter:
  def __init__(self):
    self.engine       = Engine()
    self.bracketState = 0

  def checkBracket(self, code):
    for ch in code:
      if ch == "(":
        self.bracketState += 1

      if ch == ")":
        self.bracketState -= 1

      if self.bracketState == 0:
        return True
      else:
        return False


  def interpreter(self):
    self.buf = []

    print("=> ", end="")

    while True:
      for val in input():
        def e(val):
          if (self.checkBracket(val) and (len(self.buf) != 0)):
            print(self.engine.eval(Transpiler.transpile(''.join(self.buf))))
            self.buf = []

        if ('\n' == val or '\r\n' == val):
          e(val)
        else:
          self.buf.append(val)
          e(val)

      for i in list(range(self.bracketState + 1)):
        print("=", end="")

      print("> ", end='')