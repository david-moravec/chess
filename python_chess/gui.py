import tkinter as tk
from PIL import Image
from PIL import ImageTk

class GameBoard(tk.Frame):
    def __init__(self, parent, rows=8, columns=8, size=100, color1="white", color2="blue"):
        '''size is the size of a square, in pixels'''

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        self._drag_data = {"x": 0, "y": 0, "item": None}
        self._click_data = {"x": 0, "y": 0, "item": None}

        # create a couple of movable objects
        #self.create_token(100, 100, "white")
        #self.create_token(200, 100, "black")

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

        self.canvas.tag_bind("token", "<ButtonPress-1>", self.drag_start)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.drag_stop)
        self.canvas.tag_bind("token", "<B1-Motion>", self.drag)
        #self.canvas.tag_bind("token", "<Button-3>", self.click_move)

    def click_move(self, event):
        if not (self._drag_data):
            self._click_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
            self._click_data["x"] = event.x
            self._click_data["y"] = event.y
        else:
            delta_x = event.x - self._click_data["x"]
            delta_y = event.y - self._click_data["y"]
            print(delta_x, delta_y)
            self.canvas.move(self._drag_data["item"], delta_x, delta_y)
            self._click_data["item"] = None
            self._click_data["x"] = 0
            self._click_data["y"] = 0

    def drag_start(self, event):
        """Begining drag of an object"""
        # record the item and its location
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        """End drag of an object"""
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def drag(self, event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def placePieces(self, pieces, root):
        for piece in pieces:
            self.addPiece(piece, root)


    def addPiece(self, piece, root):
        '''Add a piece to the playing board'''
        #root.image = image = tk.PhotoImage(file=r'figures/white-knight.ppm')
        x = piece.x * 100 - 50
        y = piece.y * 100 - 50
        name = piece.name
        #self.canvas.create_image(x,y, image=image)
        self.placepiece(name, y, x)

    def update(self, pieces):
        for piece in pieces:
            self.placepiece(name , piece.y, piece.x)

    def placepiece(self, name, row, column):
        '''Place a piece at the given row/column'''
        #self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    #def create_token(self, x, y, color):
    #    """Create a token at the given coordinate in the given color"""
    #    self.canvas.create_oval(
    #        x - 25,
    #        y - 25,
    #        x + 25,
    #        y + 25,
    #        outline=color,
    #        fill=color,
    #        tags=("token",),
    #    )

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")


if __name__ == "__main__":
    root = tk.Tk()
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()
