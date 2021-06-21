# Cryptongo

This is a App that connects every 5 minutes to CoinMarketCap API and save of the cryptocurrencies information (Like the price and more), in MongoDB database and create a API for make queries to all information saved on MongoDB




## Description
Proyect made with Mongo 4.4.6, Flask, Python 3.7 and JWT autetication 


## Endpoints

`GET /api/`
<br>Description: HomePage.
- Example:
  <br>[http://127.0.0.1:5000/api/](http://127.0.0.1:5000/api)

 Response:
   ```json
    {
      "name": "Cryptongo API",
      "Description":"This is a App that connects to CoinMarketCap API and save of the cryptocurrencies information in MongoDB database"
    }
  ```
  
  
`GET /api/cryptos/<name>`
<br>Description: Show items for names.
- Example:
  <br>[http://127.0.0.1:5000/api/cryptos/Cardano](http://127.0.0.1:5000/api/cryptos/Cardano)

 Response if found Crypto:
   ```json
[
  {
    "circulating_supply": 31946328269.464,
    "cmc_rank": 5,
    "date_added": "2017-10-01T00:00:00.000Z",
    "last_updated": "2021-06-21T03:48:14.000Z",
    "max_supply": 45000000000,
    "name": "Cardano",
    "num_market_pairs": 257,
    "quote": {
      "USD": {
        "last_updated": "2021-06-21T03:48:14.000Z",
        "market_cap": 43753590917.511154,
        "percent_change_1h": -1.19465836,
        "percent_change_24h": -2.15424033,
        "percent_change_30d": -9.01671305,
        "percent_change_60d": 14.95744705,
        "percent_change_7d": -10.64496653,
        "percent_change_90d": 21.46317777,
        "price": 1.36959686097426,
        "volume_24h": 2025916783.2057946
      }
    },
    "symbol": "ADA",
    "total_supply": 32704886184.416
  }
]
  ```
 Else:
    ```json
    {
      "Error": "Cryptocurrency not found"
    }
  ```

  
