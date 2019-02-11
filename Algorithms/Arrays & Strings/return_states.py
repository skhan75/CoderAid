def cellCompete(states, days):


    for day in range(1,days+1):
        placeholder_for_zeroes = []
        placeholder_for_ones = []
        for i in range(0,len(states)):
            if i == 0:

                left_state = 0
                right_state = states[i+1]

            elif  i == len(states)-1:
                right_state = 0
                left_state = states[i-1]

            else:
                left_state = states[i-1]
                right_state = states[i+1]

            if left_state == 0 and right_state == 0:
                placeholder_for_zeroes.append(i)
            elif left_state == 1 and right_state == 1:
                placeholder_for_zeroes.append(i)
            else:
                placeholder_for_ones.append(i)

        for i in placeholder_for_zeroes:
            states[i] = 0
        for i in placeholder_for_ones:
            states[i] = 1




    return states


print (cellCompete([1,1,1,0,1,1,1,1],2))
