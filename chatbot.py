# A chatbot that can answer questions about the weather and the time of the current location.

import requests

# Get the current location


def get_location():
    ip = requests.get('https://api.ipify.org').text
    location = requests.get('https://ipapi.co/' + ip + '/json/').json()
    return location

# Chatbot


def chatbot():
    # Get the location
    location = get_location()
    # Print the greeting
    print('Hello, I am a chatbot. I can answer questions about information of your current location.')
    while True:
        # Ask the user a question
        question = input('Ask me a question: ').lower()
        # Check if the user wants to quit
        if 'exit' in question or 'bye' in question:
            print('Bye!')
            return
        # Check if the user wants to know the current location
        elif 'where' in question:
            print('You are in ' + location['city'] + ', ' +
                  location['region'] + ', ' + location['country_name'] + '.')
        # Check if the user wants to know the currency
        elif 'money' in question or 'currency' in question:
            print('The currency of ' + location['country_name'] + ' is ' +
                  location['currency_name'] + ' or ' + location['currency'] + '.')
        # Check if the user wants to know the area of the country
        elif 'area' in question:
            print('The area of ' + location['country_name'] + ' is ' +
                  str(location['country_area']) + ' km^2.')
        # Check if the user wants to know the population of the country
        elif 'population' in question:
            print('The population of ' +
                  location['country_name'] + ' is ' + str(location['country_population']) + '.')
        # Check if the user wants to know the calling code of the country
        elif 'phone' in question or 'calling' in question or 'call' in question:
            print('The calling code of ' +
                  location['country_name'] + ' is ' + location['country_calling_code'] + '.')
        # Check if the user wants to know the country
        elif 'country' in question:
            print('The country is ' + location['country_name'] + '.')
        # Check if the user wants to know the region
        elif 'region' in question:
            print('The region is ' + location['region'] + '.')
        # Check if the user wants to know the latitude
        elif 'latitude' in question:
            print('The latitude of your location is ' +
                  str(location['latitude']) + '.')
        # Check if the user wants to know the longitude
        elif 'longitude' in question:
            print('The longitude iof your location is ' +
                  str(location['longitude']) + '.')
        # Check if the user wants to know the IP address
        elif 'ip address' in question:
            print('The IP address of your location is ' + location['ip'] + '.')
        # Check if the user wants to know the postal code
        elif 'postal code' in question:
            print('The postal code of your location is ' +
                  location['postal'] + '.')
        # Print error message if the question is not recognized
        else:
            print('I do not understand your question.')


# Run the chatbot
chatbot()
