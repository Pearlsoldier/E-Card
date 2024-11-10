import random

player_card_list = ["市民", "市民", "市民", "市民", "奴隷"]
host_card_list = ["市民", "市民", "市民", "市民", "皇帝"]


def turn_count(count):
    count += 1
    return count


def judge(player_card, host_card):
    print("カードオープンっ！！")
    print("ざわ。ざわ。。")
    print(player_card, host_card)
    if player_card == host_card:
        print("引き分け")
        print("次のカードを選べ")
        return "drow"
    elif player_card == "奴隷" and host_card == "皇帝":
        print("Playerの勝利")
        print("Congratulation!!")
        return "player_win"
    else:
        print("Playerの敗北")
        return "player_loose"


def player_choice_card(player_card_list):
    print("手札:市民", player_card_list.count("市民"), "奴隷", player_card_list.count("奴隷"))
    player_choice = str(input())
    print(player_choice)
    player_card_list.remove(player_choice)
    print(player_card_list)
    return player_choice


def host_choice_card(host_Card_list):
    random.shuffle(host_Card_list)
    host_choice = host_card_list.pop()
    return host_choice


def main():
    count = 0
    print("ようこそ。Eゲームへ。")
    while True:
        print(count + 1, "戦目")
        player_card = player_choice_card(player_card_list)
        host_card = host_choice_card(host_card_list)
        result = judge(player_card, host_card)
        if "player_win" == result or "player_loose" == result:
            break
        count = turn_count(count)


if __name__ == "__main__":
    main()