String = "aaabbbiii";

a = String.split('').reduce((acc, curr) => acc + curr.count("a"), 0);
console.log(a);
