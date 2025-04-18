from time import sleep
from conways_game_of_life.game import Cell, Game
from conways_game_of_life.rules import (
    RULE_DIE_LESS_THAN_TWO,
    RULE_DIE_MORE_THAN_THREE,
    RULE_POPULATE_WHEN_THREE,
    RULE_SURVIVE_TWO_OR_THREE,
)


def print_grid(cells: set[Cell], width: int, height: int):
    print("+", " ".join("-" * (width * 2 + 1)), "+")
    for y in range(-height, height):
        row = [
            "x" if Cell(x, y) in cells else " "
            for x in range(-width, width + 1)
        ]
        print("|", " ".join(row), "|")
    print("+", " ".join("-" * (width * 2 + 1)), "+")


def main():
    g = Game()
    g.add_rule(RULE_DIE_LESS_THAN_TWO)
    g.add_rule(RULE_DIE_MORE_THAN_THREE)
    g.add_rule(RULE_SURVIVE_TWO_OR_THREE)
    g.add_rule(RULE_POPULATE_WHEN_THREE, False)

    g.add_cell(-5, -3)
    g.add_cell(-4, -3)
    g.add_cell(-4, -5)
    g.add_cell(-3, -3)
    g.add_cell(-3, -4)

    while len(g.cells) > 0:
        print_grid(g.cells, 10, 10)
        g.step()
        sleep(1)
