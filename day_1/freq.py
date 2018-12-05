#assume number come in on a file, each line has only one number
import sys
def find_first_dup_freq(numbers, running_total, prev_freq_set, ):
    prev_freq_set.add(0)
    for (idx, x) in enumerate(numbers):
        running_total = running_total + int(x)
        if running_total in prev_freq_set:
            print("FOUND")
            return running_total
        prev_freq_set.add(running_total)
    return find_first_dup_freq(numbers, running_total, prev_freq_set)


input_file = sys.argv[1]
numbers = []
with open(input_file, 'r') as fp:
    for x in fp:
        numbers.append(int(x))
print(sum(numbers))
print(find_first_dup_freq(numbers, 0, set()))

