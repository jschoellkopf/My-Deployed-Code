function flex_countdown(lowNum, highNum, mult)
{
    for (num = highNum; num >= lowNum; num -= mult)
    {
        console.log(num);
    }
}

flex_countdown(2,9,3)