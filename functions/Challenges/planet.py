
def planet(id):
    planets = {1: 'Mercury', 2: 'Venus', 3: 'Earth', 4: 'Mars', 5: 'Jupiter', 6: 'Saturn', 7: 'Uranus', 8: 'Neptune',
           9: 'Pluto'}


    return planets.get(id, 'Invalid planet id')

n = int(input("enter the id"))
planet_name = planet(n)
print("the planet name is", planet_name)

print("___")
planets = {
    1: 'Mercury',
    2: 'Venus',
    3: 'Earth',
    4: 'Mars',
    5: 'Jupiter',
    6: 'Saturn',
    7: 'Uranus',
    8: 'Neptune',
    9: 'Pluto'
}


def planet(planet_id):
    return planets.get(planet_id, 'Invalid planet id')


num = int(input('Enter planet ID: '))
print('Planet name is', planet(num))