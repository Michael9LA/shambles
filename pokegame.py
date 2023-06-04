import requests
import random


# Retrieve pokemon list from poke API
def get_pokemon(pokemon):
    chosen_poke = "https://pokeapi.co/api/v2/pokemon/" + str(pokemon.lower())
    response = requests.get(chosen_poke)
    if response.status_code == 200:
        pokedata = response.json()
        pokename = pokedata['name']
        skills = [ability['ability']['name'] for ability in pokedata['abilities']]
        stats = {stat['stat']['name']: stat['base_stat'] for stat in pokedata['stats']}
        return pokename, skills, stats
    else:
        return None


# Round for games
def play_round(player_pokemon, opp_pokemon, attribute):
    print(f'{player_pokemon[0].capitalize()} (Player) vs {opp_pokemon[0].capitalize()} (Opponent)')
    print(f'{player_pokemon[0].capitalize()} {attribute.upper()}: {player_pokemon[2][attribute]}')
    print(f'{opp_pokemon[0].capitalize()} {attribute.upper()}: {opp_pokemon[2][attribute]}')

    if player_pokemon[2][attribute] > opp_pokemon[2][attribute]:
        print('Player Pokemon wins the round')
        return "Player"
    elif opp_pokemon[2][attribute] > player_pokemon[2][attribute]:
        print('Opponent Pokemon wins the round')
        return "Opponent"
    else:
        print('The round is a draw.')
        return "Draw"


# Main Game
def play_game():
    # Player chooses their Pokemon
    player_pokename = input('Choose your Pokemon: ')
    player_pokemon = get_pokemon(player_pokename)
    while player_pokemon is None:
        print('Invalid Pokemon name, please try again.')
        player_pokename = input('Choose your Pokemon: ')
        player_pokemon = get_pokemon(player_pokename)

    # Opponents Pokemon generated
    opp_pokename = random.randint(1, 151)
    opp_pokemon = get_pokemon(str(opp_pokename))

    print(f'Player Pokemon: {player_pokemon[0].capitalize()} vs Opponent Pokemon: {opp_pokemon[0].capitalize()}')
    attributes = list(player_pokemon[2].keys())

    opp_wins = []
    player_wins = []

    while len(opp_wins) < 4 or len(player_wins) < 4 or len(attributes) > 0:
        print('\nAvailable Attributes')

        for i, attr in enumerate(attributes, start=1):
            print(f'{i}. {attr.capitalize()}')

        choice = int(input('Choose your Attribute: ')) - 1
        if choice < 0 or choice >= len(attributes):
            print('Invalid choice. Try again.')
            continue

        attr_choice = attributes[choice]
        attributes.remove(attr_choice)

        result = play_round(player_pokemon, opp_pokemon, attr_choice)

        if result == "Player":
            print(f'Player 1: {player_pokemon[0]} had more {attr_choice}!')
            player_wins.append('/')
        elif result == "Opponent":
            print(f'Opponent: {opp_pokemon[0]} had more {attr_choice}!')
            opp_wins.append('/')
        else:
            print('The round is a draw.')

    print('\nGame Over!')
    if player_wins > opp_wins:
        print(f'Player 1 Pokemon - {player_pokemon} - Wins!!')
    elif opp_wins > player_wins:
        print(f'You lose! Better luck next time...')
    else:
        print('All attributes have been played and no one wins.')


play_game()
