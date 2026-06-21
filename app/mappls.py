import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MAPPLS_API_KEY")


def reverse_geocode(lat, lng):

    url = "https://search.mappls.com/search/address/rev-geocode"

    params = {
        "access_token": API_KEY,
        "lat": lat,
        "lng": lng
    }

    try:
        response = requests.get(url, params=params, timeout=20)

        print("Status:", response.status_code)
        print("Raw Response:", response.text)

        data = response.json()

        if data.get("responseCode") == 200:
            return data["results"][0]

        print("Mappls JSON:", data)

        return {
            "formatted_address": "Location unavailable"
        }

    except Exception as e:
        print("Mappls Exception:", str(e))

        return {
            "formatted_address": "Location unavailable"
        }