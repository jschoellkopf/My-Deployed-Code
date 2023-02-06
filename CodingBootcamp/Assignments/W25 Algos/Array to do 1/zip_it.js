// function zip_it(arr1,arr2)
// {
//     var big_arr = [...arr1,...arr2];
//     return big_arr.sort(function(a,b){return a-b})
// }

// console.log(zip_it([1,3,5,29,12,18],[5,11,17,40,42]));
//

function zip_it2(arr1,arr2)
{
    var new_arr = []
    var big_arr = arr1.concat(arr2);
    
    for ( a = 0; a < big_arr.length; a++)
    {
        for ( i = 0; i < big_arr.length; i++)
        {
            if (Math.min(...big_arr) == big_arr[i])
            {
                new_arr = new_arr.concat(big_arr.splice(i,1));
            }
        }
        a--
    }
    return new_arr
}

console.log(zip_it2([2,3,1,5,29,12,18],[5,11,17,40,42]));