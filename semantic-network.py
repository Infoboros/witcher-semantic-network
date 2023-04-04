from typing import Optional


class Node:
    def __init__(self, content: str):
        self.content = content
        self.links = {}

    def exist_link_by_type(self, node, type_link: str) -> bool:
        for link in self.links.get(type_link, []):
            if link == node:
                return True
        return False

    def link(self, node, type_link: str):
        if not self.exist_link_by_type(node, type_link):
            self.links[type_link] = [*self.links.get(type_link, []), node]

    def __eq__(self, other):
        return self.content == other.content


class Network:
    def __init__(self):
        self.nodes = []
        self.node_contents = set()

    def __find_node(self, node_content: str) -> Node:
        if node_content not in self.node_contents:
            raise Network.DoesNotNodeExists(node_content)

        for node in self.nodes:
            if node.content == node_content:
                return node

    def add_nodes(self, *nodes: str):
        for node in nodes:
            if node not in self.node_contents:
                self.nodes.append(Node(node))
                self.node_contents.add(node)

    def add_link(self, type_link: str, start: str, end: str):
        start_node = self.__find_node(start)
        end_node = self.__find_node(end)

        start_node.link(end_node, type_link)

    class NetworkException(Exception):
        pass

    class DoesNotNodeExists(NetworkException):
        def __init__(self, node_content: str):
            super().__init__(f"Node {node_content} does not exists")
