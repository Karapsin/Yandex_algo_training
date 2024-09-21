import math

input_list = list(map(int, input().split()))

K1 = input_list[0]
M  = input_list[1]
K2 = input_list[2]
P2 = input_list[3]
N2 = input_list[4]

all_prev_sections = ((P2-1)*M+(N2-1))

if all_prev_sections==0:
    if K1<K2:
        print(1, 1)
    elif M==1:
        print(0, 1)
    elif K1<M:
        print(1, 0)
    else:
        print(0, 0)

else:
    upper_guess = (K2/all_prev_sections)-0.000001
    lower_guess = K2/(all_prev_sections+1)

    guesses = list(range(math.ceil(lower_guess), math.floor(upper_guess) + 1))
    guesses = [item for item in guesses if item >= 0]

    if  N2>M or len(guesses)==0:
        print(-1, -1)
    else:
        P1 = []
        N1 = []
        for guess in guesses:
            flats_per_section = guess*M

            current_p1 = math.ceil(K1/flats_per_section)

            P1.append(current_p1)

            upper_part = K1 - flats_per_section*(current_p1-1)

            if (upper_part%guess)==0:
                N1.append((upper_part // guess))
            else:
                N1.append((upper_part//guess)+1)

        set_P1 = set(P1)
        set_N1 = set(N1)

        if len(set_P1)==1 and len(set_N1)==1:
            print(P1[0], N1[0])

        elif len(set_P1)!=1 and len(set_N1)==1:
            print(0, N1[0])

        elif len(set_P1)==1 and len(set_N1)!=1:
            print(P1[0], 0)

        elif len(set_P1)!=1 and len(set_N1)!=1:
            print(0, 0)

