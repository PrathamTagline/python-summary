String = "aaabbbiiidsnowfnowowerworuworjwohicnscmsojpscpkxsnowfwpfwonfbowbfownfwpfmwfnqeqeuwryuiewurowndwncbviagsdodjwoeirowqewnbcvbowvwpdwufiwoufpwj";
charcter_arr = String.split("");
map = {}
total_a = charcter_arr.filter(x => x === "a").length;
total_e = charcter_arr.filter(x => x === "e").length;
total_i = charcter_arr.filter(x => x === "i").length;
total_o = charcter_arr.filter(x => x === "o").length;
total_u = charcter_arr.filter(x => x === "u").length;

map.a = total_a;
map.e = total_e;
map.i = total_i;
map.o = total_o;
map.u = total_u;

console.log(map);