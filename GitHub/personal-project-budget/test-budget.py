import pytest
from budget import Budget


appendMe = '\nyour leg '
add = 'testing\n'
appendFile= open('exampleFile.txt', 'a')
appendFile.write(appendMe + add)
appendFile.close()

