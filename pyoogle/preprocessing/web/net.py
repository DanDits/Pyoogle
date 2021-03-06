

class WebNet:
    def __init__(self):
        self.nodes = []  # All nodes
        self.url_to_nodes = {}  # Maps urls to nodes, can contain nodes multiple times

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        return iter(self.get_nodes())

    def get_nodes(self):
        return self.nodes

    def add_node(self, webnode):
        self.nodes.append(webnode)
        self.url_to_nodes[webnode.get_urls()[0]] = webnode

    def get_by_content_hash(self, content_hash):
        for node in self.nodes:
            if node.get_content_hash() == content_hash:
                return node

    def get_by_url(self, url, extend_index=False):
        if url is None:
            return
        node = self.url_to_nodes.get(url)
        if node is not None:
            return node
        # Now brute force search
        for node in self.get_nodes():
            if url in node.get_urls():
                if extend_index:
                    # Map url to node (maybe it is common)
                    self.url_to_nodes[url] = node
                return node

    def build_url_index(self):
        for node in self.get_nodes():
            for url in node.get_urls():
                self.url_to_nodes[url] = node
