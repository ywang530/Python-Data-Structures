def draw_line(tick_length, tick_label=''):
    '''Draw one line with given tick length (followed by optional label).'''
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    '''Draw tick interval based upon a central tick length'''
    if center_length > 0:                   # stop when length drops to 0
        draw_interval(center_length - 1)    # recursively draw top ticks
        draw_line(center_length)            # draw center tick
        draw_interval(center_length - 1)    # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    '''Draw English ruler with given number of inches, major tick length'''
    draw_line(major_length, '0')
    for i in range(1, 1+num_inches):
        draw_interval(major_length-1)
        draw_line(major_length, str(i))


if __name__ == '__main__':
    draw_line(4, '0')
    draw_interval(3)
    draw_ruler(4,3)