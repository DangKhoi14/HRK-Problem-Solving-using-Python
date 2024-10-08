# https://www.hackerrank.com/challenges/taum-and-bday/problem


import os


def taumBday(b, w, bc, wc, z):
    cost_1 = b * bc + w * wc
    cost_2 = (b + w) * wc + b*z
    cost_3 = (b + w) * bc + w*z

    return min(cost_1, cost_2, cost_3)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()