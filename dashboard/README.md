# 🚇 MRT-3 Ridership Dashboard

A comprehensive Streamlit dashboard for analyzing Metro Rail Transit Line 3 ridership data from 1999 to 2025. This dashboard provides interactive visualizations and insights similar to the DOTR Railway Sector Datasets website.

## 📊 Features

### Overview Dashboard
- **Key Metrics**: Total ridership, average daily ridership, peak daily ridership, and data coverage
- **Annual Trends**: Yearly ridership totals and year-over-year growth analysis
- **Monthly Patterns**: Heatmap visualization of monthly ridership patterns
- **Key Insights**: Data coverage and growth trend summaries

### Trend Analysis
- **Time Series**: Daily ridership over time with interactive zooming
- **Moving Averages**: 30-day and 90-day moving averages for trend identification
- **Decade Comparison**: Analysis of ridership patterns across different decades

### Seasonal Patterns
- **Monthly Analysis**: Average daily ridership by month
- **Seasonal Heatmap**: Monthly ridership patterns by year
- **Day of Month Patterns**: Analysis of ridership by day of the month
- **Seasonal Insights**: Ridership patterns by season (Winter, Spring, Summer, Fall)

### Statistical Analysis
- **Descriptive Statistics**: Comprehensive statistical summary
- **Distribution Analysis**: Histogram and box plot visualizations
- **Correlation Analysis**: Correlation matrix between variables
- **Outlier Detection**: Identification and visualization of outliers

### Predictive Analysis
- **Trend Projections**: 5-year ridership forecasts
- **Growth Rate Analysis**: Projected growth rates
- **Seasonal Forecasting**: Monthly pattern-based forecasting

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Clone or download the project files**
   ```bash
   # If using git
   git clone <repository-url>
   cd mrt
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**
   ```bash
   streamlit run dashboard.py
   ```

4. **Access the dashboard**
   - Open your web browser
   - Navigate to `http://localhost:8501`
   - The dashboard will load automatically

## 📁 Project Structure

```
mrt/
├── dashboard.py              # Main Streamlit dashboard application
├── requirements.txt          # Python dependencies
├── README.md                # This file
└── mrt-3/
    ├── data/
    │   ├── cleaned_ridership_data.csv    # Main dataset
    │   ├── DAILY RIDERSHIP FROM 1999 (58).xlsx
    │   └── ridership (2).xlsx
    ├── mrt-3.ipynb          # Original analysis notebook
    └── wide format.ipynb     # Data processing notebook
```

## 🎛️ Dashboard Controls

### Sidebar Options
- **Year Range Slider**: Filter data by specific year ranges
- **Analysis Type Selector**: Choose between different analysis views:
  - Overview
  - Trend Analysis
  - Seasonal Patterns
  - Statistical Analysis
  - Predictions

### Interactive Features
- **Zoom and Pan**: All charts support interactive zooming and panning
- **Hover Information**: Detailed information on hover over data points
- **Responsive Layout**: Dashboard adapts to different screen sizes
- **Real-time Filtering**: Data updates automatically when filters change

## 📈 Data Insights

### Key Findings from the Analysis
- **Historical Growth**: MRT-3 has experienced significant growth since its inception
- **Seasonal Patterns**: Clear monthly and seasonal variations in ridership
- **Impact Events**: Notable drops during major events (e.g., COVID-19 pandemic)
- **Recovery Trends**: Post-event recovery patterns and growth trajectories

### Data Quality
- **Coverage**: Comprehensive data from 1999 to 2025
- **Completeness**: High data completeness with minimal missing values
- **Accuracy**: Validated ridership numbers from official sources

## 🛠️ Technical Details

### Technologies Used
- **Streamlit**: Web application framework
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib/Seaborn**: Additional plotting capabilities

### Performance Features
- **Caching**: Data loading is cached for faster performance
- **Responsive Design**: Optimized for various screen sizes
- **Efficient Processing**: Optimized data processing for large datasets

## 🔧 Customization

### Adding New Visualizations
1. Create new functions in `dashboard.py`
2. Add new analysis types to the sidebar selector
3. Update the main function to include new views

### Modifying Data Sources
1. Update the `load_data()` function in `dashboard.py`
2. Ensure data format matches expected structure
3. Update preprocessing steps as needed

### Styling Changes
- Modify the CSS in the `st.markdown()` section
- Update color schemes and layout parameters
- Customize chart themes in Plotly configurations

## 📞 Support

For questions or issues:
1. Check the data format matches the expected structure
2. Ensure all dependencies are properly installed
3. Verify Python version compatibility
4. Check console output for error messages

## 📄 License

This project is for educational and analytical purposes. Please ensure proper attribution when using the analysis or visualizations.

## 🔄 Updates

### Version 1.0
- Initial dashboard release
- Comprehensive analysis modules
- Interactive visualizations
- Responsive design

---

**Note**: This dashboard is designed to provide insights into MRT-3 ridership patterns and should be used as a tool for understanding public transportation trends in Metro Manila.
