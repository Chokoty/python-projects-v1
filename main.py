import random

# 난수 정답 생성 부분
answer = []
for i in range(3):
  while True:
    temp = random.randrange(0,10)
    if temp in answer:
      continue
    break
  answer.append(temp)
#print(answer)

strike = 0
ball = 0
life = 9
cnt = 0

# 9번 반복
print("9번 이상 입력하면 실패입니다.")
while(True):

  if cnt == life:
    print("Game over...\n")
    user = input("# Press any key to restart #\n# Press x to exit...       #\n")
    if user == 'x':
      break
    else: 
      cnt = 0
      print("9번 이상 입력하면 실패입니다.")
      continue
      

  cnt += 1

# 입력받는 부분
# 입력 조건 : 같은 숫자 입력받지 못하도록, 숫자 3개를 입력 받도록 검사, 0~9 사이의 숫자만 받도록 검사  

  player = list(map(int,input("숫자 3개를 입력하세요: ").split()))
  # while len(player) != 3:
  #   player = list(map(int,input("숫자 3.개.를 입력하세요: ").split()))
  if len(player) != 3:
    print("숫자 3개를 입력해야 합니다. 다시 입력해주세요\n")
    cnt -= 1
    continue;
  elif player[0] == player[1] or player[1] == player[2] or player[2] == player[0]:
    print("서로 다른 숫자를 입력해야 합니다.다시 입력해주세요\n")
    cnt -= 1
    continue;
  
# 비교 하는 부분
  strike = 0
  ball = 0
  for i in range(3):
    for j in range(3):
      if answer[i] == player[j]:
        if i == j:
          strike += 1
        else:
          ball += 1


  if strike == 3:
    print(f"정답입니다! 시도횟수: {cnt}\n")
    break
  print(f"{strike}S {ball}B")  

# 남은 횟수 출력하는 부분
  # print(player)
  print(f"{life-cnt}번 남음\n")

