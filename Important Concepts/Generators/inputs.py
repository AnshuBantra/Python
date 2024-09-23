import keyboard as kbd
import threading
import queue

def esc_listener(q):
    # This function will run in a separate thread to listen for the 'Esc' key press
    kbd.wait('esc')
    q.put('esc')

def get_float() -> float:
    q = queue.Queue()
    listener_thread = threading.Thread(target=esc_listener, args=(q,))
    listener_thread.daemon = True
    listener_thread.start()
    
    while True:
      _ = input('Enter number: ')

      if not q.empty():
          print("Esc pressed. Exiting the loop.")
          break
      
      try:
        _ = float(_)
        return _
      except ValueError:
        print(f'{_} is not a number')
        pass

def main():
  print(get_float())

if __name__ == '__main__':
  main()