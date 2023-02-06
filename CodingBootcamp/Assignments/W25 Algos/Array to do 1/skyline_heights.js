function skyline_heights(arr)
{
    var arr2 = []
    for (i = 1; i < arr.length; i++)
    {
        if (arr[i] > arr[i-1])
        {
            arr2.push(arr[i])
        }
    }
    return arr2
}

console.log(skyline_heights([-1,1,1,7,3,10,9]))