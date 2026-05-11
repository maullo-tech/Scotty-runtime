import random

def topology_state(density, coherence):
    if coherence > 0.5 and density > 0.4:
        return "harmonic"
    if coherence > 0.25:   # antes 0.3
        return "meta-stable"
    if density < 0.2:
        return "fragmented"
    return "chaotic"

def morphogenesis(field):
    rewrites = 0
    for node in field.nodes:
        if random.random() < 0.2:
            node.frequency *= random.uniform(0.9, 1.1)
            rewrites += 1
    return rewrites