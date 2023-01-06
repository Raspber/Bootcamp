

// Array Reverse
// Write a function that will reverse the values an array and return them.

function reverse(arr) {
    var left = 0;
    var right = arr.length - 1;
    while (left < right){
        var temp = arr[right];
        arr[right] = arr[left];
        arr[left] = temp;
        left++;
        right--;
    }
    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]
