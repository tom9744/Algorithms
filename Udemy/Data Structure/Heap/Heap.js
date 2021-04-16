class MaxBinaryHeap {
    constructor() {
        this.values = [41, 39, 33, 18, 27, 12];
    }

    swap(indexA, indexB) {
        const temp = this.values[indexA];
        this.values[indexA] = this.values[indexB];
        this.values[indexB] = temp;
    }

    insert(value) {
        // 1. Add to the end
        this.values.push(value);        
        
        // 2. Bubble Up 
        let currIndex = this.values.length - 1;
        let parentIndex = Math.floor((currIndex - 1) / 2);

        while (currIndex > 0) {
            if (this.values[currIndex] < this.values[parentIndex]) break;
            
            this.swap(currIndex, parentIndex);
            currIndex = parentIndex;
            parentIndex = Math.floor((currIndex - 1) / 2);
        }
    }
}

const heap = new MaxBinaryHeap();