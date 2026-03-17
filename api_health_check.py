import requests

def api_health_check(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print("API healthy")
        else:
            print("API unhealthy")

        print(response.status_code)

    except:
        print("Network error")


api_health_check("https://api.github.com")