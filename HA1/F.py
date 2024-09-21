input_list = list(map(int, input().split()))

width_1 = (input_list[0] + input_list[2])
height_1 = max(input_list[1], input_list[3])

width_2 = (input_list[0] + input_list[3])
height_2 = max(input_list[1], input_list[2])

width_3 = (input_list[1] + input_list[3])
height_3 = (input_list[0] + input_list[2])

width_4 = (input_list[1] + input_list[2])
height_4 = max(input_list[0], input_list[3])

width_5 = (input_list[1] + input_list[3])
height_5 = max(input_list[0], input_list[2])

area_1 = width_1*height_1
area_2 = width_2*height_2
area_3 = width_3*height_3
area_4 = width_4*height_4
area_5 = width_5*height_5

stupid_list = [area_1, area_2, area_3, area_4, area_5]

stupid_min = min(range(len(stupid_list)),
                key=stupid_list.__getitem__
             )
print(eval('width_'+str(stupid_min+1)), eval('height_'+str(stupid_min+1)))
