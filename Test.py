from pyparsing import *
import re

module_name = Word(alphas + '_')
full_module_name = module_name + ZeroOrMore('.' + module_name)
import_as = Optional('as' + module_name)
parse_module = 'import' + full_module_name + import_as

f = open('Test.obj')
for line in f:
    s = f.readline()
    if len(s) > 0 and (s[0] == 'v') and (s[1] == ' '):
        t = ()
        nums = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', s)
        nums = [float(i) for i in nums]
        t = (nums[0], nums[1], nums[2])
        print(t)
f.close()

