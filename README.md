\# Binance Futures Testnet Trading Bot



\## Setup



1\. Install Python

2\. Install dependencies:



pip install -r requirements.txt



3\. Create .env file with:



BINANCE\_API\_KEY=your\_api\_key

BINANCE\_API\_SECRET=your\_secret\_key



\## Run



Market Order:



py cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001



Limit Order:



py cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000



\## Assumptions



\- Binance Futures Testnet is used

\- API credentials are stored in .env

