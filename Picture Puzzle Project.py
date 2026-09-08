import tkinter as tk
from tkinter import messagebox
import numpy as np
from PIL import Image, ImageTk, ImageDraw
import time
import random
import os

# -------------------------------------------------------------------
# CONFIGURATION: Relative file path
# -------------------------------------------------------------------
IMAGE_PATH = "LinkedIn Banner.png"


def prepare_image(image_path, target_w, target_h, grid_size=3):
    """
    Loads an image from disk (or generates a fallback if missing),
    resizes it to (target_w, target_h), and draws tile numbers for readability.
    """
    if os.path.exists(image_path):
        img = Image.open(image_path).convert("RGB")
        img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    else:
        # Fallback widescreen synthetic test image
        img = Image.new("RGB", (target_w, target_h), color=(240, 240, 240))
        draw = ImageDraw.Draw(img)
        
        # Quadrant blocks
        draw.rectangle([0, 0, target_w//2, target_h//2], fill=(231, 76, 60))        # Red Top-Left
        draw.rectangle([target_w//2, 0, target_w, target_h//2], fill=(46, 204, 113))    # Green Top-Right
        draw.rectangle([0, target_h//2, target_w//2, target_h], fill=(52, 152, 219))    # Blue Bottom-Left
        draw.rectangle([target_w//2, target_h//2, target_w, target_h], fill=(241, 196, 15)) # Yellow Bottom-Right
        
        draw.text((20, 20), "NUMPY WIDESCREEN PUZZLE", fill="white")

    # Draw small numbered badges on every tile
    draw = ImageDraw.Draw(img)
    tile_w = target_w // grid_size
    tile_h = target_h // grid_size
    tile_count = 1

    for r in range(grid_size):
        for c in range(grid_size):
            x = c * tile_w + 10
            y = r * tile_h + 10
            # Small semi-transparent background box for numbers
            draw.rectangle([x, y, x + 24, y + 24], fill=(0, 0, 0))
            draw.text((x + 7, y + 5), str(tile_count), fill=(255, 255, 255))
            tile_count += 1

    # Return 3D NumPy array: Shape (Height, Width, Color Channels)
    return np.array(img)


# -------------------------------------------------------------------
# NUMPY PUZZLE ENGINE
# -------------------------------------------------------------------
class NumPyPuzzleEngine:
    def __init__(self, image_path, width, height, grid_size=3):
        self.grid_size = grid_size
        self.total_tiles = grid_size * grid_size
        self.image_path = image_path
        
        # Initialize array structure
        self.resize_and_rebuild(width, height)
        
        # Track shuffled tile order
        self.current_order = list(range(self.total_tiles))
        self.scramble()

    def resize_and_rebuild(self, width, height):
        """Re-scales the NumPy matrices when the window is resized."""
        self.width = width
        self.height = height
        self.tile_w = width // self.grid_size
        self.tile_h = height // self.grid_size

        # 1. Load/Scale Image to new matrix dimensions
        self.original_array = prepare_image(self.image_path, width, height, self.grid_size)
        
        # 2. Slice array into sub-matrices
        self.original_tiles = self._slice_tiles(self.original_array)

    def _slice_tiles(self, img_array):
        """Slices the main 3D array into a list of sub-array tiles."""
        tiles = []
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                r_start, r_end = r * self.tile_h, (r + 1) * self.tile_h
                c_start, c_end = c * self.tile_w, (c + 1) * self.tile_w
                tile = img_array[r_start:r_end, c_start:c_end, :]
                tiles.append(tile)
        return tiles

    def scramble(self):
        """Randomly scrambles tile order."""
        while True:
            random.shuffle(self.current_order)
            if self.current_order != list(range(self.total_tiles)):
                break

    def swap_tiles(self, idx1, idx2):
        """Swaps two tile positions in the grid."""
        self.current_order[idx1], self.current_order[idx2] = (
            self.current_order[idx2],
            self.current_order[idx1],
        )

    def assemble_current_array(self):
        """Reconstructs the 3D array using NumPy horizontal & vertical block stacking."""
        ordered_tiles = [self.original_tiles[i] for i in self.current_order]
        rows = []
        for r in range(self.grid_size):
            row_tiles = ordered_tiles[r * self.grid_size : (r + 1) * self.grid_size]
            row_concat = np.hstack(row_tiles)
            rows.append(row_concat)
        return np.vstack(rows)

    def verify_solution(self):
        """
        Checks if current tile sequence matches the solved order [0, 1, ..., N-1].
        This ensures 100% reliable victory detection regardless of image interpolation noise.
        """
        return self.current_order == list(range(self.total_tiles))


# -------------------------------------------------------------------
# TKINTER RESIZABLE GUI INTERFACE
# -------------------------------------------------------------------
class PuzzleApp:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path
        self.root.title("NumPy Resizable Photo Puzzle")
        
        # Default Widescreen Size (800x600)
        self.width = 800
        self.height = 600
        self.root.geometry(f"{self.width}x{self.height + 60}")
        self.root.minsize(400, 300)

        self.grid_size = 3
        self.selected_tile = None
        self.game_state = "PREVIEW"

        self.start_time = 0
        self.preview_timer = 3
        self._resize_job = None

        # UI Setup
        self._setup_ui()
        self.start_game()

    def _setup_ui(self):
        # Header Panel
        self.header_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        self.header_frame.pack(fill=tk.X, side=tk.TOP)

        self.label_title = tk.Label(
            self.header_frame, text="Widescreen Puzzle", font=("Arial", 14, "bold"), fg="#f1c40f", bg="#2c3e50"
        )
        self.label_title.pack(side=tk.LEFT, padx=20, pady=10)

        self.label_status = tk.Label(
            self.header_frame, text="Memorize Picture!", font=("Arial", 12, "bold"), fg="#2ecc71", bg="#2c3e50"
        )
        self.label_status.pack(side=tk.LEFT, padx=20, pady=10)

        self.label_timer = tk.Label(
            self.header_frame, text="Time: 0s", font=("Arial", 14, "bold"), fg="#ffffff", bg="#2c3e50"
        )
        self.label_timer.pack(side=tk.RIGHT, padx=20, pady=10)

        # Canvas Area
        self.canvas = tk.Canvas(self.root, bg="#000000", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bindings
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.root.bind("<Configure>", self.on_window_resize)

    def start_game(self):
        self.puzzle = NumPyPuzzleEngine(self.image_path, self.width, self.height, self.grid_size)
        self.game_state = "PREVIEW"
        self.selected_tile = None
        self.preview_timer = 3

        self.label_status.config(text=f"Memorize Image! Scrambling in: {self.preview_timer}s", fg="#2ecc71")
        self.label_timer.config(text="Time: 0s")

        self.display_numpy_array(self.puzzle.original_array)
        self.root.after(1000, self.update_preview_countdown)

    def update_preview_countdown(self):
        if self.game_state != "PREVIEW":
            return

        self.preview_timer -= 1
        if self.preview_timer > 0:
            self.label_status.config(text=f"Memorize Image! Scrambling in: {self.preview_timer}s")
            self.root.after(1000, self.update_preview_countdown)
        else:
            self.game_state = "PLAYING"
            self.label_status.config(text="Click 2 tiles to swap them", fg="#f1c40f")
            self.start_time = time.time()
            self.render_board()
            self.update_live_timer()

    def update_live_timer(self):
        if self.game_state == "PLAYING":
            elapsed = int(time.time() - self.start_time)
            self.label_timer.config(text=f"Time: {elapsed}s")
            self.root.after(500, self.update_live_timer)

    def on_window_resize(self, event):
        if event.widget == self.root:
            new_w = event.width
            new_h = event.height - 60

            if new_w > 100 and new_h > 100 and (new_w != self.width or new_h != self.height):
                self.width = new_w
                self.height = new_h

                if self._resize_job:
                    self.root.after_cancel(self._resize_job)
                self._resize_job = self.root.after(150, self._apply_resize)

    def _apply_resize(self):
        self.puzzle.resize_and_rebuild(self.width, self.height)
        if self.game_state == "PREVIEW":
            self.display_numpy_array(self.puzzle.original_array)
        else:
            self.render_board()

    def display_numpy_array(self, img_array):
        pil_img = Image.fromarray(img_array)
        self.tk_image = ImageTk.PhotoImage(pil_img)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def render_board(self):
        current_array = self.puzzle.assemble_current_array()
        self.display_numpy_array(current_array)

        # Draw Grid Lines
        tile_w = self.puzzle.tile_w
        tile_h = self.puzzle.tile_h

        for i in range(1, self.grid_size):
            self.canvas.create_line(i * tile_w, 0, i * tile_w, self.height, fill="#000000", width=2)
            self.canvas.create_line(0, i * tile_h, self.width, i * tile_h, fill="#000000", width=2)

        # Highlight selected tile
        if self.selected_tile is not None:
            r = self.selected_tile // self.grid_size
            c = self.selected_tile % self.grid_size
            self.canvas.create_rectangle(
                c * tile_w, r * tile_h,
                (c + 1) * tile_w, (r + 1) * tile_h,
                outline="#f1c40f", width=4
            )

    def on_canvas_click(self, event):
        if self.game_state != "PLAYING":
            return

        col = event.x // self.puzzle.tile_w
        row = event.y // self.puzzle.tile_h
        
        col = min(col, self.grid_size - 1)
        row = min(row, self.grid_size - 1)
        clicked_idx = row * self.grid_size + col

        if self.selected_tile is None:
            self.selected_tile = clicked_idx
            self.render_board()
        else:
            self.puzzle.swap_tiles(self.selected_tile, clicked_idx)
            self.selected_tile = None
            self.render_board()

            # Check victory condition
            if self.puzzle.verify_solution():
                self.game_state = "WON"
                completion_time = round(time.time() - self.start_time, 2)
                
                response = messagebox.askyesno(
                    "Puzzle Solved!",
                    f"🎉 Excellent! Puzzle completed in {completion_time} seconds.\n\n"
                    "Would you like to try again?"
                )
                
                if response:
                    self.start_game()
                else:
                    self.root.destroy()


# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleApp(root, IMAGE_PATH)
    root.mainloop()