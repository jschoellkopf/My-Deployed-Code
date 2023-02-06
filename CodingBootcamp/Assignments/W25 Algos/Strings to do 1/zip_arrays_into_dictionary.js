function arr_to_dic(arr1,arr2)
{
    var myDict = {}
    for (i=0;i<arr1.length;i++)
    {
        myDict[arr1[i]] = arr2[i]
    }
    return myDict
}

console.log(arr_to_dic(["abc",3,"yo"],[42,"wassup",true]));
// not sure why this is not in the right order in the dictionary