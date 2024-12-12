#!/usr/bin/python3
"""
Fetch and print all characters of a Star Wars movie.
"""

import requests


def get_star_wars_characters(movie_id):
    """
    Fetch and print all characters from a Star Wars movie by ID.

    Args:
        movie_id (int): The ID of the Star Wars movie (1-6).

    Returns:
None
    """
    base_url = "https://swapi.dev/api/films/"
    try:
        response = requests.get(f"{base_url}{movie_id}/")
        if response.status_code != 200:
            print("Failed to fetch the movie details. Check the movie ID.")
            return

        data = response.json()
        print(f"Movie: {data['title']}")
        print("Characters:")

        for character_url in data['characters']:
            character_response = requests.get(character_url)
            if character_response.status_code == 200:
                character_data = character_response.json()
                print(f"-
			{character_data['name']}")
            else:
                print("Failed to fetch character details.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    movie_id = int(input("Enter the Star Wars movie ID (1-6): "))
    get_star_wars_characters(movie_id)
