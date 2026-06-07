# ============================================
# MOVIE RECOMMENDATION SYSTEM USING PYTHON
# Beginner-Friendly AI Internship Project
# ============================================

# Dictionary storing movie recommendations
movies = {

    "action": [
        "⭐ Avengers",
        "⭐ John Wick",
        "⭐ Batman",
        "⭐ Mission Impossible"
    ],

    "comedy": [
        "⭐ Mr. Bean",
        "⭐ Home Alone",
        "⭐ Jumanji",
        "⭐ The Mask"
    ],

    "horror": [
        "⭐ The Conjuring",
        "⭐ Annabelle",
        "⭐ IT",
        "⭐ Insidious"
    ],

    "sci-fi": [
        "⭐ Interstellar",
        "⭐ Inception",
        "⭐ Avatar",
        "⭐ The Matrix"
    ],

    "romance": [
        "⭐ Titanic",
        "⭐ The Notebook",
        "⭐ La La Land",
        "⭐ Me Before You"
    ]
}

# ============================================
# WELCOME MESSAGE
# ============================================

print("========================================")
print("🎬 MOVIE RECOMMENDATION SYSTEM")
print("========================================")

print("\nType 'exit' anytime to quit.\n")

# ============================================
# MAIN PROGRAM LOOP
# ============================================

while True:

    # Display available genres
    print("Available Genres:")
    print("1. Action")
    print("2. Comedy")
    print("3. Horror")
    print("4. Sci-Fi")
    print("5. Romance")

    # Take user input
    user_choice = input("\nEnter your favorite genre: ")

    # Convert input to lowercase
    user_choice = user_choice.lower()

    # Exit condition
    if user_choice == "exit":

        print("\n👋 Thank you for using the Movie Recommendation System.")
        print("🎉 Have a great day!")

        break

    # Check if genre exists
    elif user_choice in movies:

        print("\n🎥 Recommended Movies:\n")

        # Display recommended movies
        for movie in movies[user_choice]:

            print(movie)

        print("\n========================================\n")

    # Invalid input handling
    else:

        print("\n❌ Invalid genre entered.")
        print("📌 Please choose from the available genres.\n")