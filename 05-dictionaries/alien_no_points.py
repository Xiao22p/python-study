alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])  当键不存在时会引发错误

point_value = alien_0.get('points', 'No points value assigned.')  # get()方法
print(point_value)