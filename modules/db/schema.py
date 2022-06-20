# define the basic schema of the project here
# should check on startup

def collections():
    collection_list = ['users', 'events', 'categories', 'questions']
    return collection_list


class template:
    collections = collections()
