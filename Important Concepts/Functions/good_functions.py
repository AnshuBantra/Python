import datetime as dtt

def get_time() -> str:
  """ Function to get crrent time in users locale and returns it as string

  Returns:
      str: time
  
  Example:
    >>> get_time()
    '15:15:43'
  """
  now: dtt.datetime = dtt.datetime.now()
  return f'{now:%X}'

print(get_time())