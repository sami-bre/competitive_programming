class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        d_array = []
        for point in points:
            d_array.append((point[0]**2 + point[1]**2, point))
            
        d_array.sort()
        
        print(d_array)
        temp = []
        for item in d_array[:k]:
            temp.append(item[1])
        
        return temp
            
            
        # for i in range(len(d_array)):
        #     least_index = i
        #     for j in range(i,len(d_array)):
        #         if(d_array[j]<d_array[least_index]):
        #             least_index = j
        #     d_array[i], d_array[least_index] = d_array[least_index], d_array[i]
        #     points[i], points[least_index] = points[least_index], points[i]
            
        # return points[:k]