function multiple_of_3()
{
    for (var num = -300; num < 1; num = num + 1)
    {
        if (num % 3 == 0 && num != -3 && num != -6)
        {
            console.log(num);
        }
    }
}

multiple_of_3()