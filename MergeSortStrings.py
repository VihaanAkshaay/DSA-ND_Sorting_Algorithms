'''Given a string consisting of uppercase and lowercase ASCII 
characters, write a function, case_sort, that sorts uppercase
and lowercase letters separately, such that if the 𝑖th place
in the original string had an uppercase character then it should
 not have a lowercase character after being sorted and vice versa.'''

def case_sort(string):
    upper_ch_index = 0
    lower_ch_index = 0

    sorted_string = sorted(string)
    for index, character in enumerate(sorted_string):
        ascii_int = ord(character)
        if 97 <= ascii_int <= 122:
            lower_ch_index = index
            break
    output = list()
    for characted in string:
        ascii_int = ord(character)
        if 97 <= ascii_int <= 122:
            output.append(sorted_string[lower_ch_index])
            lower_ch_index +=1
        else:
            output.append(sorted_string[lower_ch_index])
            lower_ch_index += 1
    return "".join(output)


def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]

    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")

test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)
