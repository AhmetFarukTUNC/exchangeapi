# Currency Converter

This project is a simple currency converter that allows users to input:

The amount they want to convert.

The currency they want to convert from.

The currency they want to convert to.

The converter fetches real-time exchange rates and returns the converted amount.

## Features

Supports all major currencies.

Fetches live exchange rates.

Simple input for amount, source currency, and target currency.

## Requirements

Python 3.x

requests library

Install the required libraries with:

pip install requests

pip install json

## Usage

Replace <you can input your api key> in the code with your actual API key from Exchange Rate API.

Run the script with:

python exchange.py

Example input:

Bozdurulan döviz türü: USD

Alınacak döviz türü: TRY

Ne kadar USD bozdurmak istiyorsunuz: 1000

Example output:

1 USD = 27 TRY

1000 USD = 27000 TRY

## API Information

This project uses the Exchange Rates API to fetch real-time currency data.

## Contribution

Fork the repository.

Create a new branch.

Make your changes and commit with a descriptive message.

Push the branch and create a pull request.