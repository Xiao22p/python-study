# 导入整个模块
import pizza3

pizza3.make_pizza(16, 'pepperoni')
pizza3.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 导入特定的函数
from pizza3 import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用as给函数指定别名
from pizza3 import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用as给模块指定别名
import pizza3 as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 导入模块中的所有函数
from pizza3 import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')