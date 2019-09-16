import sys
from conway.gol import GameOfLife

def parse_file(lines):
    line0 = lines[0].split()
    str_points = [ item.replace("\n", "").split() for item in lines[2:2+int(lines[1])]]
    points = [{"x":int(item[0]), "y":int(item[1])} for item in str_points]
    result = {"num_rows":int(line0[0]), "num_cols":int(line0[1]),
              "points":points}
    return result

def main():
    # commad 입력 받음
    if len(sys.argv) == 2:
        file = open(sys.argv[1])
        lines = file.readlines()
        command = parse_file(lines)

        gol = GameOfLife(command["num_rows"], command["num_cols"], command["points"])

        while gol.state == "waiting":
            key = gol.win.getch()
            if key == ord("s"):
                gol.start()

    elif len(sys.argv) == 3:
        # 두번째 파라메터의 횟수가 되었을 때 파일을 출력한다.
        print("---파일 출력하기---")
    else:
        # parameter가 없다는 것. 랜덤으로 생성한다.
        print("---{}---", len(sys.argv))
        gol = GameOfLife(10, 10, [])
        gol.start()

if __name__ == '__main__':
    main()


