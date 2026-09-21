import pandas as pd


data = {
    "Title": [
        "Minecraft",
        "Super Mario Odyssey",
        "Zelda: Breath of the Wild",
        "Roblox",
        "Pokemon Scarlet",
        "Fortnite",
    ],
    "Genre": ["Sandbox", "Platformer", "Adventure", "Sandbox", "RPG", "Shooter"],
    "Rating": [9.5, 9.7, 10.0, 7.8, 7.2, 8.5],  # Score out of 10
    "Hours_Played": [120, 45, 95, 200, 35, 110],
}


df = pd.DataFrame(data)

print("--- ALL GAMES ---")
print(df)


total_hours = df["Hours_Played"].sum()
average_rating = df["Rating"].mean()

print("\n--- QUICK STATS ---")
print(f"Total time played across all games: {total_hours} hours")
print(f"Average game score: {average_rating:.2f} / 10")


top_tier = df[df["Rating"] >= 9.0]
print("\n--- TOP TIER GAMES (9.0+) ---")
print(top_tier[["Title", "Rating"]])


genre_playtime = df.groupby("Genre")["Hours_Played"].sum()
print("\n--- HOURS PLAYED PER GENRE ---")
print(genre_playtime)


df.to_csv("my_games.csv", index=False)
print("\nSaved everything to 'my_games.csv'!")
