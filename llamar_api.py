import requests


def buscar_noticias(query):

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": query,
        "apiKey":"400d20e349bc48c0a45bcea76ed45384"
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    return data.get("articles" , [])
    
    







buscar_noticias("chile")

