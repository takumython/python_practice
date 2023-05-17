import random


class Player:
    def __init__(self):
        self.options = ["グー", "チョキ", "パー"]


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def choose_from_options(self):
        print("\nグー、チョキ、パーを入力してください。")
        while True:
            choose_option = input("じゃんけんポン！: ")
            if choose_option in self.options:
                break
        self.choose_option = choose_option


class RobotPlayer(Player):
    def __init__(self):
        super().__init__()

    def choose_from_options(self):
        self.choose_option = random.choice(self.options)


class Referee:
    @classmethod
    def judge_round(cls, human_choose_option, robot_choose_option):
        judge_dict = {"グー": "チョキ", "チョキ": "パー", "パー": "グー"}
        if human_choose_option == robot_choose_option:
            print(
                f"\nあなた: {human_choose_option} わたし: {human_choose_option}\nあいこです！もう一度！"
            )
            return 0
        elif judge_dict.get(human_choose_option) == robot_choose_option:
            print(f"\nあなた: {human_choose_option} わたし: {robot_choose_option}\nあなたの勝ちです！")
            return 1
        else:
            print(f"\nあなた: {human_choose_option} わたし: {robot_choose_option}\nあなたの負けです！")
            return 2


class JankenGame:
    def __init__(self):
        self.human_player = HumanPlayer()
        self.robot_player = RobotPlayer()

    def set_rounds(self):
        while True:
            rounds = input("\nじゃんけんの回数を入力してください。\n回数: ")
            if rounds.isdecimal() and int(rounds) > 0:
                self.rounds = int(rounds)
                self.victory_round = int(rounds) // 2 + 1
                break
            else:
                print("数値を入力してください！")

    def play_game(self):
        print("#######プレイ 開始#######")
        self.set_rounds()

        result_list = []
        for i in range(self.rounds):
            print(f"\n#######ラウンド{i + 1} 開始！#######")

            result = 0
            while result == 0:
                for player in self.human_player, self.robot_player:
                    player.choose_from_options()
                result = Referee.judge_round(
                    self.human_player.choose_option, self.robot_player.choose_option
                )
            result_list.append(result)

            if result_list.count(1) == self.victory_round:
                print(f"\nあなたは{self.victory_round}回、わたしに勝利したので、あなたの勝ちです！")
                break
            elif result_list.count(2) == self.victory_round:
                print(f"\nわたしは{self.victory_round}回、あなたに勝利したので、わたしの勝ちです！")
                break
        if result_list.count(1) == result_list.count(2):
            print(f"\nあなたとわたしは{result_list.count(1)}回ずつ勝利したので、この勝負は引き分けです！")


if __name__ == "__main__":
    janken_game = JankenGame()
    janken_game.play_game()
