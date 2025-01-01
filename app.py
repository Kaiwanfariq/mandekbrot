import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Define the Mandelbrot set function
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Generate the Mandelbrot set image
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    real, imag = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)
    C = np.array([[complex(r, i) for r in real] for i in imag])
    img = np.zeros(C.shape, dtype=int)
    
    for i in range(height):
        for j in range(width):
            img[i, j] = mandelbrot(C[i, j], max_iter)
    
    return img

# Streamlit UI
st.title("Mandelbrot Set Visualization")

# User inputs for the Mandelbrot set parameters
xmin = st.sidebar.number_input("X-Min", -2.0, -1.0, -2.0)
xmax = st.sidebar.number_input("X-Max", 0.0, 2.0, 1.0)
ymin = st.sidebar.number_input("Y-Min", -2.0, -1.0, -1.5)
ymax = st.sidebar.number_input("Y-Max", 0.0, 2.0, 1.5)
width = st.sidebar.slider("Resolution (Width)", 100, 2000, 800)
height = st.sidebar.slider("Resolution (Height)", 100, 2000, 800)
max_iter = st.sidebar.slider("Max Iterations", 50, 1000, 256)

# Generate Mandelbrot set image based on user input
img = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

# Plot the Mandelbrot set using Matplotlib
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img, cmap='hot', extent=(xmin, xmax, ymin, ymax))
ax.set_title("Mandelbrot Set")
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")

# Display the plot in Streamlit
st.pyplot(fig)

# Display a color bar for reference
st.write("Color bar represents the number of iterations before escaping.")
