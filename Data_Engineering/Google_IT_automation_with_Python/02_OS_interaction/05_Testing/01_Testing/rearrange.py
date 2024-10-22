# %%
import re

def rearrange_name(name):
  # if type(name) != str: return name
  # result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  # if result is None:
  #   return name
  # return "{} {}".format(result[2], result[1])

  try:
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    return "{} {}".format(result[2], result[1])
  except:
    return name

# %%
