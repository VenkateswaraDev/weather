'''
from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        #source contain JSON data from API
        api_key = '044e2ccc230a54b93ed7912cd7631823'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        source = urllib.request.urlopen(url).read()
        #source = urllib.request.urlopen(
        #    'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=044e2ccc230a54b93ed7912cd7631823').read()
        
        #converting JSON data to a dictionary
        list_of_data = json.loads(source)
        
        #data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + ' kelven', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request,'main.html',data)
'''
from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '044e2ccc230a54b93ed7912cd7631823'  
        
        try:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
            source = urllib.request.urlopen(url).read()
            list_of_data = json.loads(source)
            
            data = {
                "country_code": str(list_of_data['sys']['country']), 
                "coordinate": str(list_of_data['coord']['lon']) + ' '
                              + str(list_of_data['coord']['lat']), 
                "temp": str(list_of_data['main']['temp']) + 'k', 
                "pressure": str(list_of_data['main']['pressure']), 
                "humidity": str(list_of_data['main']['humidity']),
            }
            print(data)
            
        except urllib.error.HTTPError as e:
            print(e.code, e.reason)  # Print the HTTP error code and reason for debugging
            data = {}  # Empty data in case of error
        
    else:
        data = {}
        
    return render(request, 'main.html', data)

