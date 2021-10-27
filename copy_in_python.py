# alias
warmtones = ['oranges', 'browns', 'red']
palette = warmtones
palette.append('Blue')
warmtones.append('Green')
print('alias')
print(palette, hex(id(palette)))
print(warmtones, hex(id(warmtones)))


# shallow copy
warmtones = ['oranges', 'browns', 'red']
palette = list(warmtones)
palette.append('Blue')
warmtones.append('Green')
print('shallow copy')
print(palette, hex(id(palette)))
print(warmtones, hex(id(warmtones)))


# deep copy
import copy
warmtones = ['oranges', 'browns', 'red']
palette = copy.deepcopy(warmtones)
palette.append('Blue')
warmtones.append('Green')
print('shallow copy')
print(palette, hex(id(palette)))
print(warmtones, hex(id(warmtones)))