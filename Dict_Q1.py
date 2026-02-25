employe = {
            "emp_id": 101,
            "name": "Guru", 
            "department": "IT",
            "salary": 50000,
            "location": "Pune"
          }

print(employe["name"])

employe["salary"] = 58000
print(employe)  

employe["email"] = "guru@email.com"
print(employe)  

del employe["location"]
print(employe)

employe["phone"] = "9850003490"
print(employe)

employe["department"] = "Electronics"
print(employe)  

print(employe["salary"])

print("Total fields:", len(employe))