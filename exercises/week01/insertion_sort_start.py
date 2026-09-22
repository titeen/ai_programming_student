"""
Oefening 1: Insertion Sort
===========================
Implementeer insertion sort volgens het stappenplan in opgave_week1.md.
"""

import time
import random


def insertion_sort(sequence):
    """
    Sorteer een lijst van klein naar groot met behulp van insertion sort.

    Parameters:
        sequence (list): De lijst om te sorteren.

    Returns:
        list: De gesorteerde lijst.
    """

    for i in range(1, len(sequence)):
        key = sequence[i]
        j = i - 1

        while j >= 0 and key < sequence[j]:
            sequence[j + 1] = sequence[j]
            j -= 1

        sequence[j + 1] = key

    return sequence


def bubble_sort(sequence):
    n = len(sequence)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]

    return sequence


def merge_sort(sequence):
    if len(sequence) <= 1:
        return sequence

    mid = len(sequence) // 2

    left_half = merge_sort(sequence[:mid])
    right_half = merge_sort(sequence[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    result.extend(left_half[i:])
    result.extend(right_half[j:])

    return result


def meet_snelheid(sort_function, sequence):

    start = time.perf_counter()

    sort_function(sequence.copy())

    einde = time.perf_counter()

    return einde - start


if __name__ == "__main__":
    # Test je implementatie met deze voorbeelden
    test_lijsten = [
        [],
        [42],
        [1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [3, 1, 2, 1, 3],
        [5, 2, 4, 6, 1, 3],
    ]

    for lijst in test_lijsten:
        origineel = lijst.copy()
        gesorteerd = insertion_sort(lijst)
        print(f"Origineel: {origineel} -> Gesorteerd: {gesorteerd}")

    # Stap 5: vergelijk insertion sort, bubble sort en merge sort

    groottes = [10, 100, 1000, 10000]

    print("\n--- Snelheidsvergelijking ---")

    for grootte in groottes:
        lijst = [random.randint(0, 100000) for _ in range(grootte)]

        insertion_tijd = meet_snelheid(insertion_sort, lijst)
        bubble_tijd = meet_snelheid(bubble_sort, lijst)
        merge_tijd = meet_snelheid(merge_sort, lijst)

        print(f"\nAantal items: {grootte}")
        print(f"Insertion Sort: {insertion_tijd:.6f} seconden")
        print(f"Bubble Sort:    {bubble_tijd:.6f} seconden")
        print(f"Merge Sort:     {merge_tijd:.6f} seconden")
