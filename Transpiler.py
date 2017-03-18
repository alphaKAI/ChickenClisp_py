# -*- coding: utf-8 -*-
from Parser import Parser
import re

comment_rgx = re.compile(".*;.*")
newline_rgx = re.compile("\n")

class Transpiler:
    """
    Transpiler
    """
    @staticmethod
    def transpile(code):
        """
        trasnpile
        """
        fst = re.sub(comment_rgx, "", code)
        snd = re.sub(newline_rgx, "", fst)
        return Parser.parse(snd)[0]
