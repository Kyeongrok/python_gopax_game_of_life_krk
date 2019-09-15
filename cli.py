import sys
from conway.gol import GameOfLife

def main():
    # txt를 입력 받음

    # 알고리즘 적용해서 새 grid를 만듬
    # 화면에 출력함

    if len(sys.argv) > 1:
        file = open(sys.argv[1])
        lines = file.readlines()
        print(lines)

        num_rows = 10
        num_cols = 10
        gol = GameOfLife(num_rows, num_cols)
        gol.start()
    else:
        print("------")

if __name__ == '__main__':
    main()


