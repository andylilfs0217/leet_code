from collections import Counter


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        # return self.minWindow1(s, t)
        return self.minWindow2(s, t)

    def minWindow1(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        l, r, n = 0, 1, len(s)
        window = s[l:r]
        window_counter = Counter(window)
        ans = ''
        while l < n and r <= n and (ans == '' or len(ans) > len(t)):
            t_is_subset_of_window = True
            for tk, tv in t_counter.items():
                if window_counter[tk] < tv:
                    t_is_subset_of_window = False
                    break
            if t_is_subset_of_window and (ans == '' or len(ans) > len(window)):
                ans = window
            elif (t_is_subset_of_window
                  and l < r) or (not t_is_subset_of_window and r >= n):
                window_counter[s[l]] -= 1
                l += 1
            else:
                window_counter[s[r]] += 1
                r += 1
            window = s[l:r]
        return ans

    def minWindow2(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        need = len(t)
        have = 0
        l, r, n = 0, 0, len(s)
        ans = ''
        window_counter = Counter()
        while l < n and r <= n:
            if have < need and r < n:
                r += 1
                new_word = s[r - 1]
                if window_counter[new_word] < t_counter[new_word]:
                    have += 1
                window_counter[new_word] += 1
            else:
                removed_word = s[l]
                window_counter[removed_word] -= 1
                if window_counter[removed_word] < t_counter[removed_word]:
                    have -= 1
                l += 1
            window = s[l:r]
            if have == need and (ans == '' or r - l < len(ans)):
                ans = window
        return ans


print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
print(Solution().minWindow(s="a", t="a"))
print(Solution().minWindow(s="a", t="aa"))