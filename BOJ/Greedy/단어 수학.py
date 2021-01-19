# 1339 : 단어 수학
#
# 각 알파벳의 자릿수 별 가중치를 구하고,
# 가중치가 높은 알파벳부터 높은 수를 배정해 합을 구해야 한다.
#

num_of_words = int(input())
words = []
bias = {}

for _ in range(num_of_words):
    words.append(input())

for word in words:
    word_length = len(word)

    for index in range(word_length):
        character = word[index]
        if bias.get(character):
            bias[character] += (10 ** (word_length - index - 1))
        else:
            bias[character] = (10 ** (word_length - index - 1))

bias_array = sorted(list(bias.values()), reverse=True)
number = 9
acc = 0

for each in bias_array:
    acc += each * number
    number -= 1

print(acc)

# 첫번째 시도
#
# counters = [[], [], [], [], [], [], [], []]
# num_of_words = int(input())
# words = []
# used = []
# assigned = {}
# number = 9
#
# for _ in range(num_of_words):
#     words.append(input())
#
# for word in words:
#     for digit in range(len(word)):
#         index = len(word) - digit - 1
#         counters[index].append(word[digit])
#
# counters.reverse()
#
# for digit in counters:
#     for char in digit:
#         if used.count(char) is 0:
#             used.append(char)
#             assigned[char] = str(number)
#             number -= 1
#
# translated_numbers = []
#
# for word in words:
#     temp = ""
#     for char in word:
#         temp += assigned.get(char)
#     translated_numbers.append(int(temp))
#
# print(sum(translated_numbers))