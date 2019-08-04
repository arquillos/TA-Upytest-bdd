import requests

from pytest_bdd import scenarios, given, then, parsers

# Shared variables
DUCKDUCKGO_API = 'https://api.duckduckgo.com/'

# Scenarios
scenarios('../features/service.feature', example_converters=dict(phrase=str))


# Given steps
@given('the DuckDuckGo APU is queried with "<phrase>"')
def ddg_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params)
    return response


# Then steps
@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code


@then('the response contains results for "<phrase>"')
def ddg_response_contents(ddg_response, phrase):
    assert phrase.lower() == ddg_response.json()['Heading'].lower()
