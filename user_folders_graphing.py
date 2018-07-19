import matplotlib.pyplot as plt

def buildDirectoryGraph(users_u1, users_u2, users_u3, new_ece, cse_h1, cse_h2, che_h2):
    labels = ['U1', 'U2', 'U3', 'new-ece', 'cse_h1', 'cse_h2', 'che_h2']

    #color = ['green', 'red', 'blue', 'yellow', 'brown', ]

    sizes = [users_u1, users_u2, users_u3, new_ece, cse_h1, cse_h2, che_h2]

    plt.pie(sizes, labels=labels, shadow=True, explode=(0.1, 0.1, 0.1), startangle=90, autopct='%1.1f%%')

    plt.title("Auburn Total Student Directories")

    plt.axis('equal')

    plt.savefig('DirectoryGraph.png', bbox_inches='tight')

