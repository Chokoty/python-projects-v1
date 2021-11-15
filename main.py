import game as g

# AI = []
# player = []
# strike = 0
# ball = 0
# life = 9
# cnt = 0

game = g.Game(9)
# 게임 멘트
game.print_title()
# 게임 실행
game.make_answer()
while(True):
  if game.check_cnt() == "exit": # 남은 턴 확인
    break
  game.player_input() # 플레이어 차례
  if game.print_hit_status() == "win": # 스트라이크 볼 출력
    break

