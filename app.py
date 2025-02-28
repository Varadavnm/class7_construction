import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from flask import Flask, render_template, send_file
import io

app = Flask(__name__)

def create_animation():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Draw x-axis (baseline)
    base_line, = ax.plot([], [], "k-", linewidth=2)  # Base line
    semicircle, = ax.plot([], [], "b--")  # Semicircle arc
    mark_60, = ax.plot([], [], "ro")  # First 60-degree mark
    mark_120, = ax.plot([], [], "ro")  # Second 60-degree mark
    bisection_arc, = ax.plot([], [], "g--")  # Bisection arc
    final_angle_line, = ax.plot([], [], "r-", linewidth=2)  # Final 45-degree line

    def init():
        base_line.set_data([], [])
        semicircle.set_data([], [])
        mark_60.set_data([], [])
        mark_120.set_data([], [])
        bisection_arc.set_data([], [])
        final_angle_line.set_data([], [])
        return base_line, semicircle, mark_60, mark_120, bisection_arc, final_angle_line

    def update(frame):
        if frame < 10:
            # Draw base line
            base_line.set_data([0, 8], [0, 0])
        elif frame < 20:
            # Draw semicircle
            theta = np.linspace(0, np.pi, 30)
            x = 4 + 4 * np.cos(theta)
            y = 4 * np.sin(theta)
            semicircle.set_data(x, y)
        elif frame < 30:
            # Mark first 60-degree intersection
            mark_60.set_data(8, 0)
        elif frame < 40:
            # Mark second 60-degree intersection (120-degree point)
            mark_120.set_data(4, 4)
        elif frame < 50:
            # Draw arcs for angle bisection
            theta = np.linspace(0, np.pi/2, 20)
            arc_x = 4 + 3 * np.cos(theta)
            arc_y = 3 * np.sin(theta)
            bisection_arc.set_data(arc_x, arc_y)
        else:
            # Draw final 45-degree line
            final_angle_line.set_data([0, 4], [0, 4])
        
        return base_line, semicircle, mark_60, mark_120, bisection_arc, final_angle_line

    ani = animation.FuncAnimation(fig, update, frames=60, init_func=init, interval=100)

    # Save as GIF
    buf = io.BytesIO()
    ani.save(buf, format="gif", writer="pillow", fps=10)
    buf.seek(0)
    return buf

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/animation")
def get_animation():
    gif = create_animation()
    return send_file(gif, mimetype="image/gif")

if __name__ == "__main__":
    app.run(debug=True)
