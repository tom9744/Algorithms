class Solution:
    # 나의 풀이 (Runtime: 72ms, Memory: 14.2MB)
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        itinerary_graph = {}
        result = []
        
        # 출발지와 도착지를 나타내는 그래프를 형성하며, 정렬해준다.
        for src, dest in sorted(tickets):
            if src not in itinerary_graph:
                itinerary_graph[src] = [] 
            if dest not in itinerary_graph:
                itinerary_graph[dest] = [] 
            itinerary_graph[src].append(dest)
        
        def dfs(graph, start='JFK'):
            # [중요] dfs를 먼저 호출한 뒤, result에 추가해야 한다.
            # 그렇지 않으면 [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]에서 틀린다. 
            while itinerary_graph[start]:
                next_start = itinerary_graph[start].pop(0)
                dfs(graph, next_start)
            result.append(start)
            
        dfs(itinerary_graph)
        
        # 뒤집어서 출력해야 순서가 맞다.
        return result[::-1]