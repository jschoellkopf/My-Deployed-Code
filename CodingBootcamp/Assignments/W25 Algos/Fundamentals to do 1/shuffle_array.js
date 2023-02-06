function shuffle(a) {
    var j, x;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        // console.log(j);
        x = a[i];
        // console.log(x);
        // console.log(a[j]);
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}

console.log(shuffle([3,5,9,2,0,1])); 