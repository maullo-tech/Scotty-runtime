import csv
import os
from datetime import datetime

LOG_FILE = "logs/scotty_metrics.csv"

def init_logger():

    if not os.path.exists("logs"):
        os.makedirs("logs")

    if not os.path.exists(LOG_FILE):

        with open(LOG_FILE,"w") as f:

            writer = csv.writer(f)

            writer.writerow([
                "timestamp",
                "cpu",
                "ram",
                "temp",
                "energy",
                "governor",
                "coherence",
                "density",
                "field_state"
            ])

def log_state(metrics,governor,coherence,density,state):

    with open(LOG_FILE,"a") as f:

        writer = csv.writer(f)

        writer.writerow([
            datetime.now().isoformat(),
            metrics["cpu"],
            metrics["ram"],
            metrics["temp"],
            metrics["energy"],
            governor,
            coherence,
            density,
            state
        ])
