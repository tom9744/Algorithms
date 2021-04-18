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
}

const graph = new UndirectedGraph();

graph.addVertex("Dallas");
graph.addVertex("Tokyo");
graph.addVertex("Aspen");
graph.addVertex("Los Angeles");
graph.addVertex("Hong Kong");

graph.addEdge("Dallas", "Tokyo");
graph.addEdge("Dallas", "Aspen");
graph.addEdge("Hong Kong", "Tokyo");
graph.addEdge("Aspen", "Tokyo");
graph.addEdge("Los Angeles", "Hong Kong");
graph.addEdge("Los Angeles", "Dallas");
