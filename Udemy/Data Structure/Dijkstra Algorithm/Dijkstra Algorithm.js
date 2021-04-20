class FakePriorityQueue {
    constructor() {
        this.values = [];
    };
    enqueue(val, priority) {
        this.values.push({ val, priority });
        this.sort();
    };
    dequeue() {
        return this.values.shift();
    };
    sort() {
        this.values.sort((valueA, valueB) => valueA.priority - valueB.priority);
    };
}

class WeightedGraph {
    constructor() {
        this.adjList = {};
    }

    addVertex(vertex) {
        if (!this.adjList[vertex]) this.adjList[vertex] = [];
    }

    addEdge(vertexA, vertexB, weight) {
        if (!this.adjList[vertexA] || !this.adjList[vertexB]) return false;

        this.adjList[vertexA].push({ node: vertexB, weight });
        this.adjList[vertexB].push({ node: vertexA, weight });
    }

    dijkstra(start, dest) {
        if (!start || !dest) return false;

        const nodes = new FakePriorityQueue();
        const distances = {};
        const previous = {};
        const path = [];

        // 0. 초기 상태를 설정한다.
        for (let vertex in this.adjList) {
            if (vertex === start) {
                // 출발 정점의 비용은 0이다.
                distances[vertex] = 0;      
                nodes.enqueue(vertex, 0);   
            } else {
                distances[vertex] = Infinity;
                nodes.enqueue(vertex, Infinity);
            }
            previous[vertex] = null;
        }

        // 1. 우선순위 큐에 방문할 다음 노드가 존재하는 경우, 
        while (nodes.values.length) {
            // 1-1. 최소 비용을 가지는 노드를 꺼낸다.
            const { val: smallest } = nodes.dequeue();

            // 1-2. 목적지에 도착하면 경로를 생성한다.
            if (smallest === dest) { 
                const current = dest;

                // 출발지의 previous는 null이므로, 반복문이 종료된다.
                while (previous[current]) {
                    path.push(current);
                    current = previous[current];
                }

                path.push(start); // 출발지를 경로에 추가한다.

                return path.reverse();
            }

            // 1-3. 해당 정점의 이웃 정점에 대해 다음을 수행한다.
            if (smallest || distances[smallest] !== Infinity) {
                // 1-3-1. 이웃하는 정점을 찾는다.
                for (const neighbor of this.adjList[smallest]) {
                    const { node, weight } = neighbor;

                    // 1-3-2. 이웃 정점으로의 새로운 거리를 계산한다.
                    const newDistance = distances[smallest] + weight;

                    // 1-3-3. 새로 계산한 거리가 기존의 거리보다 작다면,
                    if (newDistance < distances[node]) {
                        // 이웃 정점까지의 새로운 최소 거리를 갱신한다.
                        distances[node] = newDistance;
                        // 이웃 정점으로 도달하기 위해 방문한 직전 노드를 갱신한다.  
                        previous[node] = smallest;
                        // 우선순위 큐에 새로운 비용으로 추가한다.
                        nodes.enqueue(node, newDistance);
                    }
                } 
            }            
        }
    }
}

const weighted = new WeightedGraph();

weighted.addVertex("A");
weighted.addVertex("B");
weighted.addVertex("C");
weighted.addVertex("D");
weighted.addVertex("E");
weighted.addVertex("F");
 
weighted.addEdge("A", "B", 4);
weighted.addEdge("A", "C", 2);
weighted.addEdge("B", "E", 3);
weighted.addEdge("C", "D", 2);
weighted.addEdge("C", "F", 4);
weighted.addEdge("D", "E", 3);
weighted.addEdge("D", "F", 1);
weighted.addEdge("E", "F", 1);

console.log(weighted.adjList);
 
graph.dijskstras("A", "E")