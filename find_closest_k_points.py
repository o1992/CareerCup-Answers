import heapq
def find_k_elem(arr,dist,dict_loc,k):
    k_smallest = []
    heapq.heapify(dist)
    for i in range(k):
        tmp = heapq.heappop(dist)
        k_smallest.append(arr[dict_loc[tmp]])
    return k_smallest




def find_k_closest_points(arr,point,k):
    func = lambda x: ((x[0]-point[0])**2 + (x[1]-point[1])**2)**0.5
    dist = list(map(func,arr))
    dict_loc = {x:i for i,x in enumerate(dist)}

    return find_k_elem(arr,dist,dict_loc,k)


k=2
arr = [(1,2),(0,3.14),(0.5,0.5555),(1,3),(4,2),(3,6),(-1,0)]
print(find_k_closest_points(arr,(1,2),7))