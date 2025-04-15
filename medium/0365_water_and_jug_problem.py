class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        def check_meet_target(jug_x: int, jug_y: int, target: int) -> bool:
            return jug_x == target or jug_y == target or jug_x + jug_y == target

        queue = [(x, 0), (0, y)]
        found_res = False
        visited = set()

        while queue and not found_res:
            ele = queue.pop(0)
            if ele not in visited:
                visited.add(ele)
                jug_x, jug_y = ele

                # For each action, check if (or)
                # 1. x == target
                # 2. y == target
                # 3. x + y == target
                if check_meet_target(jug_x, jug_y, target):
                    found_res = True
                else:
                    # Actions:
                    # 1. Fill x
                    if jug_x < x:
                        queue.append((x, jug_y))
                    # 2. Fill y
                    if jug_y < y:
                        queue.append((jug_x, y))
                    # 3. Empty x
                    if jug_x > 0:
                        queue.append((0, jug_y))
                    # 4. Empty y
                    if jug_y > 0:
                        queue.append((jug_x, 0))
                    # 5. Transfer x to y
                    if jug_x > 0 and jug_y < y:
                        available_space = y - jug_y
                        available_water = jug_x
                        transferrable = min(available_space, available_water)
                        after_x = jug_x - transferrable
                        after_y = jug_y + transferrable
                        queue.append((after_x, after_y))
                    # 6. Transfer y to x
                    if jug_x < x and jug_y > 0:
                        available_space = x - jug_x
                        available_water = jug_y
                        transferrable = min(available_space, available_water)
                        after_x = jug_x + transferrable
                        after_y = jug_y - transferrable
                        queue.append((after_x, after_y))

        return found_res


print(Solution().canMeasureWater(x=3, y=5, target=4))  # True
print(Solution().canMeasureWater(x=2, y=6, target=5))  # False
print(Solution().canMeasureWater(x=1, y=2, target=3))  # True
