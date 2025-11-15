def build_person(first_name, last_name): # build_person()函数接受名和姓的信息
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name} # 将这些值存在字典中
    return person

musician = build_person('jimi', 'hendrix')
print(musician)