import networkx as nx
import matplotlib.pyplot as plt
from os import listdir
import sample



def createGraph(path="./"):
    g=nx.DiGraph() # create direct graph 
    files_to_parse=list(filter(lambda f: f.endswith(".py") ,listdir(path))) #only python files
    for file in files_to_parse:
        g.add_node(extract_filename(file))  
        find_edges_in_file(file,g)
    return g
    
    


def drawGraph(graph):
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()


def find_edges_in_file(file,g):
    with  open(file, 'r') as fr:
        for number, line in enumerate(fr):
            if("import" in line ):
                tab=line.split()
                g.add_edge(extract_filename(file),tab[1])

            
def extract_filename(file):
    return file.split(".")[0]  #cut extension .py

g=createGraph()
drawGraph(g)