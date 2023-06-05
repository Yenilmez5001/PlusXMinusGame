
prompt_1 = "Please enter the board size\n"
prompt_2 = "Please enter how many squares you want to place\n"
prompt_3 = "Please enter the coordinates of a square you want to place\n"
prompt_4 = "Please enter a target square coordinate, or enter exit to exit\n"
prompt_5 = "Congratulations, you won!"
prompt_6 = "Thanks for playing."
error_message_1 = "Improper board size"
error_message_2 = "Improper amount of squares"
error_message_3 = "Incorrect input format for square coordinates"
error_message_4 = "Improper square coordinates"
error_message_5 = "Sign already placed to square"


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

while True:
    size = int(input(prompt_1))
    if not 5 <= size <= 9:
        print(error_message_1)
        continue
    else:
        break

matrix = []
for _ in range(size):
    matrix.append([0] * size)

while True:
    number_of_target = int(input(prompt_2))
    if not 1 <= number_of_target <= size**2:
        print(error_message_2)
        continue
    else:
        break

_ = 0
while True:
    if _ == number_of_target:
        break

    coordinates_input = input(prompt_3)

    if len(coordinates_input.split()) < 2:
        print(error_message_3)
        continue

    x, y = coordinates_input.split()[:2]

    try:
        x, y = int(x), int(y)

        if 1 <= x <= size and 1 <= y <= size:
            if matrix[x - 1][y - 1] == 1:
                print(error_message_5)
                continue
            else:
                matrix[x - 1][y - 1] = 1
                _ += 1

                print(' ', end='')
                for i in range(size):
                    print(' ' + str(i + 1), end='')
                print()
                for i in range(size):
                    print(i + 1, end='')
                    for j in range(size):
                        if matrix[i][j]:
                            print(' +', end='')
                        else:
                            print(' -', end='')
                    print()

        else:
            print(error_message_4)
            continue

    except ValueError:
        print(error_message_3)
        continue

while True:

    swap_coordinates = input(prompt_4)

    if len(swap_coordinates.split()) < 2:
        if swap_coordinates.lower() == 'exit':
            print(prompt_6)
            break

        print(error_message_3)
        continue

    x, y = swap_coordinates.split()[:2]
    try:

        x, y = int(x), int(y)
        if 1 <= x <= size and 1 <= y <= size:
            matrix[x - 1][y - 1] = - matrix[x - 1][y - 1] + 1
            if x - 2 >= 0 and y - 2 >= 0:
                matrix[x - 2][y - 2] = - matrix[x - 2][y - 2] + 1
            if x - 2 >= 0 and y < size:
                matrix[x - 2][y] = - matrix[x - 2][y] + 1
            if x < size and y - 2 >= 0:
                matrix[x][y - 2] = - matrix[x][y - 2] + 1
            if x < size and y < size:
                matrix[x][y] = - matrix[x][y] + 1

            print(' ', end='')
            for i in range(size):
                print(' ' + str(i + 1), end='')
            print()
            for i in range(size):
                print(i + 1, end='')
                for j in range(size):
                    if matrix[i][j]:
                        print(' +', end='')
                    else:
                        print(' -', end='')
                print()

            kazandi = True
            for k in matrix:
                for l in k:
                    if l == 1:
                        kazandi = False
            if kazandi:
                print(prompt_5)
                print(prompt_6)
                break

        else:
            print(error_message_4)
            continue

    except ValueError:
        print(error_message_3)
        continue

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE