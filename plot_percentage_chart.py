from matplotlib import pyplot as plt

def plot_lawn_percentage_chart(lawn_percentage):
    plt.figure()
    labels = 'Lawn Area', 'Other Area'
    sizes = [lawn_percentage, 100 - lawn_percentage]
    colors = ['green', 'gray']
    explode = (0.1, 0)  # "explode" the lawn area slice for emphasis

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title("Lawn Area Percentage")
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.