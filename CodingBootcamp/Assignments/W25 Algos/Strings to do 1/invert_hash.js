function invertHash(assocArr)
{
    var arr1 = []
    var arr2 = []
    var new_obj = {}
    for (key in assocArr)
    {
        arr1.push(key)
        arr2.push(assocArr[key])
    }
    for (i=0;i<arr1.length;i++)
    {
        new_obj[arr2[i]] = arr1[i]
    }
    return new_obj
}

console.log(invertHash({"name":"Zapphod","charm":"high","morals":"dicey"}));