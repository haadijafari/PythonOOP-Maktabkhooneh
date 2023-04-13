from abc import ABC, abstractmethod
import requests


class Joke(ABC):
    @abstractmethod
    def get_random_joke(self):
        pass


class APINinjas(Joke):
    url = "https://jokes-by-api-ninjas.p.rapidapi.com/v1/jokes"

    headers = {
        "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
        "X-RapidAPI-Host": "jokes-by-api-ninjas.p.rapidapi.com"
    }

    def get_random_joke(self):
        response = requests.request("GET", self.url, headers=self.headers)
        print(response.text)


class DadJokes (Joke):
    url = "https://dad-jokes7.p.rapidapi.com/dad-jokes/joke-of-the-day"

    headers = {
        "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
        "X-RapidAPI-Host": "dad-jokes7.p.rapidapi.com"
    }

    def get_random_joke(self):
        response = requests.request("GET", self.url, headers=self.headers)
        print(response.text)


class WorldOfJokes(Joke):
    url = "https://world-of-jokes1.p.rapidapi.com/v1/jokes/categories"

    headers = {
        "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
        "X-RapidAPI-Host": "world-of-jokes1.p.rapidapi.com"
    }

    def get_random_joke(self):
        response = requests.request("GET", self.url, headers=self.headers)
        print(response.text)
