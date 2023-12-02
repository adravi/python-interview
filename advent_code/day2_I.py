# https://adventofcode.com/2023/day/2

RED, GREEN, BLUE = 12, 13, 14

input = [
    [{'b': 12, 'r': 15, 'g': 2}, {'r': 17, 'g': 8, 'b': 5}, {'r': 8, 'b': 17},{'g': 9, 'b': 1, 'r': 4}],
    [{'r': 6, 'b': 6, 'g': 2}, { 'b': 1, 'r': 1}, { 'g': 6, 'r': 1, 'b': 10}],
    [{ 'g': 1, 'b': 2}, { 'b': 7, 'g': 4}, { 'g': 2, 'b': 1}, { 'b': 10, 'g': 4}, { 'b': 4}, { 'g': 1, 'b': 7, 'r': 1}],
    [{'r': 16, 'b': 12, 'g': 10}, { 'r': 15, 'g': 5, 'b': 6}, { 'g': 10, 'r': 15, 'b': 12}],
    [{'g': 2, 'r': 2, 'b': 9}, { 'r': 1, 'g': 5}, { 'g': 4, 'b': 12, 'r': 1}, { 'b': 5, 'g': 8}],
    [{'b': 17, 'g': 3, 'r': 4}, { 'g': 6, 'b': 16, 'r': 3}, { 'r': 2, 'b': 15}],
    [{'g': 4, 'r': 10}, { 'g': 1, 'r': 4, 'b': 4}, { 'b': 4, 'r': 11}],
    [{'g': 8, 'b': 4}, { 'g': 17, 'r': 4}, { 'b': 10, 'g': 5, 'r': 9}, { 'g': 9, 'r': 8, 'b': 3}, { 'g': 9, 'r': 5, 'b': 2}],
    [{'r': 4, 'g': 2}, { 'b': 7, 'r': 3, 'g': 3}, { 'g': 3, 'b': 7, 'r': 3}],
    [{'g': 3, 'r': 2, 'b': 2}, { 'g': 3, 'r': 11, 'b': 1}, { 'g': 16, 'r': 11}],
    [{'b': 2, 'g': 18}, { 'b': 12, 'g': 1}, { 'g': 2, 'b': 6}, { 'r': 1, 'b': 4, 'g': 20}, { 'b': 14, 'r': 1, 'g': 4}],
    [{'g': 2, 'b': 1, 'r': 7}, { 'r': 11, 'g': 3, 'b': 6}, { 'r': 1, 'b': 2, 'g': 3}, { 'r': 4, 'g': 2, 'b': 5}],
    [{'r': 4, 'b': 17, 'g': 5}, { 'b': 6, 'g': 2}, { 'b': 12, 'g': 4, 'r': 2}, { 'g': 5, 'b': 9}, { 'g': 5, 'b': 3, 'r': 3}, { 'g': 4, 'r': 1, 'b': 7}],
    [{'b': 4, 'g': 18}, { 'b': 3, 'r': 3, 'g': 13}, { 'b': 5, 'g': 10}, { 'g': 10, 'b': 2}, { 'b': 1, 'g': 14}, { 'b': 3, 'g': 18, 'r': 2}],
    [{'g': 1, 'b': 2, 'r': 1}, { 'g': 1, 'r': 2, 'b': 1}, { 'g': 1, 'r': 2}, { 'g': 1, 'b': 4, 'r': 4}, { 'b': 6, 'r': 2, 'g': 1}, { 'b': 3, 'r': 2}],
    [{'g': 3, 'r': 2}, { 'g': 4, 'r': 1, 'b': 8}, { 'b': 5, 'r': 9, 'g': 3}, { 'b': 7, 'g': 19, 'r': 18}],
    [{'b': 10, 'r': 9, 'g': 7}, { 'r': 16, 'g': 11, 'b': 11}, { 'b': 8, 'g': 3}, { 'r': 12, 'b': 1, 'g': 10}],
    [{'g': 11, 'b': 11, 'r': 5}, { 'r': 7, 'g': 11, 'b': 13}, { 'g': 5, 'r': 9, 'b': 6}, { 'r': 9, 'g': 16, 'b': 17}],
    [{'r': 8, 'g': 3, 'b': 16}, { 'g': 13, 'b': 8}, { 'r': 7, 'g': 8, 'b': 1}, { 'r': 13, 'b': 3, 'g': 7}, { 'g': 6, 'b': 14, 'r': 13}, { 'b': 15, 'g': 9, 'r': 13}],
    [{'r': 1, 'g': 7, 'b': 5}, { 'g': 14, 'b': 4}, { 'g': 10, 'b': 11, 'r': 2}, { 'r': 2, 'b': 3, 'g': 1}, { 'r': 1, 'b': 5, 'g': 8}],
    [{'g': 10, 'b': 12, 'r': 6}, { 'b': 17, 'r': 6, 'g': 6}, { 'b': 12, 'g': 9, 'r': 4}, { 'b': 5, 'r': 3, 'g': 4}, { 'g': 6, 'b': 7, 'r': 5}],
    [{'b': 1, 'r': 3, 'g': 16}, { 'r': 4, 'b': 1, 'g': 3}, { 'g': 12, 'b': 1, 'r': 2}, { 'r': 12}],
    [{'r': 2, 'b': 6, 'g': 1}, { 'r': 11, 'b': 13, 'g': 4}, { 'r': 8, 'b': 3, 'g': 6}, { 'g': 2, 'b': 8, 'r': 2}, { 'r': 7, 'b': 11, 'g': 4}],
    [{'r': 4, 'g': 12, 'b': 2}, { 'b': 8, 'r': 15}, { 'b': 1, 'g': 10, 'r': 8}, { 'g': 1, 'b': 2, 'r': 6}, { 'g': 10, 'b': 8, 'r': 5}],
    [{'b': 2, 'g': 11}, { 'g': 17, 'r': 1, 'b': 2}, { 'b': 2, 'r': 3, 'g': 1}],
    [{'b': 16, 'g': 11}, { 'g': 4}, { 'g': 9, 'b': 4}, { 'g': 10, 'b': 5}, { 'r': 1, 'b': 5, 'g': 9}, { 'g': 5, 'b': 5}],
    [{'g': 10, 'r': 2}, { 'b': 5, 'r': 1}, { 'r': 6, 'g': 5}],
    [{'r': 3, 'g': 5, 'b': 10}, { 'r': 1, 'g': 5, 'b': 2}, { 'b': 6, 'g': 2, 'r': 2}, { 'r': 6, 'b': 9, 'g': 1}, { 'r': 3}, { 'r': 3, 'g': 2, 'b': 2}],
    [{'r': 8, 'b': 18, 'g': 5}, { 'b': 1, 'r': 8, 'g': 2}, { 'r': 2, 'g': 4, 'b': 18}, { 'r': 6, 'g': 4, 'b': 7}],
    [{'r': 1, 'g': 18}, { 'g': 11}, { 'b': 4, 'r': 5, 'g': 14}, { 'g': 3, 'b': 8, 'r': 2}],
    [{'r': 1, 'b': 5, 'g': 17}, { 'b': 7}, { 'g': 10, 'b': 8, 'r': 1}, { 'g': 11, 'b': 4}],
    [{'b': 5, 'r': 15, 'g': 12}, { 'r': 6, 'g': 8, 'b': 8}, { 'r': 2, 'g': 14, 'b': 3}, { 'b': 4, 'g': 15}, { 'b': 7, 'r': 12, 'g': 7}, { 'b': 2, 'r': 9, 'g': 7}],
    [{'r': 13, 'g': 2}, { 'g': 1, 'r': 7, 'b': 15}, { 'g': 1, 'b': 14, 'r': 13}, { 'r': 8, 'g': 2}, { 'r': 12, 'b': 14, 'g': 10}, { 'g': 8, 'b': 16, 'r': 10}],
    [{'g': 11, 'b': 9, 'r': 2}, { 'r': 4, 'g': 1, 'b': 8}, { 'b': 4, 'g': 7, 'r': 4}, { 'b': 7, 'r': 1, 'g': 8}, { 'b': 9, 'r': 1, 'g': 4}, { 'r': 2, 'g': 10, 'b': 4}],
    [{'r': 3, 'b': 9}, { 'b': 11, 'r': 3, 'g': 12}, { 'g': 7, 'b': 10, 'r': 2}],
    [{'b': 9, 'g': 3, 'r': 3}, { 'b': 5, 'r': 1, 'g': 3}, { 'g': 2, 'r': 6}, { 'b': 9, 'r': 7}],
    [{'r': 1, 'b': 7}, { 'r': 4, 'g': 1}, { 'g': 1, 'r': 9, 'b': 9}],
    [{'g': 1, 'r': 12}, { 'g': 4, 'r': 12, 'b': 4}, { 'g': 5, 'r': 10}, { 'r': 6, 'g': 4, 'b': 3}, { 'g': 4, 'r': 10}, { 'g': 2, 'b': 5, 'r': 4}],
    [{'b': 2}, { 'r': 4}, { 'r': 4, 'g': 5, 'b': 1}],
    [{'r': 7, 'g': 2, 'b': 17}, { 'g': 12, 'r': 1, 'b': 7}, { 'g': 9, 'r': 2, 'b': 8}],
    [{'g': 18, 'r': 5, 'b': 4}, { 'g': 20, 'b': 17, 'r': 5}, { 'r': 3, 'b': 7, 'g': 7}, { 'r': 4, 'g': 19, 'b': 18}, { 'b': 20, 'g': 20}],
    [{'g': 1, 'b': 6, 'r': 1}, { 'b': 5, 'r': 1, 'g': 3}, { 'g': 3, 'b': 7, 'r': 1}],
    [{'b': 4, 'g': 6, 'r': 13}, { 'r': 16, 'b': 7, 'g': 8}, { 'g': 4, 'r': 16}],
    [{'g': 5, 'r': 4, 'b': 13}, { 'r': 4, 'b': 12, 'g': 3}, { 'g': 6}],
    [{'r': 1, 'b': 17, 'g': 15}, { 'r': 6, 'g': 3, 'b': 9}, { 'g': 5, 'b': 1, 'r': 7}, { 'b': 6, 'r': 4, 'g': 4}],
    [{'b': 1, 'r': 11, 'g': 1}, { 'r': 2, 'g': 2, 'b': 1}, { 'r': 4, 'g': 1, 'b': 1}, { 'b': 2, 'r': 7, 'g': 3}, { 'r': 11, 'g': 3}],
    [{'r': 2, 'b': 1}, { 'g': 1, 'r': 1, 'b': 1}, { 'g': 5, 'r': 1}],
    [{'b': 9, 'r': 1}, { 'g': 1, 'r': 2, 'b': 11}, { 'r': 2, 'b': 6}],
    [{'b': 5, 'r': 7, 'g': 17}, { 'r': 5, 'g': 4, 'b': 7}, { 'r': 1, 'b': 3}, { 'r': 4, 'g': 12, 'b': 6}, { 'g': 6, 'b': 4, 'r': 3}],
    [{'b': 11, 'g': 12, 'r': 1}, { 'g': 8, 'r': 7, 'b': 9}, { 'r': 13, 'b': 12, 'g': 10}, { 'g': 5, 'b': 10, 'r': 3}],
    [{'b': 8, 'r': 1}, { 'r': 5, 'g': 2}, { 'b': 9, 'r': 6, 'g': 4}, { 'g': 4, 'r': 1, 'b': 13}, { 'b': 15, 'r': 3, 'g': 8}, { 'r': 6, 'g': 1, 'b': 4}],
    [{'b': 2, 'r': 1}, { 'r': 1, 'b': 4, 'g': 5}, { 'r': 3, 'b': 14, 'g': 2}],
    [{'b': 8, 'g': 10, 'r': 11}, { 'r': 5, 'b': 4, 'g': 19}, { 'r': 8, 'b': 3}, { 'r': 3, 'b': 3, 'g': 2}, { 'r': 4, 'g': 4}],
    [{'g': 3, 'r': 17}, { 'g': 7, 'r': 13, 'b': 5}, { 'b': 11, 'r': 10, 'g': 10}, { 'g': 3, 'r': 19, 'b': 4}, { 'g': 11, 'b': 6, 'r': 19}, { 'r': 5, 'b': 4, 'g': 9}],
    [{'b': 3, 'r': 4}, { 'r': 1, 'b': 1, 'g': 2}, { 'b': 4, 'g': 2, 'r': 4}],
    [{'r': 10, 'g': 3, 'b': 5}, { 'b': 2, 'r': 2}, { 'r': 7, 'b': 3, 'g': 2}],
    [{'r': 12, 'b': 1, 'g': 8}, { 'b': 1, 'g': 3, 'r': 10}, { 'g': 5, 'r': 8}],
    [{'r': 6, 'g': 4, 'b': 2}, { 'r': 7, 'b': 6, 'g': 14}, { 'b': 5, 'r': 6, 'g': 2}, { 'r': 2, 'b': 4}, { 'b': 7, 'g': 12}, { 'g': 7, 'b': 3, 'r': 8}],
    [{'r': 6, 'b': 5}, { 'b': 5, 'g': 1}, { 'b': 1, 'r': 6}, { 'b': 4, 'r': 2, 'g': 1}, { 'r': 3, 'b': 2}, { 'b': 3, 'r': 5, 'g': 1}],
    [{'r': 1, 'g': 12, 'b': 2}, { 'r': 4, 'b': 5}, { 'g': 12, 'r': 1}, { 'b': 5, 'r': 13, 'g': 17}, { 'g': 15, 'b': 1}],
    [{'b': 10, 'r': 18}, { 'b': 4, 'g': 1, 'r': 14}, { 'b': 4, 'g': 2}, { 'g': 2, 'r': 6, 'b': 10}],
    [{'g': 2, 'b': 13, 'r': 8}, { 'g': 7, 'r': 5, 'b': 8}, { 'r': 5, 'b': 8}, { 'r': 3, 'g': 5, 'b': 4}, { 'b': 15, 'r': 5, 'g': 6}],
    [{'r': 6, 'g': 7, 'b': 2}, { 'r': 2, 'g': 6}, { 'b': 2, 'r': 4, 'g': 5}, { 'b': 1, 'r': 2, 'g': 5}, { 'r': 4, 'g': 8}, { 'g': 9, 'r': 2}],
    [{'r': 4, 'b': 4}, { 'b': 7, 'r': 5}, { 'g': 8, 'r': 5, 'b': 6}, { 'r': 2, 'b': 3, 'g': 1}, { 'b': 7, 'g': 9, 'r': 7}, { 'g': 11, 'r': 2, 'b': 3}],
    [{'r': 1, 'g': 11, 'b': 9}, { 'r': 2, 'g': 5, 'b': 17}, { 'r': 2, 'b': 3, 'g': 6}, { 'r': 2, 'g': 6, 'b': 14}],
    [{'g': 7, 'r': 5, 'b': 2}, { 'r': 5, 'g': 7, 'b': 2}, { 'g': 6, 'b': 3, 'r': 15}, { 'g': 8, 'r': 20, 'b': 4}, { 'r': 8, 'g': 8, 'b': 3}, { 'b': 3, 'r': 11, 'g': 5}],
    [{'b': 2, 'g': 2}, { 'b': 6, 'g': 1, 'r': 3}, { 'r': 3, 'g': 7, 'b': 4}, { 'r': 1, 'g': 1, 'b': 8}],
    [{'g': 1, 'r': 3}, { 'g': 2, 'b': 1, 'r': 5}, { 'r': 2, 'g': 2, 'b': 1}, { 'g': 2, 'r': 3, 'b': 1}, { 'r': 6, 'b': 1}],
    [{'r': 4, 'g': 2, 'b': 3}, { 'r': 14}, { 'b': 3}, { 'r': 11, 'g': 1}, { 'r': 13, 'g': 3, 'b': 2}],
    [{'g': 1, 'b': 1, 'r': 6}, { 'g': 1, 'r': 4, 'b': 1}, { 'r': 6, 'b': 1}],
    [{'g': 1, 'b': 8, 'r': 10}, { 'g': 6, 'r': 3, 'b': 2}, { 'r': 14, 'g': 3}, { 'b': 9, 'g': 2, 'r': 2}, { 'b': 7, 'r': 5, 'g': 1}, { 'g': 6, 'b': 5, 'r': 10}],
    [{'r': 2, 'b': 10}, { 'r': 1, 'b': 7, 'g': 4}, { 'r': 1, 'g': 3, 'b': 6}],
    [{'r': 6, 'b': 6, 'g': 5}, { 'b': 1, 'g': 11, 'r': 7}, { 'r': 10, 'b': 7, 'g': 2}],
    [{'g': 4, 'r': 2, 'b': 3}, { 'r': 1, 'g': 6}, { 'r': 2, 'b': 4}, { 'b': 1}, { 'b': 2, 'g': 1}],
    [{'r': 10, 'b': 5, 'g': 1}, { 'b': 12}, { 'g': 2, 'b': 11, 'r': 9}, { 'b': 1, 'r': 14}, { 'r': 2, 'g': 2, 'b': 13}],
    [{'g': 9, 'b': 1}, { 'g': 8, 'b': 2, 'r': 7}, { 'b': 4, 'g': 7, 'r': 4}],
    [{'r': 14, 'b': 3, 'g': 10}, { 'b': 3, 'g': 7, 'r': 2}, { 'r': 5, 'g': 7, 'b': 3}, { 'r': 14, 'g': 8, 'b': 3}, { 'g': 9, 'r': 5}, { 'b': 2, 'r': 7, 'g': 15}],
    [{'b': 5, 'g': 9, 'r': 8}, { 'g': 11, 'b': 9, 'r': 4}, { 'r': 8, 'b': 2, 'g': 10}, { 'b': 3, 'g': 7}],
    [{'r': 4, 'b': 6, 'g': 10}, { 'b': 2, 'g': 17, 'r': 15}, { 'r': 15, 'b': 6, 'g': 14}],
    [{'r': 2, 'g': 8}, { 'b': 6, 'g': 6}, { 'g': 1, 'r': 3, 'b': 8}, { 'g': 5, 'b': 4, 'r': 3}, { 'b': 3, 'r': 1}, { 'g': 7, 'b': 8, 'r': 3}],
    [{'b': 5, 'r': 1}, { 'b': 10, 'r': 7, 'g': 3}, { 'g': 4, 'r': 1, 'b': 10}, { 'r': 8, 'b': 4, 'g': 3}, { 'b': 11, 'g': 9, 'r': 1}, { 'r': 6, 'g': 10}],
    [{'g': 1, 'b': 2, 'r': 1}, { 'b': 2, 'g': 1, 'r': 2}, { 'r': 2, 'g': 8}, { 'r': 3, 'b': 3, 'g': 5}],
    [{'b': 3, 'g': 4, 'r': 5}, { 'b': 6, 'r': 5, 'g': 5}, { 'r': 4, 'b': 2, 'g': 5}, { 'g': 2, 'b': 6, 'r': 5}, { 'r': 1, 'g': 2}],
    [{'b': 14, 'g': 1}, { 'g': 9, 'r': 3, 'b': 1}, { 'g': 5, 'b': 10, 'r': 3}, { 'g': 9}, { 'g': 6, 'b': 18}, { 'r': 2, 'g': 8}],
    [{'b': 1, 'r': 7}, { 'g': 12, 'r': 7, 'b': 5}, { 'b': 9, 'g': 6, 'r': 7}, { 'r': 10, 'g': 7, 'b': 1}, { 'g': 3, 'b': 6, 'r': 7}, { 'r': 10, 'b': 16}],
    [{'r': 9, 'b': 10, 'g': 2}, { 'r': 2, 'b': 12, 'g': 9}, { 'g': 11, 'b': 2, 'r': 3}],
    [{'b': 1, 'r': 7, 'g': 9}, { 'r': 1, 'b': 6}, { 'b': 3, 'g': 12}],
    [{'b': 1, 'g': 4}, { 'r': 4, 'b': 13, 'g': 1}, { 'g': 7, 'b': 4, 'r': 3}, { 'b': 2, 'g': 4, 'r': 5}, { 'r': 4, 'g': 7, 'b': 10}, { 'r': 1, 'g': 7, 'b': 13}],
    [{'b': 5, 'r': 8, 'g': 1}, { 'b': 7, 'g': 2, 'r': 7}, { 'g': 2, 'b': 8, 'r': 11}],
    [{'b': 5, 'g': 1, 'r': 11}, { 'b': 6, 'r': 8}, { 'r': 2, 'b': 3, 'g': 4}, { 'g': 2, 'b': 4, 'r': 7}, { 'b': 3, 'r': 8}, { 'r': 6, 'b': 3, 'g': 1}],
    [{'g': 2, 'r': 13, 'b': 9}, { 'b': 12, 'g': 6}, { 'g': 14, 'b': 10, 'r': 3}, { 'b': 13, 'g': 7, 'r': 5}, { 'g': 1, 'b': 9, 'r': 14}, { 'g': 10, 'b': 8, 'r': 17}],
    [{'g': 10, 'r': 3, 'b': 17}, { 'r': 13, 'g': 7, 'b': 15}, { 'b': 9, 'r': 8, 'g': 4}, { 'b': 1, 'r': 8}, { 'r': 9, 'g': 1, 'b': 19}],
    [{'b': 1, 'g': 7, 'r': 4}, { 'b': 2, 'g': 8}, { 'r': 10, 'g': 10, 'b': 1}, { 'g': 10, 'b': 2}, { 'r': 3, 'b': 3}],
    [{'r': 5, 'g': 8, 'b': 14}, { 'r': 4, 'g': 7, 'b': 20}, { 'b': 11, 'r': 4, 'g': 13}, { 'b': 18, 'r': 1, 'g': 3}],
    [{'r': 5, 'g': 8, 'b': 11}, { 'g': 12, 'b': 5}, { 'b': 4, 'g': 14}, { 'g': 7, 'b': 9, 'r': 5}, { 'r': 3, 'g': 4, 'b': 7}, { 'r': 3, 'b': 12, 'g': 3}],
    [{'r': 10, 'b': 12, 'g': 9}, { 'g': 4, 'b': 8, 'r': 4}, { 'b': 8, 'r': 3, 'g': 4}, { 'g': 6, 'r': 10}, { 'b': 2, 'g': 3, 'r': 15}, { 'r': 12, 'g': 2, 'b': 2}],
    [{'g': 13, 'b': 1}, { 'g': 9, 'r': 1, 'b': 1}, { 'b': 6, 'g': 10}, { 'r': 1, 'b': 6, 'g': 11}],
    [{'b': 2, 'g': 14, 'r': 2}, { 'g': 7, 'b': 1}, { 'b': 1, 'r': 1, 'g': 3}, { 'r': 2, 'b': 1, 'g': 15}, { 'b': 1, 'r': 2, 'g': 10}],
    [{'g': 3, 'r': 8, 'b': 7}, { 'r': 6, 'b': 13}, { 'r': 12, 'g': 4, 'b': 4}, { 'r': 12, 'g': 8, 'b': 3}, { 'b': 11, 'r': 11, 'g': 4}],
    [{'r': 2, 'b': 13, 'g': 1}, { 'g': 1, 'b': 12}, { 'r': 1, 'b': 5, 'g': 1}, { 'b': 3, 'r': 3}]
]

def cubes_game(games):
    ids_sum = 0

    for id, game in enumerate(games):
        game_id = id + 1
        
        for cubeset in game:
            if 'r' in cubeset and cubeset['r'] > RED:
                break
            if 'g'in cubeset and cubeset['g'] > GREEN:
                break
            if 'b'in cubeset and cubeset['b'] > BLUE:
                break
        else:
            # All cubesets of Game are valid
            ids_sum += game_id
            continue
  
    return ids_sum

print(cubes_game(input))