
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    for worker in all_python_devs:
        print(worker)
    print(" ")

    for worker in all_platzi_workers:
        print(worker)
    print(" ")

    for worker in adults:
        print(worker)
    print("""
    



    """)
    print("---------------------  RETO  ------------------")
    print("1. Crear las listas all_python_devs y all_Platzi_workers usando una combinacion de filter y map")
    print("2. Crear la lista old_people y adults con list comprehesions")
    print(" ")
    print(" ")

    all_python_devs_r = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs_r = list(map(lambda worker: worker["name"], all_python_devs_r))
    print("all_python_devs = " + str(all_python_devs))

    print(" ")

    all_platzi_workers_r = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers_r = list(map(lambda worker: worker["name"], all_platzi_workers_r))
    print("all_platzi_workers = " + str(all_platzi_workers_r))
    
    print(" ")

    old_people_r = [worker | {"old": worker["age"] > 70} for worker in DATA]
    print("old_people = " + str(old_people_r))

    print(" ")

    adults_r = [worker["name"] for worker in DATA if worker["age"] > 18]
    print("adults = " + str(adults_r))


if __name__ == "__main__":
    run()