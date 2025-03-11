# Replace m8 with the student submission filename

import m8

module = m8
function_name = input()
function = getattr(module, function_name)
inputs = input()
if len(inputs) > 0:
    inputs = inputs.split("|")
    inputs = map(str.strip, inputs)
    inputs = map(eval, inputs)
    inputs = list(inputs)
else:
    inputs = []
return_value = function(*inputs)
inputs = map(repr, inputs)
print(f"{function_name}({', '.join(inputs)}) returned {repr(return_value)}")