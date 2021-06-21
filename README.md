# Cryptongo

This is a App that connects every 5 minutes to CoinMarketCap API and save of the cryptocurrencies information (Like the price and more), in MongoDB database and create a API for make queries to all information saved on MongoDB




## Description
Proyect made with Mongo 4.4.6, Flask, Python 3.7 and JWT autetication 


## Endpoints

1- `GET /api/`
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
  
2- `GET /api/cryptos/info`
<br>Description: Show database info.
- Example:
  <br>[http://127.0.0.1:5000/api/cryptos/info](http://127.0.0.1:5000/api/cryptos/info)

 Response:
   ```json
  {
    "Creation date": "jun 19-2021 23:54",
    "Creator Name": "Ovidio Andrade Zambrano",
    "Number of Documents": 1044
  }
  ```
  
  
3- `GET /api/cryptos/<name>`
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

3- `GET /api/cryptos`
<br>Description: Show items with limits and names .
- Example:
  <br>[http://127.0.0.1:5000/api/cryptos?limit=2&name=Bitcoin](http://127.0.0.1:5000/api/cryptos?limit=2&name=Bitcoin)

 Response if found Crypto:
   ```json
[
     {
       "circulating_supply": 18739650,
       "cmc_rank": 1,
       "date_added": "2013-04-28T00:00:00.000Z",
       "last_updated": "2021-06-21T03:49:02.000Z",
       "max_supply": 21000000,
       "name": "Bitcoin",
       "num_market_pairs": 9099,
       "quote": {
          "USD": {
            "last_updated": "2021-06-21T03:49:02.000Z",
            "market_cap": 650687853826.2715,
            "percent_change_1h": -0.62874939,
            "percent_change_24h": -2.7574355,
            "percent_change_30d": -6.00703393,
            "percent_change_60d": -35.01271117,
            "percent_change_7d": -10.55091735,
            "percent_change_90d": -36.5370431,
            "price": 34722.5190345749,
            "volume_24h": 35848757947.411
        }
    },
      "symbol": "BTC",
      "total_supply": 18739650
   },
     {
       "circulating_supply": 18739650,
       "cmc_rank": 1,
       "date_added": "2013-04-28T00:00:00.000Z",
       "last_updated": "2021-06-21T03:50:02.000Z",
       "max_supply": 21000000,
       "name": "Bitcoin",
       "num_market_pairs": 9099,
       "quote": {
         "USD": {
           "last_updated": "2021-06-21T03:50:02.000Z",
           "market_cap": 650520078244.3922,
           "percent_change_1h": -0.80857913,
           "percent_change_24h": -2.72236184,
           "percent_change_30d": -6.16195051,
           "percent_change_60d": -35.05237396,
           "percent_change_7d": -10.62403004,
           "percent_change_90d": -36.55194752,
           "price": 34713.5660615002,
           "volume_24h": 35864628396.308464
       }
    },
    "symbol": "BTC",
    "total_supply": 18739650
  }
]
  
