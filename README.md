# 🎁 Amazing Box

**Amazing Box** is a dynamic 2D OpenGL-based animation in Python where colorful points bounce within a window, change directions, and blink on command. It's interactive, fun to play with, and showcases animation logic using PyOpenGL and GLUT.

---

## 🚀 Features

- 🌈 Randomly colored points
- 🖱️ Right-click to create new points at mouse position
- 💡 Left-click to toggle blinking effect
- ⏸️ Spacebar to freeze/unfreeze movement
- 🔼 Increase speed with UP arrow key
- 🔽 Decrease speed with DOWN arrow key
- ⛔ Points bounce off the window edges
- 👀 View coordinates printed on point creation

---

## 🛠️ Requirements

- Python 3.x
- `PyOpenGL`
- `PyOpenGL_accelerate` (optional for better performance)

You can install the required libraries using pip:

```bash
pip install PyOpenGL PyOpenGL_accelerate
🧠 How It Works
🎯 Point Creation
On right-click, a new point is added at the cursor location (converted to OpenGL coordinates).

Each point has:

A random direction

A random RGB color

A bouncing behavior

✨ Blinking Animation
Left-click toggles blinking mode.

When blinking is ON, points toggle between visible and invisible every 500ms.

🕹️ Controls
Input | Action

Right Mouse Click | Add a new point
Left Mouse Click | Toggle blinking on/off
Spacebar | Freeze/unfreeze all movement
Up Arrow | Increase speed
Down Arrow | Decrease speed
🖥️ Running the Program
Simply run the Python file:

bash
python amazing_box.py
You’ll see a 600x600 window titled "Amazing Box".
