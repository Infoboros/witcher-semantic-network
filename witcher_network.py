import pandas as pd

from semantic_network import Network


class WitcherNetwork(Network):

    def __init_from_dataset(self):
        dataset = pd.read_csv('witcher_network.csv')[['Source', 'Target', 'book']]

        characters = list(set(list(dataset['Source']) + list(dataset['Target'])))
        self.add_nodes(characters)

        for _, (source, target, book) in dataset.iterrows():
            self.add_link(str(book), source, target)

    def __init__(self):
        super().__init__()
        self.__init_from_dataset()

