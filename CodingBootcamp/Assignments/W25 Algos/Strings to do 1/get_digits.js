function getDigits(string)
{
    var nums = '0123456789'
    new_string = ''
    for (i in string)
    {
        if (nums.includes(string[i]))
        {
            new_string += string[i]
        }
    }
    return new_string
}

console.log(getDigits('0s1a3y5w7h9a2t4?6!8?0'));