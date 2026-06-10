movies = {
    "Action": ["John Wick", "Mad Max", "The Dark Knight"],
    "Comedy": ["3 Idiots", "Jumanji", "The Mask"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"],
    "Horror": ["The Conjuring", "Insidious", "Annabelle"]
}

print("=" * 50)
print("🎬 MOVIE RECOMMENDATION SYSTEM 🎬")
print("=" * 50)

print("\nAvailable Genres:")
for genre in movies:
    print("-", genre)

choice = input("\nEnter your favorite genre: ")

if choice in movies:
    print(f"\nRecommended {choice} Movies:")
    for movie in movies[choice]:
        print("⭐", movie)
else:
    print("\n❌ Genre not found. Please choose from the list.")