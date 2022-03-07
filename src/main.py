import pandas as pd
import argparse

from yahoofinance.webscraping.yfexchangerate import YFExchangeGateway

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('year', help='Year of the exchange.  Example: 2021')
    parser.add_argument('month', help='Month of the exchange in numeric format.  Example(June): 6')
    parser.add_argument('date', help='Date of the exchange.  Example: 18')
    args = parser.parse_args()
    year = args.year
    month = args.month
    date = args.date

    try:
        gateway = YFExchangeGateway(year, month, date)
        titles, values = gateway.get_data()
    except Exception as e:
        print('Error encountered while retrieving exchange data.')
        print(e)
        exit(1)

    df_result = pd.DataFrame()
    df_result[titles[0]] = titles[1:]
    df_result[values[0]] = values[1:]
    print(df_result.T)