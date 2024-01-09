import os
import time

class Pos:
    def __init__(self, y=None, x=None):
        self.y = y
        self.x = x

class Maze:
    def __init__(self) -> None:
        self.maze = [
             ["X", "X", "X", "X", "X", "X", "X"],
              ["X", " ", " ", " ", "X", " ", "X"],
              ["X", " ", "X", " ", "X", " ", " "],
              ["X", " ", "X", " ", "X", " ", "X"],
              ["X", " ", "X", " ", " ", " ", "X"],
              ["X", " ", "X", "X", "X", "X", "X"],
        ]
        self.ply = Pos(5, 1)
        self.end = Pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"

    def is_in_bound(self, y, x):
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])

    def print_board(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col, " ", end="")
            print("")
        print("\n\n\n")

    def print_end(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congratulation!!! <<<<<")
        print("\n\n\n")

    def move(self, direction):
        directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        dy, dx = directions.get(direction, (0, 0))
        next_move = Pos(self.ply.y + dy, self.ply.x + dx)

        if self.is_in_bound(next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] in [" ", "E"]:
            self.maze[self.ply.y][self.ply.x] = " "
            self.maze[next_move.y][next_move.x] = "P"
            self.ply = next_move
            time.sleep(0.25)

            if self.maze[next_move.y][next_move.x] == "E":
                self.print_end()
                return False

        return True

    def solve_maze_dfs(self):
        stack = [(self.ply.y, self.ply.x)]

        while stack:
            y, x = stack.pop()

            if not self.is_in_bound(y, x) or self.maze[y][x] in ["X", "P", "."]:
                continue

            if self.maze[y][x] == "E":
                self.print_end()
                return

            self.maze[y][x] = "."
            self.print_board()
            time.sleep(0.25)

            stack.append((y - 1, x))
            stack.append((y + 1, x))
            stack.append((y, x - 1))
            stack.append((y, x + 1))

        print(">>>>> Congraturation!!! <<<<<")

if __name__ == "__main__":
    m = Maze()
    m.print_board()

    u, r, d = 1, 1, 1

    while u <= 4 and m.move("up"):
        m.print_board()
        u += 1
    u = 1

    while r <= 2 and m.move("right"):
        m.print_board()
        r += 1
    r = 1

    while d <= 3 and m.move("down"):
        m.print_board()
        d += 1
    d = 1

    while r <= 2 and m.move("right"):
        m.print_board()
        r += 1
    r = 1

    while u <= 2 and m.move("up"):
        m.print_board()
        u += 1
    u = 1

    while r <= 1 and m.move("right"):
        m.print_board()
        r += 1

    m.solve_maze_dfs()
