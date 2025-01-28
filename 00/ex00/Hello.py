ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

ft_tuple1 = list(ft_tuple)
ft_tuple1[1] = "France!"
ft_tuple = tuple(ft_tuple1)

ft_set.clear()
ft_set.add("Nice!")
ft_set.add("Hello")

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
