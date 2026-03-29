class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(token))
        return stack[0]

                

        # for token in tokens:
        #     if token.isdigit():
        #         internal.append(int(token))
        #     else:
        #         if token == '+':
        #             res += sum(internal)
        #         elif token == '-':
        #             sub_res = internal[0]
        #             for sub_token in range(1,len(internal)):
        #                 sub_res -= internal[sub_token]
        #             res -= sub_res
        #         elif token == '*':
        #             prod_res = internal[0]
        #             for prod_token in range(1, len(internal)):
        #                 prod_res *= prod_res
        #             res *= prod_res
        #         elif token == '/':
        #             div_res = internal[0]
        #             for div_res in range(1, len(internal)):
        #                 div_res /= div_res
        #             res /= div_res
        #         internal = []
            
