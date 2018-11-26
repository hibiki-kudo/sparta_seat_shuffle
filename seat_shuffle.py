import random


class SeatShuffle:

    def __init__(self):
        with open("before_seat.txt", "r") as f:
            before_seats = f.read()

        self.table1 = before_seats.split("\n")[0].split(" ")
        self.table2 = before_seats.split("\n")[1].split(" ")
        self.table3 = before_seats.split("\n")[2].split(" ")


    # 実際に動かすために呼ばれるためのメソッド
    def shuffle(self):
        seats = self._stay_seat()

        # 今回の席を保存するためにファイルを開く
        f = open("before_seat.txt", "w")

        index = 0

        for rest_seat in self._shuffle_decision():
            seats[index].extend(rest_seat)

            # 念の為、席内で更にシャッフル
            seats[index] = random.sample(seats[index], len(seats[index]))

            # 今回の処理を次の席移動のために結果を保存しておく
            f.write(str(" ".join(seats[index])) + "\n")

            index += 1

        f.close()

        self.table1 = seats[0]
        self.table2 = seats[1]
        self.table3 = seats[2]

    # 最初に席の1/3の人を残すためのメソッド
    def _stay_seat(self):
        instead_table1 = random.sample(self.table1, int(round(len(self.table1) / 3)))
        self.table1 = [a for a in self.table1 if a not in instead_table1]

        instead_table2 = random.sample(self.table2, int(round(len(self.table2) / 3)))
        self.table2 = [a for a in self.table2 if a not in instead_table2]

        instead_table3 = random.sample(self.table3, int(round(len(self.table3) / 3)))
        self.table3 = [a for a in self.table3 if a not in instead_table3]

        return [instead_table1, instead_table2, instead_table3]

    # _stay_seatで選ばれなかった人をランダムで決めるためのメソッド
    def _shuffle_decision(self):
        # 前回の席のtableから別の席のtableに移るようにランダム(ここはtable1)
        instead_table1 = random.sample(self.table2 + self.table3, 4)
        # 選択された分、tableに保存されいる人を削除していく
        self.table2 = [a for a in self.table2 if a not in instead_table1]
        self.table3 = [a for a in self.table3 if a not in instead_table1]

        # 上記と同様
        instead_table2 = random.sample(self.table1 + self.table3, 3)
        self.table1 = [a for a in self.table1 if a not in instead_table2]
        self.table3 = [a for a in self.table3 if a not in instead_table2]

        # 場合によってはtable1とtable2ばかり上記のtableで選択された場合のためにここの部分は全tableから取得
        instead_table3 = random.sample(self.table1 + self.table2 + self.table3, 3)
        self.table1 = [a for a in self.table1 if a not in instead_table3]
        self.table2 = [a for a in self.table2 if a not in instead_table3]
        self.table3 = [a for a in self.table3 if a not in instead_table3]

        return instead_table1, instead_table2, instead_table3


if __name__ == "__main__":
    seat = SeatShuffle()
    seat.shuffle()

    print(f"table1: " + " ".join(seat.table1))
    print(f"table2: " + " ".join(seat.table2))
    print(f"table3: " + " ".join(seat.table3))
