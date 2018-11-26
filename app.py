from seat_shuffle import SeatShuffle


def input_members():
    with open("members.txt", "r")as f:
        members = f.read().split("\n")

    member_counter = 0

    while member_counter >= 15:
        if member_counter == 0:
            print("現在のテーブル1(6席)の配置を下記のメンバーの数字から入力してください")

        if member_counter == 6:
            input_seat = input_seat + "\n"
            print("現在のテーブル2(5席)の配置を下記のメンバーの数字から入力してください")

        if member_counter == 10:
            input_seat = input_seat + "\n"
            print("現在のテーブル3(4席)の配置を下記のメンバーの数字から入力してください")

        for index in range(len(members)):
            print(f"{index}: {members[index]}")

        input_seat = input_seat + " " + members[int(input())]
        member_counter += 1

    with open("before_seat.txt", "w")as f:
        f.write(str(input_seat))


def main():
    with open("before_seat.txt", "r") as f:
        before_seat = f.read()

    if before_seat == "":
        input_members()

    seat = SeatShuffle()
    seat.shuffle()

    print("table1: " + " ".join(seat.table1))
    print("table2: " + " ".join(seat.table2))
    print("table3: " + " ".join(seat.table3))


if __name__ == "__main__":
    main()
