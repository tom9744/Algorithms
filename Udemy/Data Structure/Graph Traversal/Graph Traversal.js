/**
 * 그래프 자료구조의 자세한 구현 방법보다는 개념을 설명하기 위한 것으로,
 * 예외 처리에 대한 구현은 포함되지 않았다.
 */
 class UndirectedGraph {
    constructor() {
        this.adjList = {};
    }

    addVertex(vertex) {
        if(!this.adjList[vertex]) this.adjList[vertex] = [];
    }

    addEdge(vertexA, vertexB) {
        if (!this.adjList[vertexA] || !this.adjList[vertexB]) return false;

        this.adjList[vertexA].push(vertexB);
        this.adjList[vertexB].push(vertexA);
    }

    removeEdge(vertexA, vertexB) {
        if (!this.adjList[vertexA] || !this.adjList[vertexB]) return false;

        this.adjList[vertexA] = this.adjList[vertexA].filter(vertex => vertex !== vertexB);
        this.adjList[vertexB] = this.adjList[vertexB].filter(vertex => vertex !== vertexA);
    }
    
    removeVertex(vertex) {
        if(!this.adjList[vertex]) return false;

        while (this.adjList[vertex].length > 0) {
            const adjVertex = this.adjList[vertex].pop();

            this.removeEdge(vertex, adjVertex);
        }

        delete this.adjList[vertex];

        return true;
    }

    recursiveDFS(startingVertex) {
        if (!this.adjList[startingVertex]) return;

        const result = [];
        const visited = {};
        const DFS = (vertex) => {
            if (visited[vertex]) return;

            // 현재 노드를 방문처리하고, 결과 배열에 추가한다.
            visited[vertex] = true; 
            result.push(vertex);    

            // 아직 방문하지 않은 자식 노드가 존재하면, 재귀적으로 호출한다.
            this.adjList[vertex].forEach(adjVertex => {
                if (!visited[adjVertex]) {
                    DFS(adjVertex);
                }
            });
        };

        DFS(startingVertex);

        return result;
    }

    iterativeDFS(startingVertex) {
        const stack = [startingVertex, ];
        const result = [];
        const visited = {};

        while (stack.length > 0) {
            const currentVertex = stack.pop();

            if (!visited[currentVertex]) {
                visited[currentVertex] = true;
                result.push(currentVertex);

                this.adjList[currentVertex].forEach(vertex => {
                    if (!visited[vertex]) {
                        stack.push(vertex);
                    }
                });
            }
        }

        return result;
    }

    BFS(startingVertex) {
        const queue = [startingVertex, ];
        const result = [];
        const visited = {};

        while (queue.length > 0) {
            const currentVertex = queue.pop();

            if (!visited[currentVertex]) {
                visited[currentVertex] = true;
                result.push(currentVertex);

                this.adjList[currentVertex].forEach(vertex => {
                    if (!visited[vertex]) {
                        queue.unshift(vertex);
                    }
                });
            }
        }

        return result;
    }
}

const graph = new UndirectedGraph();

graph.addVertex("A");
graph.addVertex("B");
graph.addVertex("C");
graph.addVertex("D");
graph.addVertex("E");
graph.addVertex("F");
graph.addEdge("A", "B");
graph.addEdge("B", "D");
graph.addEdge("D", "E");
graph.addEdge("F", "E");
graph.addEdge("D", "F");
graph.addEdge("A", "C");
graph.addEdge("C", "E");

graph.recursiveDFS("A");  // (6) ["A", "B", "D", "E", "F", "C"]
graph.iterativeDFS("A");  // (6) ["A", "C", "E", "F", "D", "B"]
graph.BFS("A");           // (6) ["A", "B", "C", "D", "E", "F"]