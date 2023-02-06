function isCreditCardValid(digitArr)
{
    var sum = 0
    
    // 1. set a side last digit
    var last_num = digitArr.splice(digitArr.length-1,1)
    
    // 2. multiply digits in odd positions by 2
    for (i=digitArr.length-1; i>= 0; i-=2)
    {
        digitArr[i] = digitArr[i]*2
        // 3. if results are larger than 9, substract 9 from them
        if (digitArr[i] > 9)
        {
            digitArr[i] = digitArr[i] - 9
        }
    }
    // 4. add up all the digits
    for (i=0;i<digitArr.length;i++)
    {
        sum += digitArr[i]
    }
    // 5. adding the last digit backk in and check if multiple of 10
    if ((sum + parseInt(last_num))%10 == 0)
    {
        return true
    }
    else
    {
        return false
    }
}

console.log(isCreditCardValid([2,4,0,0,1,4,5,7,9,3,8,8,0,5,2,7,3]))