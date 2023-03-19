function createSecretHolder(x) {
    secret = {
        content: x,
        getSecret : function() {
            return this.content;
        },
        setSecret : function(secret) {
            return this.content = secret;
        },
    };
    return secret
}


obj = createSecretHolder(5)
console.log(obj)
console.log(obj.getSecret())
console.log(obj.setSecret(3))
console.log(obj)