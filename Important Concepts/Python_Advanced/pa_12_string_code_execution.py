# https://www.youtube.com/watch?v=6ViGc5NgdSw&t=19s

# %% String Code Execution
# String Code Execution
def demo_exec():
  code = '''def greet(name):
    return f'Hello {name}!'
  '''
  local_scope = {}
  global_scope = {}
  exec(code, global_scope, local_scope)
  print(global_scope['greet']('Anshu'))

demo_exec()
# %%
