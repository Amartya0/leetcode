class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # stack = []
        # for token in tokens:
        #     if token == '*':
        #         stack.append(stack.pop()*stack.pop())
        #     elif token == '+':
        #         stack.append(stack.pop()+stack.pop())
        #     elif token == '-':
        #         subtractor = stack.pop()
        #         stack.append(stack.pop() - subtractor)
        #     elif token == '/':
        #         divisor = stack.pop()
        #         stack.append(int(stack.pop()/divisor))
        #     else:
        #         stack.append(int(token))

        # return stack[0]

        stack = []
        for token in tokens:
            if token in '+-*/':
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]


def main():
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
    # Output: 9
    print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
    # Output: 6
    print(Solution().evalRPN(["10", "6", "9", "3",
          "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
    # Output: 22


if __name__ == '__main__':
    main()
