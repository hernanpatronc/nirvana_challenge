# If dev environment
dev = True
# Raise an error if no member_id is present on the request query params
errorOnNoMemberId = False
# use mock API
useMock = True
# The default member_id
defaultMemberId = '1'
# If should validate that every API response contains just the keys below
validateKeys = False
# Keys to check in API responses
validKeys = ['deductible', 'stop_loss', 'oop_max']
# APIs to call. The defaults are for hitting mock_api.py on port 3001
apisToCall = ['http://localhost:3001/api/1',
              'http://localhost:3001/api/2', 'http://localhost:3001/api/3']
# If invalid strategy as parameter, wether to use the default one or raise an error
errorOnInvalidStrategy = False
# Default strategy to use if none present
defaultStrategy = 'average'
# API port
port = 3000
# API version for backwards compatibility
version = 1
