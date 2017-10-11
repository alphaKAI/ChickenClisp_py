from expression.ImmediateValue import ImmediateValue
from expression.CallOperator import CallOperator
from expression.IExpression import IExpression
from operators.IOperator import IOperator
from Closure import Closure

from operators.AddOperator import AddOperator
from operators.SubOperator import SubOperator
from operators.MulOperator import MulOperator
from operators.DivOperator import DivOperator
from operators.ModOperator import ModOperator
from operators.EqualOperator import EqualOperator, NotEqualOperator, LessOperator, GreatOperator, LEqOperator, GEqOperator
from operators.IOperator import IOperator
from operators.GetOperator import GetOperator
from operators.SetOperator import SetOperator
from operators.StepOperator import StepOperator
from operators.UntilOperator import UntilOperator
from operators.IfOperator import IfOperator
from operators.LogicOperator import NotOperator, AndOperator, OrOperator
from operators.PrintOperator import PrintOperator
from operators.PrintlnOperator import PrintlnOperator
from operators.DeffunOperator import DeffunOperator
from operators.WhileOperator import WhileOperator
from operators.GetfunOperator import GetfunOperator
from operators.DynamicOperator import DynamicOperator
from operators.LambdaOperator import LambdaOperator
from operators.MapOperator import MapOperator
from operators.SetIdxOperator import SetIdxOperator
from operators.AsIVOperator import AsIVOperator
from operators.DefvarOperator import DefvarOperator
from operators.SeqOperator import SeqOperator
from operators.FoldOperator import FoldOperator
from operators.LengthOperator import LengthOperator
from operators.CarOperator import CarOperator
from operators.CdrOperator import CdrOperator
from operators.LoadOperator import LoadOperator
from operators.CondOperator import CondOperator
from operators.AliasOperator import AliasOperator
from operators.ConsOperator import ConsOperator
from operators.ForeachOperator import ForeachOperator
from operators.LetOperator import LetOperator
from operators.WhenOperator import WhenOperator
from operators.IsListOperator import IsListOperator
from operators.RemoveOperator import RemoveOperator


class Engine:
    def __init__(self):
        self.variables = {}

        self.variables["+"] = AddOperator()
        self.variables["-"] = SubOperator()
        self.variables["*"] = MulOperator()
        self.variables["/"] = DivOperator()
        self.variables["%"] = ModOperator()
        self.variables["="] = EqualOperator()
        self.variables["<"] = LessOperator()
        self.variables[">"] = GreatOperator()
        self.variables["<="] = LEqOperator()
        self.variables[">="] = GEqOperator()
        self.variables["set"] = SetOperator()
        self.variables["get"] = GetOperator()
        self.variables["until"] = UntilOperator()
        self.variables["step"] = StepOperator()
        self.variables["if"] = IfOperator()
        self.variables["!"] = NotOperator()
        self.variables["not"] = self.variables["!"]
        self.variables["&&"] = AndOperator()
        self.variables["and"] = self.variables["&&"]
        self.variables["||"] = OrOperator()
        self.variables["or"] = self.variables["||"]
        self.variables["print"] = PrintOperator()
        self.variables["println"] = PrintlnOperator()
        self.variables["def"] = DeffunOperator()
        self.variables["while"] = WhileOperator()
        self.variables["get-fun"] = GetfunOperator()
        self.variables["lambda"] = LambdaOperator()
        self.variables["map"] = MapOperator()
        self.variables["set-idx"] = SetIdxOperator()
        self.variables["as-iv"] = AsIVOperator()
        self.variables["def-var"] = DefvarOperator()
        self.variables["seq"] = SeqOperator()
        self.variables["fold"] = FoldOperator()
        self.variables["length"] = LengthOperator()
        self.variables["car"] = CarOperator()
        self.variables["cdr"] = CdrOperator()
        self.variables["load"] = LoadOperator()
        self.variables["cond"] = CondOperator()
        self.variables["alias"] = AliasOperator()
        self.variables["cons"] = ConsOperator()
        self.variables["for-each"] = ForeachOperator()
        self.variables["let"] = LetOperator()
        self.variables["when"] = WhenOperator()
        self.variables["list?"] = IsListOperator()
        self.variables["remove"] = RemoveOperator()

        self.super_ = None

    def clone(self):
        newEngine = Engine()
        newEngine.super_ = self

        for key, value in self.variables.items():
            newEngine.variables[key] = value

        return newEngine

    def defineVariable(self, name, value):
        self.variables[name] = value

        return value

    def setVariable(self, name, value):
        engine = self

        while True:
            if name in engine.variables:
                engine.variables[name] = value

                return value
            elif engine.super_ is not None:
                engine = engine.super_
            else:
                return engine.defineVariable(name, value)

    def getVariable(self, name):
        engine = self

        while True:
            if name in self.variables:
                return self.variables[name]
            elif engine.super_ is not None:
                engine = engine.super_
            else:
                return None

    def eval(self, script):
        ret = self.getExpression(script)

        if isinstance(ret, IOperator):
            return ret

        ret = ret.eval(self)

        if isinstance(ret, IOperator):
            return Closure(self, ret)
        else:
            return ret

    def getExpression(self, script):
        if isinstance(script, ImmediateValue):
            return script

        if isinstance(script, list):
            if isinstance(script[0], list):
                ret = CallOperator(self.variables[script[0][0]], script[0][1:])
                tmp = ret.eval(self)

                if isinstance(tmp, Closure):
                    return ImmediateValue(tmp.eval(script[1:]))
                elif isinstance(tmp, IOperator):
                    return ImmediateValue(tmp.call(self, script[1:]))

            return CallOperator(self.variables[script[0]], script[1:])
        else:
            tmp = self.getVariable(script)

            if tmp is not None:
                if isinstance(tmp, IOperator):
                    return tmp
                else:
                    return ImmediateValue(tmp)

            return ImmediateValue(script)
