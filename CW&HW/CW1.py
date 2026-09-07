apple_j = 15.5
orange_j = 20
grape_j = 10.25

total_volume = apple_j+orange_j+grape_j
print('total volume is',total_volume)

convert_vol_int = int(total_volume)
print('converted int volume is',convert_vol_int)

convert_vol_str = str(total_volume)
print('converted str volume is',convert_vol_str)

import random
add_bonus = (random.randrange(5,10)) + total_volume
print('bonus volume is',add_bonus)