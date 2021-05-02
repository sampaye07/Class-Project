# import required modules
import requests, json

def k_to_f(k):
    f = (k - 273.15) * 9/5 + 32
    return int(f)


def weather():
    # enter your API key
    api_key = "68b6187cbc61b04bd4f34e59c25bde7a"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # cityname = input("Enter your city name:")
    zip_code = input("Enter your zip code:\n")

    payload = {
        "zip": zip_code,
        "appid": api_key
    }

    try:
        r = requests.get(base_url, params=payload).json()
        if r["cod"] != 200:
            raise Exception(r["message"])
    except Exception as err:
        print("Error:", err)
        return

    body = r["main"]
    weather = r["weather"]

    temperature = k_to_f(body["temp"])
    print("Temperature is {temperature}° Farenheit".format(temperature=temperature))

    feels_like = k_to_f(body["feels_like"])
    print("Temperature feels like {feels_like}° Farenheit".format(feels_like=feels_like))

    temp_min = k_to_f(body["temp_min"])
    print("Temperature min is {temp_min}° Farenheit".format(temp_min=temp_min))

    temp_max = k_to_f(body["temp_max"])
    print("Temperature max is {temp_max}° Farenheit".format(temp_max=temp_max))

    humidity = body["humidity"]
    print("Humidity: {humidity}%".format(humidity=humidity))

    description = weather[0]["description"]
    print("Description is: {description}".format(description=description))


def main():
    weather()
    prompt = "Do you want to check the weather again? (y/n)\n"
    answer = input(prompt)
    if answer.lower().strip() in ["y", "yes"]:
        main()


main()