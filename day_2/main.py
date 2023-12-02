import re

R_LIMIT = 12
G_LIMIT = 13
B_LIMIT = 14

def main():
    with open("input.txt", "r") as f:
        input_data = f.read().splitlines()
    total = 0
    total_power = 0
    for row in input_data:
        possible = True
        r = 0
        g = 0
        b = 0
        id, game = row.split(":")
        print(f"Processing game {id}")
        draws = game.split(";")
        for draw in draws:
            print(f"Processing draw {draw}")
            draw = draw.split(",")
            for cube in draw:
                cube = cube.strip()
                count = int(re.findall(r'^[^\d]*(\d+)', cube)[0])
                if "red" in cube:
                    if count > r:
                        r = count
                elif "green" in cube:
                    if count > g:
                        g = count
                elif "blue" in cube:
                    if count > b:
                        b = count
        id = int(re.findall(r'^[^\d]*(\d+)', id)[0])

        if not any([r > R_LIMIT, g > G_LIMIT, b > B_LIMIT]):
            total += id

        ## Part 2
        power = r * g * b
        total_power += power

    print(f"Part 1: {total}")
    print(f"Part 2: {total_power}")

if __name__ == "__main__":
    main()
