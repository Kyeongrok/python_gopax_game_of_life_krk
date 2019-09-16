import sys
from random import randrange
from conway.gol import GameOfLife

def parse_file(lines):
    line0 = lines[0].split()
    str_points = [ item.replace("\n", "").split() for item in lines[2:2+int(lines[1])]]
    points = [{"x":int(item[0]), "y":int(item[1])} for item in str_points]
    result = {"num_rows":int(line0[0]), "num_cols":int(line0[1]),
              "points":points}
    return result

def get_random_command():
    rows = randrange(40, 60)
    cols = randrange(80, 100)
    number_of_points = randrange(200, 300)

    points = []
    for i in range(number_of_points):
        points.append({"x":randrange(1, rows - 2), "y":randrange(1, cols - 2)})
    return {"num_rows":rows, "num_cols":cols, "points":points}


def main():
    if len(sys.argv) == 2:
        # commad 입력 받음
        file = open(sys.argv[1])
        lines = file.readlines()
        command = parse_file(lines)
        save_info = {"is_save":False, "target_generation":0}
        gol = GameOfLife(command, save_info)

    elif len(sys.argv) == 3:
        # 두번째 파라메터의 횟수가 되었을 때 파일을 출력한다.
        file = open(sys.argv[1])
        lines = file.readlines()
        command = parse_file(lines)
        save_info = {"is_save":True, "target_generation":int(sys.argv[2])}
        gol = GameOfLife(command, save_info)

    else:
        # parameter가 없다는 것. 랜덤으로 생성한다.
        command = get_random_command()
        save_info = {"is_save":False, "target_generation":0}
        gol = GameOfLife(command, save_info)

    while gol.state == "waiting":
        key = gol.win.getch()
        if key == ord("s"):
            gol.start()

if __name__ == '__main__':
    main()


