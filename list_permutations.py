# -*- coding: utf-8 -*-
# @Time    : 2023/8/2 2:26 PM
# @Author  : jiangmin5
# @Email   : jiangmin5@longfor.com
# @File    : list_permutations.py
# @Software: PyCharm


def list_permutations(original_list, res, res_final):

    for i in original_list:
        if len(original_list) == 1:
            res.append(i)
            res_final.append(res)
            return
        index_i = i.__index__() - 1
        index_s = index_i - 1
        index_e = index_i + 1
        if index_s  < 0:
            index_pre_list = []
        else:
            index_pre_list = original_list[0:index_s+1]

        if index_e >= len(original_list):
            index_beh_list = []
        else:
            index_beh_list = original_list[index_e:]

        remain_list = index_pre_list + index_beh_list
        res.append(i)
        list_permutations(remain_list, res, res_final)

    return res


def permute(nums):
    def backtrack(start):
        print("start", start)
        if start == len(nums) - 1:
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            print("====i", i, "====start", start)
            nums[start], nums[i] = nums[i], nums[start]
            # print(nums[start], nums[i])
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0)
    return result


def all_fun(original_list):
    res_final = []
    res = []
    used = [False] * len(original_list)

    def list_permutations(original_list, res, used):
        # 结束条件
        if len(res) == len(original_list):
            res_final.append(res[:]) # 应该把res的副本添加进去，而不是res，因为res之后还是会继续变化的
            return
        for i in range(len(original_list)):
            if used[i]:
                continue
            res.append(original_list[i])
            used[i] = True
            # 进入下一层决策树
            list_permutations(original_list, res, used)
            # 取消选择
            del res[-1]
            used[i] = False

    list_permutations(original_list, res, used)
    return res_final


def n_queen(n):
    original_list = []
    for i in range(n):
        original_list.append(i+1)
    rst = all_fun(original_list)
    rst_vct = []
    for i in rst:
        vct = []
        for j in i:
            s = "...."
            s = s[:j-1] + 'Q' + s[j:]
            vct.append(s)

        rst_vct.append(vct)
    return rst_vct


if __name__ == '__main__':
    # original_list1 = [1, 2, 3]
    # # original_list1.remove(1)
    # # print(original_list1)
    # a = original_list1[4]
    # c = original_list1
    # b = a + c
    # print(b)
    # original_list = [0,1,2,]
    # res = []
    # res_final = []
    # 示例
    # nums = [1, 2, 3]
    # print(permute(nums))
    # print(all_fun(original_list))
    # s = "...."
    # j = 2
    # s = s[:j-1] + 'Q' + s[j:]
    # print(s)
    print(n_queen(4))


