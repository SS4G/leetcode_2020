class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        zero_idxs = set()
        for idx, c in enumerate(S):
            if len(stack) == 0:
                stack.append(c)
                zero_idxs.add(idx)
            elif stack[-1] == '(' and c == ')':
                stack.pop()
                if len(stack) == 0:
                    zero_idxs.add(idx)
            else:
                stack.append(c)
        return "".join([c for idx, c in enumerate(S) if idx not in zero_idxs])
    
