input_list = list(map(int, input().split()))

if (input_list[0] >= input_list[1] and input_list[1] >= input_list[2]):
    # first cycle
    raw_leftovers = input_list[0] % input_list[1]
    bricks = input_list[0] // input_list[1]

    product = (input_list[1] // input_list[2]) * bricks
    bricks_leftovers = (input_list[1] % input_list[2]) * bricks

    material = raw_leftovers + bricks_leftovers

    # other cycles
    while material >= input_list[1]:
        bricks = material // input_list[1]
        product = product + (input_list[1] // input_list[2]) * bricks
        material = (material % input_list[1]) + (input_list[1] % input_list[2]) * bricks

    print(product)

else:
    print(0)