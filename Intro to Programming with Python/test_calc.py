import pytest
from calculator import square

def test_square_positive():
    test_lst = [2,3]
    for num in test_lst:
        assert square(num) == num*num

def test_square_negative():
    test_lst = [-2,-3]
    for num in test_lst:
        assert square(num) == num*num

def test_square_zero():
    test_lst = [0]
    for num in test_lst:
        assert square(num) == num*num

def test_square_str():
    with pytest.raises(TypeError):
        square('abc')


# def main():
#     test_square()

# def test_square():
#     import random
#     # test_lst = [random.randrange(-100, 100, 1) for _  in range(200)]
#     test_lst = [-3-2,0,2,3]
#     # count = 0
#     for num in test_lst:
#         assert square(num) == num*num
    #     try:
    #         assert square(num) == num*num
    #         count += 1
    #     except AssertionError:
    #         print(f'{num} squared returned {square(num)} instead of {num**2}')
        
    # print(f'{count} of 200 passed')

# def

# if __name__ == '__main__':
#     main()