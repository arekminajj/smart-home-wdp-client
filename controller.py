import requests

BASE_URL = 'https://wdp-smart-home.azurewebsites.net'

class HomeStatus:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

    def get(self):
        res = requests.get(BASE_URL)
        data = res.json()

        return data
    
    def update_light(self, light_1):
        res = requests.post(BASE_URL + '/light', json={
        "light_1": light_1,
        "API_KEY": self.API_KEY
        })

        data = res.json()

        return data
    
    def update_temp_setting(self, temp_set):
        res = requests.post(BASE_URL + '/temp-set', json={
        "temp_set": temp_set,
        "API_KEY": self.API_KEY
        })
        
        data = res.json()

        return data
    