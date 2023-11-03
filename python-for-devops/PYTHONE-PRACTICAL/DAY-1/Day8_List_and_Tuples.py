#LISTS

instance_type = ["t2.micro","t2.medium","t3.xlarge"]
print(instance_type)
print(len(instance_type))  # length of the lists
print("\n",type(instance_type))
instance_type.append("c5.xlarge")  #append used in list
print(len(instance_type))
print(instance_type)
print(instance_type[1])
instance_type.remove("t2.medium") # remove in list
print("t2.medium removed after result\n",instance_type)
new_list = instance_type[0:2]

#TUPLES
instance_type2 = ("t2.micro","t2.medium","t3.xlarge")
print(instance_type2)
print(len(instance_type2)) # length of the Tuples
print("\n",type(instance_type2))
#instance_type2.append("c5.xlarge") #append donot used in Tuples because it is will not change
print(instance_type2)