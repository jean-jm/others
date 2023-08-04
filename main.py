# -*- coding: utf-8 -*-
# @Time    : 2023/7/24 6:20 PM
# @Author  : jiangmin5
# @Email   : jiangmin5@longfor.com
# @File    : main.py
# @Software: PyCharm

def min_windows(s, t):
    """
    S = "ADOCEFBGJCKLE"
    T = "ABC"
    求最小覆盖串
    :param s:
    :param t:
    :return:
    """

    s_list = list(s)
    h = len(s_list)
    print("==========")
    print(h)
    left = 0
    right = 0
    valid = 0
    start = 0
    len_max = 100000000

    window = {}
    need = {}
    for char in t:
        need[char] = need.get(char, 0) + 1

    while right < len(s_list):
        # 将移动到窗口内的值
        current_val = s_list[right]
        # 扩大窗口
        right = right + 1
        if need.keys().__contains__(current_val):
            if window.keys().__contains__(current_val):
                window[current_val] = window[current_val] + 1
            else:
                window[current_val] = 1
            if window[current_val] == need[current_val]:
                valid = valid + 1

        while valid == len(need):
            if (right - left) < len_max:
                start = left
                len_max = right - left
            left_shrink_val = s_list[left]
            # 缩小窗口
            left = left + 1
            if need.keys().__contains__(left_shrink_val):
                if window[left_shrink_val] == need[left_shrink_val]:
                    valid = valid - 1
                window[left_shrink_val] = window[left_shrink_val] - 1
    if len_max == 100000000:
        return ""
    else:
        return s[start: start + len_max]


if __name__ == '__main__':
    s = "ADOCECFBGACKLE"
    t = "ABC"
    res = min_windows(s, t)
    print(res)













