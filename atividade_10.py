import requests
api_key = 'SUA_CHAVE_DE_API_AQUI'

# URL base da API OpenWeatherMap
base_url = 'https://api.openweathermap.org/data/2.5/weather'


def obter_previsao_tempo(cidade):
    params = {
        'q': cidade,
        'appid': api_key,
        'units': 'metric'  # Para obter a temperatura em Celsius
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temperatura = data['main']['temp']
        descricao = data['weather'][0]['description']
        return f"Previsão do tempo em {cidade}: {descricao}, Temperatura: {temperatura}°C"
    else:
        return "Não foi possível obter a previsão do tempo."


def main():
    print("Aplicativo de Previsão do Tempo")
    cidade = input("Digite o nome da cidade para obter a previsão do tempo: ")
    
    previsao = obter_previsao_tempo(cidade)
    print(previsao)

if __name__ == '__main__':
    main()
