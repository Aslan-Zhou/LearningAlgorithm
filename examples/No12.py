from collections import deque


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if Breadth_First_Search(person):
                print(person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)


def Breadth_First_Search(name):
    return name[-1] == 'm'


graph = {}
graph['you'] = ["Alice", 'Bob', 'Claire']
graph['Bob'] = ['Anuj', "Peggy"]
graph['Alice'] = ['Ben', "Peggy"]
graph['Claire'] = ['Tom', "Jonny"]
graph['Anuj'] = ['Tom', "Paul", "Harry"]
graph['Peggy'] = []
graph['Ben'] = ["Harry"]
graph['Tom'] = ["Jack"]
graph['Jonny'] = []
graph['Paul'] = []
graph['Harry'] = ['Jack']
graph['Jack'] = []

search('you')
