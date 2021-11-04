import random

answer = []
for i in range(3):
  while True:
    temp = random.randrange(0,10)
    if temp in answer:
      continue
    break
  
  answer.append(temp)

print(answer)



# answer = [1,3,2]
# player = [,,]

# player = list(map(int, input().split()))
# print(player)