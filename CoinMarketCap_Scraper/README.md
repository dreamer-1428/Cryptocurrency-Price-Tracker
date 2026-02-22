# Cryptocurrency Price Tracker
**Automated Market Data Extraction and Trend Analysis**

## Project Overview
[cite_start]This project is an automated Python-based web scraping system designed to extract and log real-time financial data from **CoinMarketCap**[cite: 6, 13]. [cite_start]Utilizing **Selenium WebDriver**, the tool navigates dynamic, JavaScript-heavy web environments to capture live metrics for the top 10 cryptocurrencies[cite: 6, 8, 15].

## Key Features
* [cite_start]**Real-time Extraction**: Captures Name, Price, 24h Change, and Market Cap[cite: 18, 28].
* [cite_start]**Headless Mode**: Runs silently in the background without a visible browser window[cite: 21, 49].
* [cite_start]**Historical Logging**: Appends cleaned data to a structured CSV file with unique timestamps for trend analysis[cite: 20, 30].
* [cite_start]**Automated Management**: Uses `webdriver_manager` for seamless ChromeDriver configuration[cite: 26, 35].

## Technical Stack
* [cite_start]**Language**: Python [cite: 32]
* [cite_start]**Automation**: Selenium WebDriver [cite: 33]
* [cite_start]**Data Processing**: Pandas [cite: 34]
