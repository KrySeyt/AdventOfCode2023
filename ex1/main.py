import re


NAMES_TO_NUMS: dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_num(str_with_num: str) -> int:
    pattern = r"|".join(NAMES_TO_NUMS) + r"|\d"
    nums = re.findall(pattern, str_with_num)

    first_num = nums[0] if nums[0].isdigit() else NAMES_TO_NUMS[nums[0]]
    second_num = nums[-1] if nums[-1].isdigit() else NAMES_TO_NUMS[nums[-1]]

    return int(first_num + second_num)


def main() -> None:
    with open("./ex1/strs", "r") as file:
        strs = file.readlines()
        s = 0
        for str_ in strs:
            s += get_num(str_)

    print(s)


if __name__ == "__main__":
    main()
