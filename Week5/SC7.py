var_nilai = 0
var_i = 1
for var_nilai in range (0,10) :
  print("Perulangan pertama Ke",var_nilai)
  while (var_i < 3) :
    print("Perulangan ke", var_nilai, ",", var_i)
    var_i +=1
  var_i =1
print("var nilai =", int(var_nilai)+1, "= 10. Bernilai False")
