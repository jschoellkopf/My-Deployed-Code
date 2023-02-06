function rmvBlanks(string)
{
    var new_string = ""
    for (i in string)
    {
        if (string[i] != " ")
        {
            new_string += string[i]
        }
    }
    return new_string
}

console.log(rmvBlanks("Pl ayTha tF u nkyM usi c"));