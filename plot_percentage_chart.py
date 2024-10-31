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

def plot_cut_vs_uncut_chart(ground_map):
    total_lawn_cells = 0
    cut_cells = 0

    for row in ground_map:
        for cell in row:
            if cell == 'L' or cell == 'C':  
                total_lawn_cells += 1
                if cell == 'C':  
                    cut_cells += 1

    cut_percentage = (cut_cells / total_lawn_cells) * 100 if total_lawn_cells > 0 else 0
    uncut_percentage = 100 - cut_percentage

    
    plt.figure()
    labels = 'Cut Grass', 'Uncut Grass'
    sizes = [cut_percentage, uncut_percentage]
    colors = ['red', 'green']
    explode = (0.1, 0)  

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title("Cut vs Uncut Lawn Area")
    plt.axis('equal')  
