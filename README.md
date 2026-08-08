# Python Snake Game

A classic Snake game built using Python's built-in `turtle` graphics module, structured with modular object-oriented programming (OOP) principles, and featuring persistent high score tracking via local file I/O.

**Repository:** [https://github.com/AmoghChhuneja/Retro-Snake-Game](https://github.com/AmoghChhuneja/Retro-Snake-Game)

---

## Features

* **Modular Architecture:** Clean separation of concerns into different classes (`Snake`, `Food`, `ScoreBoard`).
* **High Score Tracking:** Automatically saves and loads your highest score locally using a `data.txt` file.
* **Collision Detection:**
  * Detects when the snake eats food to grow longer and increase the score.
  * Resets the game seamlessly if the snake hits the boundaries or crashes into itself.
* **Smooth Controls:** Responsive arrow key inputs with logic preventing the snake from instantly reversing into itself.

---

## Project Structure

```text
├── main.py          # Main game loop, screen setup, and collision logic
├── snake.py         # Snake initialization, movement, and controls
├── food.py          # Food generation and random positioning
├── score_board.py   # Score tracking, display, and high score file handling
└── data.txt          # Local file storing the persistent high score
```

---

## Requirements

This project is built entirely using Python's standard library. No external third-party packages need to be installed via pip.

* **Python:** Version 3.x

---

## How to Run

1. Clone this repository to your local machine:

```bash
git clone https://github.com/AmoghChhuneja/Retro-Snake-Game.git
```

2. Navigate into the project directory:

```bash
cd Retro-Snake-Game
```

3. Ensure all project files (`main.py`, `snake.py`, `food.py`, `score_board.py`, and `data.txt`) are in the same directory.
4. Run the game:

```bash
python main.py
```

---

## Controls

Use the arrow keys on your keyboard to navigate the snake:

| Key | Action |
|-----|--------|
| ↑ Up Arrow | Move Up |
| ↓ Down Arrow | Move Down |
| ← Left Arrow | Move Left |
| → Right Arrow | Move Right |