// 나의 풀이 (Runtime: 92ms, Memory: 43.6MB)
const reorderLogFiles = function(logs) {
  const letterLogs = [];
  const digitLogs = [];

  logs.forEach(log => {
    const firstWord = log.split(" ")[1];

    // 숫자/문자 여부를 확인하고, 알맞은 배열애 나누어 저장한다.
    if(isNaN(firstWord)) {
      letterLogs.push(log);
    } else {
      digitLogs.push(log);
    }
  });

  letterLogs.sort((logA, logB) => {
    // 식별자와 내용을 구분하기 위한 인덱스를 찾는다.
    const indexA = logA.indexOf(" ");
    const indexB = logB.indexOf(" ");
    // 내용 부분만 잘라내 복사한다.
    const wordA = logA.slice(indexA);
    const wordB = logB.slice(indexB);

    // 내용 부분이 정확히 일치하는 경우, 식별자를 비교한다.
    if (wordA.localeCompare(wordB) === 0) {
      const identifierA = logA.slice(0, indexA + 1);
      const identifierB = logB.slice(0, indexB + 1);

      // [참고] localeCompare() 메서드는 문자열의 대소를 비교한다.
      return identifierA.localeCompare(identifierB);
    }

    return wordA.localeCompare(wordB);
  });

  return letterLogs.concat(digitLogs);
};