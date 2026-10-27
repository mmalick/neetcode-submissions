class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        nextGreater = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stack) and temperatures[stack[-1]] < temperatures[i]:
                stackTop = stack.pop()
                nextGreater[stackTop] = i - stackTop
            stack.append(i)
        return nextGreater