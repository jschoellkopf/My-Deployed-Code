function acronyms(string)
{
    var acronym = string[0].toUpperCase()
    for (i in string)
    {
        if (string[i-1] == ' ')
        {
            acronym += string[i].toUpperCase()
        }
    }
    return acronym
}

console.log(acronyms("Live form New York - it's Saturday Night!"));