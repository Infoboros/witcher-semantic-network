import networkx as nx
from pyvis.network import Network as PyvisNetwork
import pandas as pd

from semantic_network import Network


class WitcherNetwork(Network):

    def __init_from_dataset(self):
        characters = list(set(list(self.dataset['Source']) + list(self.dataset['Target'])))
        self.add_nodes(characters)

        for _, (source, target, book) in self.dataset.iterrows():
            self.add_link(str(book), source, target)

    def __init__(self):
        super().__init__()
        self.dataset = pd.read_csv('witcher_network.csv')[['Source', 'Target', 'book']]
        self.__init_from_dataset()

    def visualisation(self):
        graph = nx.from_pandas_edgelist(
            self.dataset,
            source='Source',
            target='Target',
            edge_attr='book'
        )
        net = PyvisNetwork(cdn_resources='remote', notebook=True, filter_menu=True)
        net.show_buttons(filter_=['physics'])
        net.from_nx(graph)
        net.options = {
            "configure": {
                "enabled": True
            },
            "interaction": {
                "hover": True
            },
            "nodes": {
                "borderWidth": 2,
                "borderWidthSelected": 4,
                "chosen": True,
                "color": {"highlight": {"border": "#FF4040",
                                        "background": "#EE3B3B"
                                        },
                          "hover": {"border": "#DEB887",
                                    "background": "#FFD39B"
                                    }
                          }
            },
            "edges": {
                "color": {"highlight": "#FF4040",
                          "hover": "#DEB887"
                          }
            }
        }
        net.show('example.html')
