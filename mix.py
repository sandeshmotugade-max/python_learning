

def check_result(marks):
    if marks >= 35:
        return "pass"
    else:
        return "fail"
    
marks = [75,35,22,81,90]  

for m in marks:
    result = check_result(m)
    print("Marks:", m, "result", result)