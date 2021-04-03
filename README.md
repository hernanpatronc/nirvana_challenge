## To run this project

1. Install the dependencies with "pip install -r requirements.txt"
2. Run the mock api using: "python mock_api.py"
3. Run the project with "python api.py"
4. If you want to add a strategy, follow the instructions in utils/strategies.py
5. If you want to change the behaviour of the app (for instance, default strategy or changing the API's urls), change the config.py file

This API implements two main endpoints (and some healthchecks):

- /api/v1: which accepts two optional query params, strategy, which is a string defining the strategy to use and member_id, which changes how we will retrieve data from the other APIs. The strategy must be defined in the strategies dictionary in utils/strategies.py, or the default strategy will be applied (an error can be returned if errorOnInvalidStrategy is set to True on the config )
- /api/v1/:strategy: accepts member_id as a query param and strategy is the strategy to apply. See previous endpoint

Both return a JSON object with the desired strategy applied to the APIs responses.
