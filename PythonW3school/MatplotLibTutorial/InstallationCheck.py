try:
    import matplotlib
    print("Matplotlib is installed.")
except ImportError:
    print("Matplotlib is not installed.")


# Check version
print("Matplotlib version:", matplotlib.__version__)

# Get backend
print("Matplotlib backend:", matplotlib.get_backend())

# List all available styles
print("Available styles:", matplotlib.style.available)
