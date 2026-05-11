import random, math

ATTRACTORS = [
    {"governor": "powersave",   "coh": 0.5, "den": 0.2, "sigma": 0.3},
    {"governor": "conservative","coh": 0.4, "den": 0.3, "sigma": 0.4},
    {"governor": "ondemand",    "coh": 0.25,"den": 0.4, "sigma": 0.5},
    {"governor": "schedutil",   "coh": 0.35,"den": 0.5, "sigma": 0.4},
    {"governor": "performance", "coh": 0.1, "den": 0.7, "sigma": 0.5},
]

def select_governor(field, available_governors, current, annealing_temp):
    coh = field.coherence()
    den = field.topology_density()
    best = None
    best_sim = -1
    for att in ATTRACTORS:
        if att["governor"] not in available_governors:
            continue
        dist = math.sqrt((coh - att["coh"])**2 + (den - att["den"])**2)
        sim = math.exp(-dist**2 / (2 * att["sigma"]**2))
        if sim > best_sim:
            best_sim = sim
            best = att["governor"]
    if best is None:
        return current
    if best != current:
        return best
    if random.random() < annealing_temp * 0.02:
        return random.choice(available_governors)
    return current