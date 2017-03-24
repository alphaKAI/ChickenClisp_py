# -*- coding: utf-8 -*-
import re

nrgx = re.compile("[0-9]")

from expression.ImmediateValue import ImmediateValue


class Parser:
    @staticmethod
    def nextBracket(code):
        i = 0
        leftCount = 1
        rightCount = 0

        while leftCount != rightCount:
            if code[i] == '(':
                leftCount += 1
            elif code[i] == ')':
                rightCount += 1
            i += 1

        return i

    @staticmethod
    def parse(code):
        out = []
        i = 0

        while i < len(code):
            ch = code[i]

            if ch == ' ':
                i += 1
                continue

            if ch == '(':
                j = Parser.nextBracket(code[i + 1:])

                out.append(Parser.parse(code[i + 1:i + j + 1]))

                i += j
                i += 1
                continue

            if ch == ')':
                return out

            if nrgx.search(ch) or (i + 1 < len(code) and ch == '-' and nrgx.search(code[i + 1])):
                tmp = ""
                j = i

                while True:
                    tmp += code[j]
                    j += 1

                    if not ((j < len(code)) and ((code[j] != " " and nrgx.search(code[j])) or (code[j] == "." and j + 1 < len(code) and ngrx.search(code[j + 1])))):
                        break

                if tmp.find(".") == -1:
                    out.append(int(tmp))
                else:
                    out.append(float(tmp))

                i = j - 1
                i += 1
                continue

            if (ch == '\"' or ch == '\''):
                if (ch == '\'' and i + 1 < len(code) and code[i + 1] == '('):
                    j = Parser.nextBracket(code[i + 2:]) + 1

                    out.append(ImmediateValue(
                        Parser.parse(code[i + 2:i + j + 1])))

                    i += j
                    i += 1
                    continue
                else:
                    tmp = ""
                    j = i + 1

                    while (code[j] != ch and j < len(code)):
                        tmp += code[j]
                        j += 1

                    out.append(tmp)
                    i = j
                    i += 1
                    continue

            tmp = ""
            j = i

            while (j < len(code) and code[j] != "\"" and code[j] != "\'" and code[j] != "(" and code[j] != ")" and code[j] != " "):
                tmp += code[j]
                j += 1

            if tmp == "true":
                out.append(True)
            elif tmp == "false":
                out.append(False)
            elif tmp == "null":
                out.append(None)
            else:
                out.append(tmp)

            i = j
            i += 1
            continue

        return out
