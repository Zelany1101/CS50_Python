"""
Bitcoin is cryptocurrency -- Rather than relying on a central authority like a bank, Bitcoin relies on a distributed network known as a blockchain to record transactions.
Because there's demand for Bitcoin, users are willing to buy it by exchanging one currency (USD) for Bitcoin.

Implement a program that...
    - Expects the user to specify as a command-lime argument the number of Bitcoins, n, that they would like to buy.
            - If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
    - Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
            - Catch any expections with code like...

            import requests

            try:
                ...
            except requests.RequestException:
                ...
    - Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator
"""

import requests
import sys

def convert_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        return
    else:
        content = response.json()
        return (content["bpi"]["USD"]["rate_float"])

def check_sys_argv():
    try:
        float(sys.argv[1])
    except IndexError:
        sys.exit('Missing command-line argument')
    except ValueError:
        sys.exit('Command-line argument is not a number')
    else:
        number_of_bitcoins = sys.argv[1]

    return number_of_bitcoins

def main():
    n = float(check_sys_argv())
    rate = float(convert_bitcoin())

    amount = rate * n

    print(f"${amount:,.4f}")

if __name__ == "__main__":
    main()
