import tkinter as tk
from tkinter import Canvas


class Shape:
    def __init__(self, canvas: Canvas, x: int = 60, y: int = 50, color: str = "black", fill: str | None = None, line: int = 2):
        self.canvas: Canvas = canvas
        self.color: str = color
        self.fill: str | None = fill
        self.line: int = line
        self.x_position: int = x
        self.y_position: int = y
        self.is_visible: bool = False
        self.shape_id: int | None = None

    def draw(self) -> None:
        pass

    def erase(self) -> None:
        if self.is_visible and self.shape_id is not None:
            self.canvas.delete(self.shape_id)
            self.shape_id = None
            self.is_visible = False

    def make_visible(self) -> None:
        self.is_visible = True
        self.draw()

    def make_invisible(self) -> None:
        self.is_visible = False
        self.erase()

    def change_size(self, new_size: int) -> None:
        self.erase()
        self.size: int = new_size
        self.draw()

    def change_color(self, new_color: str) -> None:
        self.color = new_color
        self.draw()

    def move_right(self)  -> None:
        self.move_horizontal(20)

    def move_left(self) -> None:
        self.move_horizontal(-20)

    def move_up(self) -> None:
        self.move_vertical(-20)

    def move_down(self) -> None:
        self.move_vertical(20)

    def move_horizontal(self, distance: int) -> None:
        self.erase()
        self.x_position += distance
        self.draw()

    def move_vertical(self, distance: int) -> None:
        self.erase()
        self.y_position += distance
        self.draw()
