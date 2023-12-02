from collections import Counter


BAG: Counter[str] = Counter({
    "red": 12,
    "green": 13,
    "blue": 14,
})


def round_is_valid(round_: str) -> tuple[bool, dict[str, int]]:
    counts: dict[str, int] = {}
    is_valid = True
    for grab in round_.strip().split(","):
        count, color = grab.strip().split()

        count = int(count)

        if color not in counts or count > counts[color]:
            counts[color] = count

        if BAG[color] < int(count):
            is_valid = False

    return is_valid, counts


def rounds_is_valid(rounds: str) -> tuple[bool, dict[str, int]]:
    counts: dict[str, int] = {}
    is_valid = True
    for round_ in rounds:
        is_valid, round_counts = round_is_valid(round_)
        for k in round_counts:
            if k not in counts or counts[k] < round_counts[k]:
                counts[k] = round_counts[k]

            if not is_valid:
                is_valid = False

    return is_valid, counts


def main() -> None:
    with open("input", "r") as file:
        games = file.readlines()

    s = 0
    for game in games:
        game_info, rounds_info = game.split(":")
        _, game_id = game_info.split()

        rounds = rounds_info.split(";")

        _, counts = rounds_is_valid(rounds)

        round_power = 1
        for count in counts.values():
            round_power *= count

        s += round_power

    print(s)


if __name__ == "__main__":
    main()
