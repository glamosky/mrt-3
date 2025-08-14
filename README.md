# MRT-3 Ridership Dashboard

A comprehensive Streamlit dashboard for analyzing Metro Rail Transit Line 3 ridership data from 1999 to March 2025.

## Quick Start (Deployment)

This repository is structured for easy deployment on platforms like Streamlit Cloud, Heroku, or similar services.

### For Deployment Platforms:
- **Main file**: `dashboard.py` (in root directory)
- **Requirements**: `requirements.txt` (in root directory)
- **Data**: Located in `data/cleaned_ridership_data.csv`

### Local Development:
For local development, navigate to the dashboard folder:
```bash
cd dashboard
streamlit run dashboard.py
```

## Project Structure

```
mrt-3/
├── dashboard.py              # Deployment entry point
├── requirements.txt          # Deployment dependencies
├── README.md                # This file
├── data/
│   └── cleaned_ridership_data.csv    # Main dataset
├── mrt-3.ipynb              # Original analysis notebook
├── wide format.ipynb         # Data processing notebook
└── dashboard/                # Dashboard application folder
    ├── dashboard.py          # Main Streamlit dashboard application
    ├── requirements.txt      # Python dependencies
    ├── environment.yml       # Conda environment file
    └── README.md             # Detailed documentation
```

## Features

- **Interactive Visualizations**: Comprehensive charts and graphs
- **Real-time Filtering**: Filter data by year ranges
- **Multiple Analysis Views**: Overview, Trends, Seasonal Patterns, Statistics, Predictions
- **Responsive Design**: Works on desktop and mobile devices

## Data Source

The dashboard uses official MRT-3 ridership data obtained through Freedom of Information requests, covering daily ridership from 1999 to March 2025.

For detailed documentation, see `dashboard/README.md`.
