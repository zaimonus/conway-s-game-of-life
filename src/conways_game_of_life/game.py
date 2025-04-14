from collections.abc import Callable
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Cell:
    x: int = field(hash=True)
    y: int = field(hash=True)

    def neighbors(self):
        return {
            Cell(self.x + xd, self.y + yd)
            for xd in {1, 0, -1}
            for yd in {1, 0, -1}
            if not (xd == yd == 0)
        }


type Rule = Callable[[Cell, set[Cell]], bool]


@dataclass
class Game:
    cells: set[Cell] = field(default_factory=set)
    killing_rules: set[Rule] = field(default_factory=set)
    creating_rules: set[Rule] = field(default_factory=set)

    def add_cell(self, x: int, y: int):
        self.cells.add(Cell(x, y))

    def remove_cell(self, x: int, y: int):
        cell = Cell(x, y)
        self.cells.discard(cell)

    def add_rule(self, rule: Rule, killing: bool = True):
        if killing:
            self.killing_rules.add(rule)
        else:
            self.creating_rules.add(rule)

    def remove_rule(self, rule: Rule):
        self.killing_rules.discard(rule)
        self.creating_rules.discard(rule)

    def _step(self):
        surviving: set[Cell] = set(self.cells)
        empty: set[Cell] = {
            n for cell in self.cells for n in cell.neighbors()
        } - self.cells

        for rule in self.killing_rules:
            surviving = {
                cell
                for cell in surviving
                if rule(cell, cell.neighbors() & self.cells)
            }

        for rule in self.creating_rules:
            empty = {
                cell
                for cell in empty
                if rule(cell, cell.neighbors() & self.cells)
            }

        self.cells = surviving | empty

    def step(self, steps: int = 1):
        for _ in range(steps):
            self._step()
