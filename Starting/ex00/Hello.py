ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

tmp = list(ft_tuple)
tmp[1] = "France!"
ft_tuple = tmp

ft_set.clear()
ft_set.add("Hello")
ft_set.add("Paris!")

ft_dict.clear()
ft_dict.update({"Hello" : "42Paris!"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)