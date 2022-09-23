function pizzaOven(crustType,sauceType,cheeses,toppings){
    var pizza = {};
    pizza.crust = crustType;
    pizza.sauce = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

var pizza1 = pizzaOven("deep dish","traditional",["mozzarella"],["mustard","fried onions","arugula"]);
// console.log(pizza1)

var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"],["mushroom","olives","onions"])
// console.log(pizza2)

var pizza3 = pizzaOven("thin","spicy red",["mozzarella","ricotta"],["fresh basil","kalamata olives","roasted garlic"])
// console.log(pizza3)

var pizza4 = pizzaOven("thick","spicy red",["mozzarella","parmesan"],["pepperoni","sausage","artichokes"])
// console.log(pizza4)

var crust = ["deep dish","hand tossed","thin","thick"]
var sauce = ["traditional","marinara","spicy red"]
var cheeses = ["mozzarella","feta","ricotta","parmesan"]
var toppings = ["mustard","fried onions","arugula","mushrooms","olives","onions","fresh basil","kalamata olives","roasted garlic","pepperoni","sausage","artichokes"]

function randomPizza(crust, sauce, cheeses, toppings){
    var pizza = {};
    pizza.crust = crust[Math.floor(Math.random() * crust.length)]
    pizza.sauce = sauce[Math.floor(Math.random() * sauce.length)]
    pizza.cheeses = [cheeses[Math.floor(Math.random() * cheeses.length)],cheeses[Math.floor(Math.random() * cheeses.length)]]
    // 2 cheeses and 3 toppings
    pizza.toppings = [toppings[Math.floor(Math.random() * toppings.length)], toppings[Math.floor(Math.random() * toppings.length)],toppings[Math.floor(Math.random() * toppings.length)]];
    return pizza
}

randPizza = randomPizza(crust, sauce, cheeses, toppings)
randPizza.toppings.push("secret ingredient")
// can only use .push if key contains a array, not possible on crust or sauce
console.log(randPizza)
