from conways_game_of_life.game import Cell


def RULE_DIE_LESS_THAN_TWO(cell: Cell, neighbor_cells: set[Cell]) -> bool:
    # 1. Each cell with one or no neighbors **dies**.
    if len(neighbor_cells) <= 1:
        return False
    return True


def RULE_DIE_MORE_THAN_THREE(cell: Cell, neighbor_cells: set[Cell]) -> bool:
    # 2. Each cell with four or more neighbors **dies**.
    if len(neighbor_cells) >= 4:
        return False
    return True


def RULE_SURVIVE_TWO_OR_THREE(cell: Cell, neighbor_cells: set[Cell]) -> bool:
    # 3. Each cell with two or three neighbors **survives**.
    if len(neighbor_cells) in {2, 3}:
        return True
    return False


def RULE_POPULATE_WHEN_THREE(cell: Cell, neighbor_cells: set[Cell]) -> bool:
    # 4. Each cell with three neighbors becomes **populated**.
    if len(neighbor_cells) == 3:
        return True
    return False
