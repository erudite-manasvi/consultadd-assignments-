# You are developing a program that analyzes weather data. Write a Python function that takes a list of temperature readings for a specific location and determines the average temperature, highest temperature, and lowest temperature.

def analyze_data(lst):
    avg = sum(lst)/len(lst)
    low = min(lst)
    high = max(lst)
    
    return [avg,low,high]

print(analyze_data([25, 28, 21, 24, 27]))


    