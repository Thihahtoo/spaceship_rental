### The Spaceship Rental Problem
#### Description
You're going to optimize the profitability of a small rental company with a single spaceship to rent. You'll
receive a list a contracts, each order will include:
- a name (String of 64 chars or less)
- a start hour (int)
- a duration (int)
- a price (int)

Start hour, duration and price are all positive integers that can quite large.

The goal is to produce a list of contract names maximizing the profit. As there's only a single ship to rent
there should not be any overlap between the accepted contracts and of course not all proposed contracts can
be picked.

For instance we can have a 4 contract list:
- Contract1: start hour 0, duration 5, price 10
- Contract2: start hour 3, duration 7, price 14
- Contract3: start hour 5, duration 9, price 8
- Contract4: start hour 5, duration 9, price 7

Optimal solution would be `Contract1` and `Contract3` with a total income of `18`. Another solution would be
`Contract1` and `Contract4` which will also lead to a continuous rental from `0` to `14` but would only give a `17`
income.

#### Requirements
Should be setup a clean Python 3.10 environment.
Install required packages like below:
```
pip3 install flask_restful
pip3 install flask
```

#### Ready to run
Run `server.py` file under main directory.
```
python3 server.py
```
Web server will start on localhost:8080.
```
 * Serving Flask app 'SpaceShip Rental'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:8080
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 128-818-091
```
The end point required is `/spaceship/optimize` accepting POST requests with a JSON payload containing
the list of contracts (see below for the format). The server will compute a solution and return a JSON
object with the total income and the list of contract names (in order) to achieve this income.

#### Payload
#### Input
The input payload will be like:
```json
[
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
    {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
    {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
    {"name": "Contract4", "start": 5, "duration": 9, "price": 7}
]
```
#### Output
The server will return a payload similar to the following:
```json
{
    "income": 18,
    "path": ["Contact1", "Contract3"]
}
```

#### Example:
Run below command to test API.
```
curl http://127.0.0.1:8080/spaceship/optimize -H 'Content-Type: application/json' -d '[{"name": "Contract2", "start": 3, "duration": 7, "price": 14},{"name": "Contract3", "start": 5, "duration": 9, "price": 8},{"name": "Contract1", "start": 0, "duration": 5, "price": 10},{"name": "Contract4", "start": 5, "duration": 9,"price": 7}]' -X POST
```
