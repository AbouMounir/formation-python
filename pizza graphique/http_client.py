import json

from kivy.network.urlrequest import UrlRequest


class HttpClient:
    def get_pizzas(self):
        url = "https://jrpizzamamadjango2.herokuapp.com/api/GetPizzas"
        
        def data_received(req, result):
            data = json.loads(result)
            pizzas_dict = []
            for i in data :
                pizzas_dict.append(i["fields"])
            print(data)
            print("data received")
            
            req = UrlRequest(url, on_success=data_received)