

visitors = [120, 80, 150, 200, 95, 300, 220]

total_visitors = 0
low_traffic_hours = 0
max_traffic = 0
traffic = 0 

for v in visitors:
    total_visitors = total_visitors + v

    if v < 100:
        low_traffic_hours = low_traffic_hours + 1

    if v > max_traffic:
        max_traffic = v

    if  v > 250:
        traffic = v
             
average_visitors = total_visitors/len(visitors)

print("Total visitors:", total_visitors)
print("Low traffic hours:", low_traffic_hours)
print("peak traffic:", max_traffic)
print("Average visitors per second:", average_visitors)            
print("High traffic alert:", traffic)