def valid_triangle(intList):
    a, b, c = intList
    return (a+b)>c and (a+c)>b and (b+c)>a

def part_one(triangleList):
    return [valid_triangle(x) for x in triangleList].count(True)

def parse_columns(triangleList):
    pass

def part_two(triangleList):
    pass

if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()
        lists = [x.split() for x in lines]
        inputs = [[int(x) for x in y] for y in lists]
        print(part_one(inputs))
