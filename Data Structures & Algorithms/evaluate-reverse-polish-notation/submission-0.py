class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        a,b = 1,1
        dictOfOperators = {
            "+" : lambda a, b:a + b,
            "-" : lambda a, b:a - b,
            "*" : lambda a, b:a * b,
            "/" : lambda a, b:int(a/b),
        }

        for i in tokens:
            if i not in dictOfOperators:
                stack.append(int(i))
            else:
                    b,a = stack.pop(), stack.pop()
                    stack.append(dictOfOperators[i](a, b))
        return stack.pop()