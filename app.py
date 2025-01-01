import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Mandelbrot calculation function
def mandelbrot(c, max_iter, escape_radius=2.0):
    """
    Calculate the Mandelbrot set for a complex number 'c'.
    Includes smoothing for better gradients.
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > escape_radius:
            # Smoothing: return iteration count with fractional component
            return n - np.log(np.log(abs(z))) / np.log(2)
        z = z**2 + c
    return max_iter

# Function to generate Mandelbrot set
def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter, escape_radius):
    """
    Generate a Mandelbrot set image.
    """
    real = np.linspace(xmin, xmax, width)
    imag = np.linspace(ymin, ymax, height)
    mandelbrot_set = np.empty((height, width))
    
    for i, y in enumerate(imag):
        for j, x in enumerate(real):
            c = complex(x, y)
            mandelbrot_set[i, j] = mandelbrot(c, max_iter, escape_radius)
    
    return mandelbrot_set

# Main Streamlit app function
def main():
    # App title and description
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
    colormap = st.sidebar.selectbox("Colormap", ["inferno", "plasma", "viridis", "cividis", "magma"])
    zoom = st.sidebar.slider("Zoom Factor", min_value=1.0, max_value=10.0, value=1.0, step=0.1)
    escape_radius = st.sidebar.number_input("Escape Radius", value=2.0, step=0.1, format="%.1f")

    # Adjust the viewing window based on zoom
    center_x = (xmin + xmax) / 2
    center_y = (ymin + ymax) / 2
    width_range = (xmax - xmin) / zoom
    height_range = (ymax - ymin) / zoom
    xmin, xmax = center_x - width_range / 2, center_x + width_range / 2
    ymin, ymax = center_y - height_range / 2, center_y + height_range / 2

    # Debugging: show the parameters in the app
    st.write("Parameters used:")
    st.write(f"xmin: {xmin}, xmax: {xmax}")
    st.write(f"ymin: {ymin}, ymax: {ymax}")
    st.write(f"width: {width}, height: {height}")
    st.write(f"max_iter: {max_iter}")
    st.write(f"colormap: {colormap}")
    st.write(f"zoom: {zoom}")
    st.write(f"escape_radius: {escape_radius}")

    # Generate Mandelbrot set
    st.write("Generating Mandelbrot set with the current parameters...")
    mandelbrot_set = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter, escape_radius)

    # Check if Mandelbrot set is generated correctly
    if mandelbrot_set.size > 0:
        # Display the Mandelbrot set
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.imshow(mandelbrot_set, extent=[xmin, xmax, ymin, ymax], cmap=colormap)
        ax.set_title("Mandelbrot Set")
        ax.set_xlabel("Real")
        ax.set_ylabel("Imaginary")
        st.pyplot(fig)
    else:
        st.write("Error: Mandelbrot set generation failed.")

# Run the app
if __name__ == "__main__":
    main()
