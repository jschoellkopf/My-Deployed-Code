# Given an array arr of strings, complete the function by calculating the total perimeter of all the islands. Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1 piece of land. Some examples for better visualization:

# ['XOOXO',
#  'XOOXO',
#  'OOOXO',
#  'XXOXO',
#  'OXOOO'] 
# which represents:

# should return: "Total land perimeter: 24".

# Following input:

# ['XOOO',
#  'XOXO',
#  'XOXO',
#  'OOXX',
#  'OOOO']
# which represents:

# should return: "Total land perimeter: 18"

def land_perimeter(arr):
    sides,rows,cols = 0,len(arr),len(arr[0])
    print("num of columns",cols, "num of rows",rows)
    for row in range(rows):
        # going through each row
        print(f"this is row {row+1}", arr[row])
        for col in range(cols):
            # going through each column
            if arr[row][col] == "X":
                sides += 4
                # since there's an X, it has 4 sides, and now checking if any other x is adjacent, if so, take away a side
                print(f'this X is col {col+1}')
                if arr[row][col-1] == "X" and col-1 >= 0:
                    # using [col-1] for as an index takes the first character from the end because of the '-' sign
                    # we have to add a condition to make sur col-1 !< 0
                    sides -= 1
                    print('X on the left')
                if arr[row-1][col] == "X" and row-1 >= 0:
                    sides -= 1
                    print('X above')
                if col+1 < cols:
                    if arr[row][col+1] == "X":
                        sides -= 1
                        print('X on the right')
                if row+1 < rows:
                    if arr[row+1][col] == "X":
                        sides -= 1
                        print('X below')
    return f'Total land perimeter: {sides}'

print(land_perimeter(['XOOXX','XOOXO','OOOXX','XXOXO','OXOOO'] ))
# print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]))
# print(land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]), "Total land perimeter: 52")
# print(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]), "Total land perimeter: 40")
# print(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]), "Total land perimeter: 54")
# print(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]), "Total land perimeter: 40")