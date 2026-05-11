import math
import random

class ResonantNode:
    def __init__(self, node_id):
        self.id = node_id
        self.frequency = random.uniform(0.5, 2.0)
        self.phase = random.uniform(0, math.pi)
        self.energy = random.uniform(0.2, 1.0)
        self.links = []

    def resonance(self, other):
        delta = abs(self.frequency - other.frequency)
        return max(0, 1 - delta)

class ResonantField:
    def __init__(self, size=8):
        self.nodes = [ResonantNode(i) for i in range(size)]
        self.connect()

    def connect(self):
        for node in self.nodes:
            node.links = []
            for other in self.nodes:
                if node.id == other.id:
                    continue
                r = node.resonance(other)
                if r > 0.35:
                    node.links.append(other.id)

    def evolve(self, temp_factor=1.0, gpu_factor=1.0):
        effective_factor = temp_factor * gpu_factor
        for node in self.nodes:
            node.frequency += random.uniform(-0.12, 0.12) * effective_factor
            node.phase += random.uniform(-0.25, 0.25) * effective_factor
            node.energy += random.uniform(-0.05, 0.05) * effective_factor
            node.energy = max(0, min(node.energy, 2))
        self.connect()

    def average_resonance(self):
        values = []
        for node in self.nodes:
            for other_id in node.links:
                other = self.nodes[other_id]
                values.append(node.resonance(other))
        if not values:
            return 0
        return round(sum(values) / len(values), 2)

    def topology_density(self):
        total_links = sum(len(n.links) for n in self.nodes)
        max_links = len(self.nodes) ** 2
        return round(total_links / max_links, 2)

    def coherence(self):
        phases = [n.phase for n in self.nodes]
        avg = sum(phases) / len(phases)
        variance = sum(abs(p - avg) for p in phases) / len(phases)
        return round(max(0, 1 - variance), 2)
