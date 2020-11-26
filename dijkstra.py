from heapq import heappop
from heapq import heappush

def dijkstra(graph, start):
    
    cache = {i: float('inf') for i in graph.keys()}
    queue = []

    cache[start] = 0
    heappush(queue, [cache[start], start])    

    while queue:
        current_distance, current_node = heappop(queue)

        if cache[current_node] < current_distance:
            print("123")
            continue

        for adjacent, weight in graph[current_node].items():

            # 이번노드까지 오는데 걸린 거리에서 다음노드까지의 거리를 더한다.
            distance = current_distance + weight

            # 최단경로라면 캐시에 있는 값을 증가시켜주고
            # 캐시에 있는 값을 업데이트 시켜주고
            # 큐에 그 경로까지 오는 거리와 노드를 넣어준다.
            if distance < cache[adjacent]:
                cache[adjacent] = distance
                heappush(queue, [distance, adjacent])
    return cache
        


graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(graph,'A'))

# 최단경로 알고리즘
# 다익스트라 알고리즘이라고 부르며 너비우선탐색(BFS)과 유사하다
# 현재 경로와 현재 경로까지 오는 거리를 큐에 저장해주고 하나씩 빼면서 캐시(최단거리 저장)에 있는값보다 작다면 캐시를 업데이트해주고
# 큐에 현재경로와 현재경로까지 오는 거리를 저장해주는 방식이다.



