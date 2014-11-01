# GitHub_network.py
import requests
from graph import DirectedGraph


class GitHubNetwork:

    def __init__(self, username, depth):
        self.username = username
        self.depth = depth
        self.request = requests.get(
            'https://api.github.com/users/' + self.username + '/followers')
        self.social_graph = DirectedGraph()

    def following(self):

        request_json = self.request.json()
        for each_person in request_json:
            self.social_graph.add_edge(self.username, each_person['login'])

        return self.social_graph.nodes

    def is_following(self, user):
        if self.social_graph.path_between(self.username, user):
            return True
        return False

    def steps_to(self, username):
        pass


def main():
    # req = requests.get(
    #    'https://api.github.com/users/Ivaylo-Bachvarov/followers')
    #r = req.json()
    # for each in r:
    #    print (each['login'])
    #print (req.json())

    # if req.status_code == 200:
    #    result = req.json()
    #print (result)

    a = GitHubNetwork("Ivaylo-Bachvarov", 1)
    a.following()
    print(a.social_graph)
    #print (a.following())


if __name__ == '__main__':
    main()
