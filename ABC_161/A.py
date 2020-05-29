boxes = list(map(int, input().split()))

boxes[0], boxes[1] = boxes[1], boxes[0]
boxes[0], boxes[2] = boxes[2], boxes[0]

print(str(boxes[0]) + ' ' + str(boxes[1]) + ' ' + str(boxes[2]))