import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from project_utils.preprocessing import get_organic_search_results, get_titles , get_links , get_snippets

from project_utils.metrics import jaccard_matrix

SAVE_PATH = "../Results/"
labels = ['United States', 'India', 'Japan', 'Germany', 'Brazil']


def save_maps(query, matrix, save=True):
    sns.set_theme(style="whitegrid", font_scale=1.2)
    
    # Create figure
    plt.figure(figsize=(8, 6))
    
    ax = sns.heatmap(
        matrix,
        annot=True,
        fmt=".2f",              # format numbers (e.g., 2 decimals)
        cmap="viridis",         # color map
        cbar_kws={"shrink": 0.8, "label": "Value"},  # colorbar styling
        linewidths=0.5,         # grid lines
        linecolor="white"
    )
    
    ax.set_xticks([i+0.5 for i in range(len(labels))])
    ax.set_yticks([i+0.5 for i in range(len(labels))])
    ax.set_xticklabels(labels, rotation=0, ha="center")
    ax.set_yticklabels(labels, rotation=0 , va="center")
    
    plt.title(query, fontsize=14, pad=15, weight="bold")
    
    plt.tight_layout()
    
    if save:
        file = f"{SAVE_PATH}{query}.png"
        plt.savefig(file, dpi=300, bbox_inches="tight")
    
    plt.show()


def generate_results(jaccard_matrix):

    for query, matrix in jaccard_matrix.items():
        
        save_maps(query,matrix)



if __name__ == '__main__':


    with open('../Data/merged.json','r') as file:
        data = json.load(file)    
     
    query = [q for q in data.keys()]
    country = [c for c in data[query[0]]]
    #print(country)
    
    titles = get_titles(data)
    jm = jaccard_matrix(titles)

    generate_results(jm)

