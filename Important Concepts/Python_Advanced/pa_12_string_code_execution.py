# https://www.youtube.com/watch?v=6ViGc5NgdSw&t=19s

# %% String Code Execution
# String Code Execution Local Scope
def demo_exec():
  code = '''def greet(name):
    return f'Hello {name}!'
  '''
  local_scope = {}
  global_scope = {}
  exec(code, global_scope, local_scope)
  print(local_scope['greet']('Anshu'))

demo_exec()
# %% String Code Execution
# String Code Execution Global Scope
code = '''def greet_2(name):
  return f'Hello {name}!'
'''
def demo_exec_2():
  local_scope = {}
  global_scope = {}
  exec(code, None, local_scope)
  print(local_scope['greet_2']('Mr. Bantra'))

demo_exec_2()

# %% String Input Eval
# String Input Eval

expression = input('Type in an expression: ')
print(f'Result of {expression} = {eval(expression)}')

# %% Eval
# Eval

def demo_safe_eval():

  vars = {'a':1, 'b':2, 'c':5}
  expression = input('Type in an expression: ')
  result = eval(expression, None, vars)
  print(f'Rersult of {expression} = {eval(expression)}')

demo_safe_eval()