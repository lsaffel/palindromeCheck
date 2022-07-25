# Write a function that takes in a non-empty string and that returns a
# boolean representing whether the string is a palindrome.
# A palindrome is defined as a string that's written the same forward and
# backward. Note that single-character strings are palindromes

def isPalindrome(string):
    # print("length of the string", string, "is", len(string))
    # # print("Character 2 in the string", string, "is", string[2])
    # print("Last character in the string", string, "is", string[len(string)-1])

    left = 0
    right = len(string)-1

    # loop through the string, comparing characters at left and right
    # if the characters are not the same, then return False
    # else left ++ and right --

    while left < right:
        if string[left] != string[right]:   # correct syntax ?
            return False
        left += 1
        right -= 1

    return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(isPalindrome("abc"))
    print(isPalindrome("a"))
    print(isPalindrome("bb"))
    print(isPalindrome("aba"))
    print(isPalindrome("abba"))
    print(isPalindrome("abcba"))
    print(isPalindrome("ablaba"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
