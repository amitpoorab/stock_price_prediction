### README

# Stock Price Trend Analysis(WIP, Not in working condition) 

Note: This repository is a Work In Progress (WIP).
This repository contains code for fetching stock price data from the Alpha Vantage API, storing the data in a PostgreSQL database, and displaying the stock price trend for the last month using a Streamlit app. This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline and provides a foundation for further enhancements, including predictive analytics.

## Features

- Fetch stock price data from the Alpha Vantage API.
- Store the fetched data in a PostgreSQL database.
- Display the stock price trend for the last month using a Streamlit app.
- Containerized application for easy deployment.
- Infrastructure as Code (IaC) integration (WIP).

## Prerequisites

- Docker
- Docker Compose
- PostgreSQL
- Python 3.9 or later
- Alpha Vantage API Key

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/stock-price-trend-analysis.git
   cd stock-price-trend-analysis
   ```

2. **Set up the environment**:
   - Create a `.env` file in the root directory with the following content:
     ```env
     ALPHA_VANTAGE_API_KEY=your_api_key
     POSTGRES_USER=your_postgres_user
     POSTGRES_PASSWORD=your_postgres_password
     POSTGRES_DB=your_postgres_db
     ```
   - Replace `your_api_key`, `your_postgres_user`, `your_postgres_password`, and `your_postgres_db` with your actual values.

3. **Build and run the Docker containers**:
   ```bash
   docker-compose up --build
   ```

## Future Enhancements

- **Predictive Analytics**: Add machine learning models to predict future stock prices.
- **IaC Integration**: Use tools like Terraform to automate infrastructure setup.
- **Enhanced Error Handling**: Improve error handling and logging for better debugging.
- **Scalability**: Optimize the pipeline for handling larger datasets and more frequent updates.
