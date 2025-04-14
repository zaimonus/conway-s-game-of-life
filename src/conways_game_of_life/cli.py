from conways_game_of_life.game import Game
from conways_game_of_life.rules import (
    RULE_DIE_LESS_THAN_TWO,
    RULE_DIE_MORE_THAN_THREE,
    RULE_POPULATE_WHEN_THREE,
    RULE_SURVIVE_TWO_OR_THREE,
)


def main():
    g = Game()
    g.add_rule(RULE_DIE_LESS_THAN_TWO)
    g.add_rule(RULE_DIE_MORE_THAN_THREE)
    g.add_rule(RULE_SURVIVE_TWO_OR_THREE)
    g.add_rule(RULE_POPULATE_WHEN_THREE, False)

    g.add_cell(0, 1)
    g.add_cell(1, 0)
    g.add_cell(-1, 0)

    for _ in range(100):
        print(g.cells)
        g.step()
