import random
import re
from GoodNumberTable import GoodNumberTable
from WordTable import WordTable

class NameCalc:

    desired_total = [31,32,35,37,41,45,47,48]
    cur_combi = list()
    out_file_name = "num_result.txt"
    out_file = None
    found_combi = list()

    def __init__(self) -> None:
        self.good_table = GoodNumberTable()
        self.good_table.build_good_list()
        self.out_file = open(self.out_file_name, "w")
        pass

    def find_num_b(self, level=0, num_a=16):
        self.cur_combi.append(num_a)
        #print(f"Now {level} {num_a} cur_combi {self.cur_combi}")
        if num_a >= 23:
            self.cur_combi.pop()
            return

        if level < 2:
            for g in self.good_table.good_idx_list:
                if g > num_a and (g - num_a) > 3:
                    self.find_num_b(level+1, g - num_a)
                else:
                    continue
        elif self.good_table.is_good(num_a + 1):
            cur_sum = sum(self.cur_combi)
            if cur_sum in self.good_table.good_idx_list:
                s = f"Find combi: {self.cur_combi} Sum = {cur_sum}"
                print(s)
                self.out_file.write(s+"\n")
                self.found_combi.append((self.cur_combi[0], self.cur_combi[1], self.cur_combi[2]))

        self.cur_combi.pop()
        return


if __name__ == "__main__":
    calc = NameCalc()
    calc.find_num_b(0, 16)
    print(calc.found_combi)

    ofh = open("name_result.txt", "w", encoding='utf-8')
    wtable = WordTable()
    good_names = list()
    for c in calc.found_combi:
        s = ["陳"]
        for w1 in wtable.table[c[1]]:
            if w1 in wtable.dont_want_list:
                continue
            s.append(w1)
            for w2 in wtable.table[c[2]]:
                if w2 in wtable.dont_want_list:
                    continue
                s.append(w2)
                n = str(s[0])+str(s[1])+str(s[2])
                good_names.append(n)
                s.pop()
            s.pop()
    #random.shuffle(good_names)

    want_list = ["南", "映", "香", "希"]
    for n in good_names:
        for w in want_list:
            if re.search(w, n):
                ofh.write(n+"\n")
                break



        


