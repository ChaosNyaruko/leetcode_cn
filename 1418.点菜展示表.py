    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dishes = set()
        counter = [collections.defaultdict(int) for _ in range(501)]
        for order in orders:
            t, dish = int(order[1]), order[2]
            dishes.add(dish)
            counter[t][dish] += 1
        
        dishes = sorted(dishes)
        #print(dishes)
        
        #dishes = list(dishes)
        #dishes.sort()
        #print(dishes)
        res = [['Table']]
        for d in dishes:
            res[0].append(d)

        for i in range(1, 501):
            if not counter[i]:
                continue
            curTable = [str(i)]
            for d in dishes:
                curTable.append(str(counter[i][d]))
            res.append(curTable)
        #print(res)
        return res
