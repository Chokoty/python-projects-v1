import random

class Game:
  def __init__(self, life):
    self.AI = []
    self.player = []
    self.cnt = 0
    self.life = life

# 게임 타이틀
  def print_title(self):
    print("==============")
    print("숫자야구 v1.1")
    print(f"{self.life}번 이상 입력하면 실패입니다.") # 9번 반복
    print("==============")
    
  # 난수 정답 생성 부분
  def make_answer(self):
    #answer = []
    for i in range(3):
      while True:
        temp = random.randrange(0,10) # shuffle도 가능
        #if temp in answer:
        if temp in self.AI:
          continue
        break
      self.AI.append(temp)
      #answer.append(temp)
    #return answer

  # 게임 카운트 
  def check_cnt(self):
    if self.cnt == self.life:
      print("Game over...\n")
      user = input("# Press any key to restart #\n# Press x to exit...       #\n")
      if user == 'x':
        return "exit"
      else: 
        self.AI = self.make_answer() # 클래스 안에서 자기 메소드 부르려면 self 쓰기
        self.cnt = 0
        print(f"{self.life}번 이상 입력하면 실패입니다.")
        return "restart"
    self.cnt += 1

  # 플레이어턴 
  # 입력 조건, 유효성 검사 : 같은 숫자 x, 숫자는 3개, 0~9 사이의 숫자만
  def player_input(self):
    self.player = list(map(int,input("숫자 3개를 입력하세요: ").split()))
    
    if len(self.player) != 3:
      print("숫자 3개를 입력해야 합니다. 다시 입력해주세요\n")
      self.player_input()
    elif self.player[0] == self.player[1] or self.player[1] == self.player[2] or self.player[2] == self.player[0]:
      print("서로 다른 숫자를 입력해야 합니다.다시 입력해주세요\n")
      self.player_input()

  def print_hit_status(self):
    strike = 0
    ball = 0 

    for i in range(3):
      for j in range(3):
        if self.AI[i] == self.player[j]:
          if i == j:
            strike += 1
          else:
            ball += 1
  
    if strike == 3:
      print(f"정답입니다! 시도횟수: {self.cnt}\n")
      return "win"

    print(f"{strike}S {ball}B")  
    print(f"{self.life-self.cnt}번 남음\n")
