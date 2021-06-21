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

