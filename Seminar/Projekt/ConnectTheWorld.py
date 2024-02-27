import networkx as nx

class ConnectTheWorld:
    
    first_test_case = {
        "terminalA": ["Paris", "Paris"],
        "terminalB": ["London", "NYC"],
        "isolated": ["Dhaka"]
    }
    
    second_test_case = {
        "terminalA": ["Tokyo", "Prauge"],
        "terminalB": ["Sydney", "Bern"],
        "isolated": []
    }
    
    third_test_case = {
        "terminalA": ["Tokyo", "Prague", "Bern"],
        "terminalB": ["Sydney", "Bern", "Vienna"],
        "isolated": []
    }
    
    fourth_test_case = {
        "terminalA": ["Madrid"],
        "terminalB": ["Porto"],
        "isolated": ["Bogota", "Lima", "Kigali", "Ottawa", "Manila"]
    }

    fifth_test_case = {
        "terminalA": ["Split", "Split"],
        "terminalB": ["Stockholm", "Winterhold"],
        "isolated": ["Zagreb"]
    }
    
    def get_max_for_each_city(self, edges: list):
        dict = {}
        for edge in edges:
            if edge[0] not in dict:
                dict[edge[0]] = 1
            else:
                dict[edge[0]] = dict[edge[0]] + 1
            if edge[1] not in dict:
                dict[edge[1]] = 1
            else:
                dict[edge[1]] = dict[edge[1]] + 1
        return dict

    def connect(self, terminalA: list, terminalB: list, isolated: list):
        graph = nx.Graph()
        graph.add_edges_from(zip(terminalA, terminalB))
        terminals_by_city = self.get_max_for_each_city(graph.edges)
        max_terminals = sorted(terminals_by_city.items(), key=lambda x: x[1], reverse=True)[0][1]

        if max_terminals < 2:
            return []
        
        if len(isolated) > 0:
            for isolated_city in isolated:
                for city, amount_of_teleporters in terminals_by_city.items():
                    if amount_of_teleporters < max_terminals:
                        try:
                            graph_copy = graph.copy()
                            graph_copy.add_edge(city, isolated_city)
                            nx.find_cycle(graph_copy)
                        except nx.NetworkXNoCycle:
                            if nx.is_connected(graph_copy):
                                return [city, isolated_city]
        else:
            for city_1, amount_of_teleporters in terminals_by_city.items():
                for city_2 in terminals_by_city:
                    if city_1 != city_2 and terminals_by_city[city_2] < max_terminals:
                        try:
                            if (city_1, city_2) not in graph.edges:
                                graph_copy = graph.copy()
                                graph_copy.add_edge(city_1, city_2)
                                nx.find_cycle(graph_copy)
                        except nx.NetworkXNoCycle:
                            if nx.is_connected(graph_copy):
                                return [city_1, city_2]

    
    def start(self):
        #First
        print("First test:")
        first_test = self.connect(self.first_test_case["terminalA"], self.first_test_case["terminalB"], self.first_test_case["isolated"])
        print(first_test)
        #Second
        print("Second test:")
        second_test = self.connect(self.second_test_case["terminalA"], self.second_test_case["terminalB"], self.second_test_case["isolated"])
        print(second_test)
        #Third
        print("Third test:")
        third_test = self.connect(self.third_test_case["terminalA"], self.third_test_case["terminalB"], self.third_test_case["isolated"])
        print(third_test)
        #Fourth 
        print("Fourth test:")
        fourth_test = self.connect(self.fourth_test_case["terminalA"], self.fourth_test_case["terminalB"], self.fourth_test_case["isolated"])
        print(fourth_test)
        #Fifth
        print("Fifth test:")
        fifth_test = self.connect(self.fifth_test_case["terminalA"], self.fifth_test_case["terminalB"], self.fifth_test_case["isolated"])
        print(fifth_test)