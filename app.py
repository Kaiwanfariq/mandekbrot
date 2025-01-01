import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Read parameters from CSV
def load_parameters():
    df = pd.read_csv("parameters.csv")
    return df

# Mandelbrot calculation function
def mandelbrot(c, max_iter, escape_radius=2.0):
    z = 0
    for n in range(max_iter):
        if abs(z) > escape_radius:
            return n - np.log(np.log(abs(z))) / np.log(2)
        z = z**2 + c
    return max_iter

# Function to generate Mandelbrot set
def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter, escape_radius):
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
    st.write("Use the CSV file to load parameters and explore the Mandelbrot set!")

    # Load parameters from CSV
    parameters = load_parameters()

    # Display available parameters
    st.write("Available Parameters:")
    st.write(parameters)

    # Let user choose which set of parameters to use
    param_index = st.sidebar.selectbox("Select Parameter Set", range(len(parameters)))

    # Get parameters based on user selection
    selected_params = parameters.iloc[param_index]
    xmin = selected_params['xmin']
    xmax = selected_params['xmax']
    ymin = selected_params['ymin']
    ymax = selected_params['ymax']
    width = selected_params['width']
    height = selected_params['height']
    max_iter = selected_params['max_iter']
    colormap = selected_params['colormap']
    zoom = selected_params['zoom']
    escape_radius = selected_params['escape_radius']

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
