import math
import random

ATTRACTORS = {
    "powersave":    {"coh": 0.15, "den": 0.20, "sigma": 0.14},
    "conservative": {"coh": 0.35, "den": 0.45, "sigma": 0.14},
    "ondemand":     {"coh": 0.55, "den": 0.65, "sigma": 0.14},
    "schedutil":    {"coh": 0.75, "den": 0.80, "sigma": 0.14},
    "performance":  {"coh": 0.90, "den": 0.92, "sigma": 0.14}
}

def select_governor(field, governors, current, annealing_temp):
    coh = field.coherence()
    den = field.topology_density()

    probs = []
    for gov in governors:
        if gov in ATTRACTORS:
            att = ATTRACTORS[gov]
            dist = math.sqrt((coh - att["coh"])**2 + (den - att["den"])**2)
            prob = math.exp(-dist**2 / (2 * att["sigma"]**2))
        else:
            prob = 0.0
        probs.append((gov, prob))

    total = sum(p for _, p in probs)
    if total == 0:
        return current

    norm = [(g, p / total) for g, p in probs]

    if random.random() < annealing_temp * 0.15:
        return random.choice(governors)

    r = random.random()
    acc = 0.0
    for gov, prob in norm:
        acc += prob
        if r <= acc:
            return gov
    return norm[-1][0]