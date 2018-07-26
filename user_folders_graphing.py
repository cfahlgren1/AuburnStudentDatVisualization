import matplotlib.pyplot as plt

def buildDirectoryGraph(new_ece, users_u3, cse_h1, users_u2, cse_h2, che_h2, users_u1):
    labels = ['new-ece', 'users_u3', 'cse_h1', 'U2', 'cse_h2', 'che_h2', 'U1']

    #color = ['green', 'red', 'blue', 'yellow', 'brown', ]

    sizes = [new_ece, users_u3, cse_h1, users_u2, cse_h2, che_h2, users_u1]

    ttl = plt.title("Auburn Total Student Directories")
    ttl.set_position([.5, 1.05])

    plt.pie(sizes, labels=labels, shadow=True, explode=(0, 0, 0, 0, 0, 0, 0), startangle=90, autopct='%1.1f%%', pctdistance=0.8)


    plt.axis('equal')

    plt.savefig('DirectoryGraph.png', bbox_inches='tight')
