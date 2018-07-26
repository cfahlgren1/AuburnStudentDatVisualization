import matplotlib.pyplot as plt

def active_users(active, inactive):
        # Data to plot
        labels = 'Active', 'Inactive'

        plt.title("User Accounts")

        sizes = [active, inactive]
        colors = ['lightcoral', 'lightskyblue']
        explode = (0.1, 0)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')
        plt.savefig('foo.png', bbox_inches='tight')

active_users(5512, 15494)