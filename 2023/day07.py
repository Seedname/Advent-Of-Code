import read
from collections import Counter
from itertools import combinations


def part_1(input: list[str]) -> int:
    TYPES = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1]
    STRENGTHS = {TYPES[n]: n for n in range(len(TYPES))}

    def calculate_strength(card: str) -> bool:
        def determine_type(card: str) -> int:
            distinct = Counter(card)
            # five of a kind
            if len(distinct) == 1: return 7
            # four of a kind
            if len(distinct) == 2 and max(distinct.values()) == 4: return 6
            # full house
            if len(distinct) == 2 and max(distinct.values()) == 3: return 5
            # three of a kind
            if len(distinct) == 3 and max(distinct.values()) == 3: return 4
            # two pair
            if len(distinct) == 3 and max(distinct.values()) == 2: return 3
            # one pair
            if len(distinct) == 4 and max(distinct.values()) == 2: return 2
            # high card
            return 1

        strength = determine_type(card) * 13 ** 6

        for i in range(5):
            strength += STRENGTHS[card[i]] * 13 ** (5 - i)

        return strength

    hands = sorted(input, key=lambda x: calculate_strength(x.split(" ")[0]))
    total_winnings = sum(int(hands[i].split(" ")[1]) * (i+1) for i in range(len(hands)))
    return total_winnings


def part_2(input: list[str]) -> int:
    TYPES = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]
    STRENGTHS = {TYPES[n]: n for n in range(len(TYPES))}

    def calculate_strength(card: str) -> bool:
        def determine_type(card: str) -> int:
            distinct = Counter(card)
            # five of a kind
            if len(distinct) == 1: return 7
            # four of a kind
            if len(distinct) == 2 and max(distinct.values()) == 4: return 6
            # full house
            if len(distinct) == 2 and max(distinct.values()) == 3: return 5
            # three of a kind
            if len(distinct) == 3 and max(distinct.values()) == 3: return 4
            # two pair
            if len(distinct) == 3 and max(distinct.values()) == 2: return 3
            # one pair
            if len(distinct) == 4 and max(distinct.values()) == 2: return 2
            # high card
            return 1

        def determine_best_joker_type(card: str) -> int:
            if 'J' not in card:
                return determine_type(card)

            combs = combinations(TYPES, card.count('J'))

            highest_score = determine_type(card)
            for comb in combs:
                new_card = card
                for item in comb:
                    new_card = card.replace('J', item)
                score = determine_type(new_card)
                if score > highest_score:
                    highest_score = score

            return highest_score

        strength = determine_best_joker_type(card) * 13 ** 6

        for i in range(5):
            strength += STRENGTHS[card[i]] * 13 ** (5 - i)

        return strength

    hands = sorted(input, key=lambda x: calculate_strength(x.split(" ")[0]))
    total_winnings = sum(int(hands[i].split(" ")[1]) * (i+1) for i in range(len(hands)))
    return total_winnings


if __name__ == "__main__":
    read.test_solution(7, 2023, part_1, part_2)
