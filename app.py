# Deployment wrapper for MRT-3 Dashboard
# This file allows deployment platforms to find the dashboard at the expected location

import sys
import os

# Add the dashboard directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'dashboard'))

# Import and run the main dashboard
from dashboard import main

if __name__ == "__main__":
    main()
