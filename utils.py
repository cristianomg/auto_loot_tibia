POSITIONS_FILE_NAME = 'positions.txt'

def write_position(position):
    f = open(POSITIONS_FILE_NAME, 'a')
    f.write('{},{}\n'.format(position.x, position.y))
    f.close()

def load_positions():
    f = open(POSITIONS_FILE_NAME, 'r')
    positions = f.read().split('\n')
    return [split_position(x_pos_y_pos) for x_pos_y_pos in positions if has_separator(x_pos_y_pos)]

def split_position(x_pos_y_pos):
    x, y = x_pos_y_pos.split(',')
    return {'x': int(x), 'y': int(y)}

def has_separator(str):
    return True if ',' in str else False