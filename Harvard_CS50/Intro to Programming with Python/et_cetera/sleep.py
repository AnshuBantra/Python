# GENERATORS
# def main() -> None:
#     for shp in sheep(get_input('sheep')):
#         print(shp)

# def get_input(val) -> int:
#     return int( input(f'Count of {val}: ') )

# def sheep(num):
#     flock=[]
#     for i in range(1, num+1):
#         yield f'{"🐑"*i}'

# if __name__ == '__main__':
#     main()


def test():
    for i in range(10):
        yield i

for t in test():
    print(t) 