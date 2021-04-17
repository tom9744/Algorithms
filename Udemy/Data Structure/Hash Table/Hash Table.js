/**
 * [Average Case]
 * Insertion: O(1)
 * Removal: O(1)
 * Access: O(1)
 * 
 * 해시 테이블은 평균적으로 모든 동작에 대해 O(1)의 압도적인 성능을 가지지만,
 * 해시 함수의 성능에 따라 데이터의 추가/삭제/접근에 대한 시간 복잡도가 달라질 수 있다.
 * 
 * 따라서, 시간 복잡도 O(1)의 해시 함수를 구현하는 것이 가장 중요하다.
 */
class HashTable {
    constructor(size=53) {
        this.keyMap = new Array(53).fill(null);
    }

    _hash(key) {
        const WEIRD_PRIME = 31;
        let total = 0;
        
        for (let i = 0; i < Math.min(key.length, 100); i++) {
            const char = key[i];
            const value = char.charCodeAt(0) - 96;
            total = (total * WEIRD_PRIME + value) % this.keyMap.length;
        }

        return total;
    }

    set(key, value) {
        const index = this._hash(key);

        if (!this.keyMap[index]) {
            this.keyMap[index] = [];
        }       
        this.keyMap[index].push([key, value]);   
    }

    get(inputKey) {
        const index = this._hash(inputKey);
        let result;

        if (this.keyMap[index]) {
            const pairs = this.keyMap[index]; 
            result = pairs.find(([key, _]) => key === inputKey);
        }

        return result ? result[1] : result;
    }
    
    // 해시 테이블의 모든 Key 값을 반환한다. (= Object.keys())
    keys() {
        let keyArray = [];

        this.keyMap.forEach(pairs => {
            if (pairs) {
                pairs.forEach(([key, _]) => {
                    if (!keyArray.includes(key)) {
                        keyArray.push(key);
                    }
                })
            }
        })

        return keyArray;
    }

    // 해시 테이블의 중복되지 않은 모든 Value 값을 반환한다. (= Object.values())
    values() {
        let valueArray = [];

        this.keyMap.forEach(pairs => {
            if (pairs) {
                pairs.forEach(([_, value]) => {
                    if (!valueArray.includes(value)) {
                        valueArray.push(value);
                    }
                })
            }
        })

        return valueArray;
    }
}

const hashTable = new HashTable();
hashTable.set("maroon", "#800000");
hashTable.set("yellow", "#FFFF00");
hashTable.set("olive", "#808000");
hashTable.set("salmon", "#FA8072");
hashTable.set("lightcoral", "#F08080");
hashTable.set("plum", "#DDA0DD");

hashTable.get("yellow"); // #FFFF00
hashTable.get("green")   // undefined

// 출력 결과에서 확인할 수 있듯, 순서를 보장하지 않는다!
hashTable.values(); // ["#FFFF00", "#808000", "#800000", "#FA8072", "#DDA0DD", "#F08080"]
hashTable.keys();   // ["yellow", "olive", "maroon", "salmon", "plum", "lightcoral"]