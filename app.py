from seat_shuffle import SeatShuffle


def input_members():
    with open("members.txt", "r") as f:
        members = f.read().split("\n")

    member_counter = 0
    input_seat = ""

    while member_counter < 15:
        if member_counter == 0:
            print("現在のテーブル1(6席)の配置を下記のメンバーの数字から入力してください")

        if member_counter == 6:
            input_seat = input_seat[:-1] + "\n"
            print("現在のテーブル2(5席)の配置を下記のメンバーの数字から入力してください")

        if member_counter == 11:
            input_seat = input_seat[:-1] + "\n"
            print("現在のテーブル3(4席)の配置を下記のメンバーの数字から入力してください")

        for index in range(len(members)):
            print(f"{index}: {members[index]}")

        try:
            input_index = int(input())
            input_seat += members[input_index] + " "
            members.pop(input_index)
            member_counter += 1
        except IndexError:
            print("表示されている数字を入力してください\n")

        except:
            print("予期せぬエラーが発生しました。")
            exit()

    with open("before_seat.txt", "w")as f:
        f.write(input_seat[:-1])


def main():
    with open("before_seat.txt", "r") as f:
        before_seat = f.read()

    if len(before_seat) == 0:
        input_members()

    seat = SeatShuffle()
    seat.shuffle()

    print("table1: " + " ".join(seat.table1))
    print("table2: " + " ".join(seat.table2))
    print("table3: " + " ".join(seat.table3))


if __name__ == "__main__":
    main()
