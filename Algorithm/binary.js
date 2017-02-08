'use strict';

function binarySearch (sortedArray, searchedNumber) {
  var listLength = sortedArray.length;
  var high = listLength;
  var low = 0;
  var actualPosition;
  var actualElement;
  var result = false;

  while (!result && high != low && low < listLength - 1) {

    actualPosition = Math.floor((high - low) / 2 + low);
    actualElement = sortedArray[actualPosition];

    if (actualElement === searchedNumber) {
      result = true;
      console.log(actualPosition);
    } else if (actualElement > searchedNumber) {
      high = actualPosition;
    } else if (actualElement < searchedNumber) {
      low = actualPosition;
    }
    console.log(low, high, actualPosition);
  }
  return result
}

console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 10));
