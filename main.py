from orchestrator.pipeline import run
from config.settings import POST_LIMIT


def main():

    seeds = [
        "air fryer",
        "standing desk"
    ]

    run(seeds, POST_LIMIT)


if __name__ == "__main__":
    main()
