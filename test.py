# -*- coding: utf-8 -*-
# @Time    : 2023/7/24 7:23 PM
# @Author  : jiangmin5
# @Email   : jiangmin5@longfor.com
# @File    : test.py
# @Software: PyCharm

# 滑动窗口
def min_windows(s, t):
    s_list = list(s)
    left = 0
    right = 0
    valid = 0
    start = 0
    len_max = 100000000

    window = {}
    need = {}
    for char in t:
        need[char] = need.get(char, 0) + 1
    print(need)

    while right < len(s_list):
        current_val = s_list[right]
        right = right + 1
        if current_val in need:
            window[current_val] = window.get(current_val, 0) + 1
            if window[current_val] == need[current_val]:
                valid = valid + 1

        # if need.keys().__contains__(current_val):
        #     if window.keys().__contains__(current_val):
        #         window[current_val] = window[current_val] + 1
        #     else:
        #         window[current_val] = 1
        #     if window[current_val] == need[current_val]:
        #         valid = valid + 1

        while valid == len(need):
            if right - left < len_max:
                start = left
                len_max = right - left
            left_shrink_val = s_list[left]
            left += 1
            if left_shrink_val in need:
                if window[left_shrink_val] == need[left_shrink_val]:
                    valid -= 1
                window[left_shrink_val] -= 1

    if len_max == 100000000:
        return ""
    else:
        return s[start : start + len_max]





if __name__ == '__main__':
    # Test
    S = "ADOCECFBGACKLE"
    T = "ABC"
    result = min_windows(S, T)
    print(result)  # Output: "BGC"

