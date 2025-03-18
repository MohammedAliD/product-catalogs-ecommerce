import os
import sys

# Get the absolute path of the project root directory
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project root directory to Python path
sys.path.insert(0, root_dir)