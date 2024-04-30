def check_brackets(inputs):
    results = []
    for line in inputs:
        results.append(''.join(line))  # 先添加原始行
        stack = []   # 存左括号编号
        output = []  # 存储每行的输出结果

        # 记录左括号，标记右括号
        for i in range(0,len(line)):
            if line[i] == '(':
                stack.append(i)
                output.append(' ')
            elif line[i] == ')':
                if stack:
                    stack.pop()
                    output.append(' ')
                else:
                    output.append('?')
            else:
                output.append(' ')
        # 记录剩余的左括号
        while stack:
            j = stack.pop()
            output[j] = 'x'
        # 输出
        results.append(''.join(output))
    return results


input_examples = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]
output_results = check_brackets(input_examples)
for result in output_results:
    print(result)