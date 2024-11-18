# Stock_Data_Automation


This project automates the extraction, formatting, and visualization of stock data from Yahoo Finance for further data analysis using Python. The tool gathers real-time data for selected stocks, performs basic data transformation and cleaning, and generates visualizations in an Excel report. 

*All you have to do is input your stock ticker and watch as your stock data report is automatically geenrated!!*

## Features


- Extracts live stock data from Yahoo Finance using web scraping.
- Converts data into user-friendly formats in an Excel report.
- Generates bar charts, scatter plots, and clustered column charts.
- Fully automated workflow for regularly updating stock data and visualizations.


## Prerequisites


- Python 3.x
- Libraries required: **openpyxl**, **pandas**, **requests**, **BeautifulSoup4**.


```bash
pip install -r requirements.txt
```


## Installation


1. **Clone the repository:**


   ```bash
   git clone https://github.com/yourusername/Stock-Data-Automation.git
   ```

3. **Navigate to the project directory**


```bash
cd Stock-Data-Automation
```

3. **Install the required Python package**


```bash
pip install -r requirements.txt
```


## Project Structure


The project  is divided into modular scripts for readability and ease of maintainance, each serving its different purpose:

- **Stock_Ticker.py** : Where your stock data to be scraped are inputed

- **script.py** : Where your stock data is scraped from Yahoo Finance

- **Data_cleaning.py** : Hnadles the cleaning and preprocessing of the stock data

- **Column_chart.py** : Generates a column chart for visualizing stock charts

- **Bar_chart.py** : Creates a bar chart for visualizing P/E ratios
- 


### How To Run The Automation


1. **Start with inputing the ticker to scrape**

```bash
python Stock_Ticker.py
```

2. Ensure that Data_cleaning.py cleans and preprocesses the data before creating visualizations

3. Use Column_chart.py and Bar_chart.py to automate visualizations


## Example Output

Your Column chart should look like this:

https://github.com/NStanley0524/Stock_Data_Automation_Python/blob/main/Images/Screenshot%202024-11-18%20182255.png


Your Bar chart should also look like this:

[https://github.com/NStanley0524/Stock_Data_Automation_Python/blob/main/Images/Screenshot%202024-11-18%20182232.png](https://github.com/NStanley0524/Stock_Data_Automation_Python/blob/main/Images/Bar_chart.png)

The stock data report should look this way:

https://github.com/NStanley0524/Stock_Data_Automation_Python/blob/main/Images/Stock_data_report_output.png



## Future Enhancements

1. Add more financial metrics and visualizations

2. Support multiple data sources ( e.g. Trading view, Finviz )


## License

This project is licensed under the MIT license. See the [LICENSE]() file for more details
