# import sys library
import sys
# import hello & goodbye from saying library
from sayings import hello, goodbye



if len(sys.argv) ==2:
    goodbye(sys.argv[1])