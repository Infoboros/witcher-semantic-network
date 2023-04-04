from typing import Optional


class Node:
    def __init__(self, content: str):
        self.content = content
        self.links = {}

    def exist_link_by_type(self, type_link: str) -> bool:
        return type_link in self.links.keys()

    def exist_link_by_type_and_node(self, node, type_link: str) -> bool:
        for link in self.links.get(type_link, []):
            if link == node:
                return True
        return False

    def link(self, node, type_link: str):
        if not self.exist_link_by_type_and_node(node, type_link):
            self.links[type_link] = [*self.links.get(type_link, []), node]

    def all_linked(self):
        all_linked = []
        for linked in self.links.values():
            all_linked += linked
        return all_linked

    def all_linked_by_type(self, type_link: str):
        return self.links.get(type_link, [])

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

    def add_nodes(self, nodes: [str]):
        for node in nodes:
            if node not in self.node_contents:
                self.nodes.append(Node(node))
                self.node_contents.add(node)

    def add_link(self, type_link: str, source: str, target: str):
        start_node = self.__find_node(source)
        end_node = self.__find_node(target)

        start_node.link(end_node, type_link)

    def all_nodes(self) -> [str]:
        return list(self.node_contents)

    def all_nodes_with_link(self, type_link: str) -> [str]:
        return [
            node.content
            for node in self.nodes
            if node.exist_link_by_type(type_link)
        ]

    @staticmethod
    def __get_linked_content_from_nodes(linked_nodes: [Node]) -> [str]:
        return list(set(
            [
                node.content
                for node in linked_nodes
            ]
        ))

    def all_linked(self, node_content: str) -> [str]:
        node = self.__find_node(node_content)
        linked_nodes = node.all_linked()
        return self.__get_linked_content_from_nodes(linked_nodes)

    def all_linked_by_type(self, node_content: str, type_link: str):
        node = self.__find_node(node_content)
        linked_nodes = node.all_linked_by_type(type_link)
        return self.__get_linked_content_from_nodes(linked_nodes)

    class NetworkException(Exception):
        pass

    class DoesNotNodeExists(NetworkException):
        def __init__(self, node_content: str):
            super().__init__(f"Node {node_content} does not exists")
