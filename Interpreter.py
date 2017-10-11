from Engine import Engine
from Transpiler import Transpiler


class Interpreter:
    def __init__(self):
        self.engine = Engine()
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
                        print(self.engine.eval(
                            Transpiler.transpile(''.join(self.buf))))
                        self.buf = []

                if ('\n' == val or '\r\n' == val):
                    e(val)
                else:
                    self.buf.append(val)
                    e(val)

            for i in list(range(self.bracketState + 1)):
                print("=", end="")

            print("> ", end='')

    def executer(self, code):
        buf = ""
        ret = None

        def e(val, buf, ret):
            if self.checkBracket(val) and len(buf) != 0:
                transpiled = Transpiler.transpile(buf)
                ret = self.engine.eval(transpiled)
                buf = ""
                return [ret, buf]

        for inpt in code.split("\n"):
            if inpt == "exit" or inpt == "(exit)":
                break

            for val in inpt:
                if val == '\n':
                    _ret = e(val, buf, ret)
                    if _ret != None:
                        ret = _ret[0]
                        buf = _ret[1]
                else:
                    buf += val
                    _ret = e(val, buf, ret)
                    if _ret != None:
                        ret = _ret[0]
                        buf = _ret[1]

        return ret
