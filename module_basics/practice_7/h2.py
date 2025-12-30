with open('test.csv', 'r') as file:
    surface_winners = {}

    for line in file:
        row = line.strip().split(',')
        winner = row[2]
        surface = row[3]
        if surface not in surface_winners:
            surface_winners[surface] = set()
        surface_winners[surface].add(winner)

max_surface = max(surface_winners, key=lambda k: len(surface_winners[k]))
print(
    f"Surface with most unique winners: {max_surface} ({len(surface_winners[max_surface])} unique winners)")
print("\nWinners on this surface:")
for winner in surface_winners[max_surface]:
    print(f"\t{winner}")
