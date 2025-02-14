#!C:\Users\hum2a\AppData\Local\Programs\Python\Python313\python.exe
import os

os.environ["BEST_MOVIE"] = "Interstellar"
os.environ["ONE_PIECE"] = "One Piece"
os.environ["FAVORITE_TEAM"] = "Liverpool"

BEST_MOVIE = input("What's the greatest movie ever?")
ONE_PIECE = input("One Piece.")
FAVORITE_TEAM = input("What is the best football team?")

print(f"Best Movie:")
print({os.getenv('BEST_MOVIE')})
print(f"One Piece Character: {os.getenv('ONE_PIECE')}")
print(f"Favorite Football Team: {os.getenv('FAVORITE_TEAM')}")

