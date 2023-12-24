def main():
    height=5
    width=3
    symbol='$'
    print_grid(height, width, symbol)

def print_grid(height=1, width=1, symbol='#'):
    for _ in range(height):
        print(symbol*width)

main() #,symbol='$')