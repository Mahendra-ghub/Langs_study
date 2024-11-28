def maxOutlets(num, reqOutletsIDs, roadCon):
    # Create an adjacency list for the graph
    graph = {i: [] for i in range(1, num + 1)}
    for road in roadCon:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    # Convert reqOutletsIDs to a set for fast lookup
    reqOutlets = set(reqOutletsIDs)

    # Helper function to perform DFS and count connected outlets
    def dfs(node, visited):
        if node in visited:
            return 0
        visited.add(node)
        count = 1 if node in reqOutlets else 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                count += dfs(neighbor, visited)
        return count

    # Calculate the maximum number of outlets that can be connected starting from each requested outlet
    max_deliveries = 0
    for outlet in reqOutlets:
        visited = set()
        max_deliveries = max(max_deliveries, dfs(outlet, visited))

    return max_deliveries

def main():
    # Input for the number of outlets
    num = int(input().strip())
    
    # Input for the number of requested outlets
    reqOutletsIDs_size = int(input().strip())
    
    # Input for the requested outlet IDs
    reqOutletsIDs = list(map(int, input().strip().split()))
    
    # Input for the road connections (edges)
    roadCon = []
    roadCon_rows, roadCon_cols = map(int, input().strip().split())
    for _ in range(roadCon_rows):
        roadCon.append(list(map(int, input().strip().split())))

    # Call the function and print the result
    result = maxOutlets(num, reqOutletsIDs, roadCon)
    print(result)

if __name__ == "__main__":
    main()
