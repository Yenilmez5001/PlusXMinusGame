
size = int(input())
box_width = int(input())
box_height = int(input())

head = "   o "
body = "  ooo"
legs = "  o o"
box = "x"

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

if box_height <= size:
    print(head)
    for i in range(size):
        print(body)
    for i in range(size - box_height):
        print(legs)
    for i in range(box_height):
        for j in range(box_width):
            print(box, end='')
        print(legs[box_width:6])

elif box_height == 2 * size + 1:
    for i in range(box_width):
        print(box, end='')
    print(head[box_width:6])
    for i in range(size):
        for j in range(box_width):
            print(box, end='')
        print(body[box_width:6])
    for i in range(size):
        for j in range(box_width):
            print(box, end='')
        print(legs[box_width:6])

else:
    print(head)
    for i in range(2 * size - box_height):
        print(body)
    for i in range(box_height - size):
        for j in range(box_width):
            print(box, end='')
        print(body[box_width:6])
    for i in range(size):
        for j in range(box_width):
            print(box, end='')
        print(legs[box_width:6])


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

