function dojo_counting()
{
    for (var num = 1; num < 101; num++)
    {
        if (num % 10 == 0)
        {
            console.log("Dojo");
            continue
        }
        if (num % 5 == 0)
        {
            console.log("Coding");
            continue
        }
        console.log(num)
    }
}

dojo_counting()