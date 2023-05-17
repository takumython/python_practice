import random


class Player:
    def __init__(self):
        self.options = ["グー", "チョキ", "パー"]


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = input("名前を入力してください: ")

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
        self.name = "ロボット"

    def choose_from_options(self):
        self.choose_option = random.choice(self.options)


class JankenGame:
    def __init__(self):
        self.human = HumanPlayer()
        self.robot = RobotPlayer()
        self.result_list = []

    def set_rounds(self):
        while True:
            rounds = input("\nじゃんけんの回数を入力してください。\n回数: ")
            if rounds.isdecimal() and int(rounds) > 0:
                self.rounds = int(rounds)
                self.victory_round = int(rounds) // 2 + 1
                break
            else:
                print("数値を入力してください！")

    def judge_round(self, human_choose_option, robot_choose_option):
        judge_dict = {"グー": "チョキ", "チョキ": "パー", "パー": "グー"}
        base_text = f"\n{self.human.name}: {human_choose_option}\n{self.robot.name}: {robot_choose_option}"
        if human_choose_option == robot_choose_option:
            print(base_text + "\nあいこです！もう一度！")
            return 0
        elif judge_dict.get(human_choose_option) == robot_choose_option:
            print(base_text + "\nあなたの勝ちです！")
            return 1
        else:
            print(base_text + "\nあなたの負けです！")
            return 2

    def judge_game(self):
        insert_line = "\n#######結果発表#######\n"
        base_text = f"勝利回数\n{self.human.name}: {self.result_list.count(1)}回\n{self.robot.name}: {self.result_list.count(2)}回"
        if self.result_list.count(1) == self.victory_round:
            print(insert_line + base_text + f"\n{self.human.name}の勝ちです！")
            return True
        elif self.result_list.count(2) == self.victory_round:
            print(insert_line + base_text + f"\n{self.robot.name}の勝ちです！")
            return True
        elif len(self.result_list) == self.rounds:
            print(insert_line + base_text + f"\nこの勝負は引き分けです！")
            return True
        else:
            return False

    def play_game(self):
        print("#######プレイ 開始#######")
        self.set_rounds()

        for i in range(self.rounds):
            print(f"\n#######ラウンド{i + 1} 開始！#######")

            result = 0
            while result == 0:
                for player in self.human, self.robot:
                    player.choose_from_options()
                result = self.judge_round(
                    self.human.choose_option, self.robot.choose_option
                )
            self.result_list.append(result)

            if self.judge_game():
                break


if __name__ == "__main__":
    janken_game = JankenGame()
    janken_game.play_game()
