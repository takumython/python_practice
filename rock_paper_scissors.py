import random


class RockPaperSciccors:
    def __init__(self):
        self.choices = ["グー", "チョキ", "パー"]

    def set_rounds(self):
        while True:
            rounds = input("\nじゃんけんの回数を入力してください。\n回数: ")
            if rounds.isdecimal() and int(rounds) > 0:
                self.rounds = int(rounds)
                self.victory_round = int(rounds) // 2 + 1
                break
            else:
                print("数値を入力してください！")

    def input_user_choice(self):
        print("\nグー、チョキ、パーを入力してください。")
        while True:
            user_choice = input("じゃんけんポン！: ")
            if user_choice in self.choices:
                break
        self.user_choice = user_choice

    def select_robot_choice(self):
        self.robot_choice = random.choice(self.choices)

    def judge_round(self):
        judge_dict = {"グー": "チョキ", "チョキ": "パー", "パー": "グー"}
        if self.user_choice == self.robot_choice:
            print(f"\nあなた: {self.user_choice} わたし: {self.robot_choice}\nあいこです！もう一度！")
            return 0
        elif judge_dict.get(self.user_choice) == self.robot_choice:
            print(f"\nあなた: {self.user_choice} わたし: {self.robot_choice}\nあなたの勝ちです！")
            return 1
        else:
            print(f"\nあなた: {self.user_choice} わたし: {self.robot_choice}\nあなたの負けです！")
            return 2

    def play_game(self):
        print("#######プレイ 開始#######")
        self.set_rounds()

        result_list = []
        for i in range(self.rounds):
            print(f"\n#######ラウンド{i + 1} 開始！#######")

            result = 0
            while result == 0:
                self.input_user_choice()
                self.select_robot_choice()
                result = self.judge_round()
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
    rock_paper_scissors = RockPaperSciccors()
    rock_paper_scissors.play_game()
