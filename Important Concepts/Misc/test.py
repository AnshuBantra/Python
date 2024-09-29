import re
import sys

def main():
    print( validate( input("IPv4 Address: ") ) )

def validate(ip):
    if ip == '' or ip == None:
        return False
    if 2 < ip.count('.') < 4:
        (p1, p2, p3, p4) = ip.split('.')
    else:
        return False
    try:
        nums = [int(_) for _ in (p1,p2,p3,p4)]
        for _ in nums:
            if not 0 <= _ <= 255:
                return False
    except ValueError:
        return False
    except Exception as e:
        return False
    return True

if __name__ == "__main__":
    main()
