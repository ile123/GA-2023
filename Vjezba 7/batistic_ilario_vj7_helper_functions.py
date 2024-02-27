import networkx as nx
import io

def loadData(file_path):
    pajekData, reached, verticesCnt = "", False, 0
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
        lines.remove("*vertices")
        for line in lines:
            if(line =="*arcs"):
                reached =True
            if not reached:
                verticesCnt += 1
                parts = line.split(" ")
                add = parts[0] + " " + parts[1] + "\n"
                pajekData += add
            elif line != "":
                pajekData += line + "\n"
    return "*vertices " + str(verticesCnt) + "\n" + pajekData
    

def loadGraph(file_path):
    data = loadData(file_path)
    graph_data_bytes = data.encode('utf-8')
    graph_file = io.BytesIO(graph_data_bytes)
    G = nx.read_pajek(graph_file)
    return G