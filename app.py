import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def mandelbrot(c, max_iter):
    """
    Calculate the Mandelbrot set for a complex number 'c'.
    Returns the number of iterations before escaping, or max_iter if bounded.
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    """
    Generate a Mandelbrot set image.
    """
    real = np.linspace(xmin, xmax, width)
    imag = np.linspace(ymin, ymax, height)
    mandelbrot_set = np.empty((height, width))
    
    for i, y in enumerate(imag):
        for j, x in enumerate(real):
            c = complex(x, y)
            mandelbrot_set[i, j] = mandelbrot(c, max_iter)
    
    return mandelbrot_set

def main():
    # Streamlit app title
    st.title("Mandelbrot Set Visualizer")
    st.write("Use the sliders to adjust the parameters and explore the Mandelbrot set!")

    # Sidebar for user input
    st.sidebar.header("Parameters")
    xmin = st.sidebar.number_input("X min", value=-2.0, step=0.1, format="%.1f")
    xmax = st.sidebar.number_input("X max", value=1.0, step=0.1, format="%.1f")
    ymin = st.sidebar.number_input("Y min", value=-1.5, step=0.1, format="%.1f")
    ymax = st.sidebar.number_input("Y max", value=1.5, step=0.1, format="%.1f")
    width = st.sidebar.slider("Image Width (px)", min_value=100, max_value=2000, value=800, step=100)
    height = st.sidebar.slider("Image Height (px)", min_value=100, max_value=2000, value=800, step=100)
    max_iter = st.sidebar.slider("Max Iterations", min_value=10, max_value=1000, value=100, step=10)

    # Generate Mandelbrot set
    st.write("Generating Mandelbrot set with the current parameters...")
    mandelbrot_set = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)

    # Display the Mandelbrot set
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(mandelbrot_set, extent=[xmin, xmax, ymin, ymax], cmap='inferno')
    ax.set_title("Mandelbrot Set")
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    st.pyplot(fig)

if __name__ == "__main__":
    main()
