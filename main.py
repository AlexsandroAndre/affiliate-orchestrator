from orchestrator.pipeline import run

def main():

    seeds = [
        "air fryer",
        "standing desk"
    ]

    for seed in seeds:

        run(seed)

if __name__ == "__main__":
    main()
