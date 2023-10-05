# Menu: 

# Make a list: 
numbers = []

def enter_num(numbers):
    numbers = []
    i=1
    while i>=1:
        x = input("Enter numbers one by one. Type 'done' when finished.")
        i += 1
        if x == "done":
            break 
        else: 
            num= float(x)
            numbers.append(num)   

    print("These are the numbers you inputted:",numbers)
    
    
# Operations: 

## mean: 
def mean():
    global numbers
    mean=sum(numbers)/len(numbers)
    print(f"Mean = {mean:.3f}")
    
## variance: 
def variance(numbers):
     
    mean = sum(numbers) / len(numbers)
    squared_deviation = [(num - mean) ** 2 for num in numbers]
    sum_of_squares= sum(squared_deviation)
    var = sum_of_squares/(len(numbers)-1)
    print(f"Variance = {var:.3f}")

## std dev: 
def st_dev(numbers):
    mean = sum(numbers) / len(numbers)
    squared_deviation = [(num - mean) ** 2 for num in numbers]
    sum_of_squares= sum(squared_deviation)
    var = sum_of_squares/(len(numbers)-1)
    std_dev= var**(1/2)
    print(f"Standard Deviation = {std_dev:.3f}")
    
## std error: 
def std_err(numbers):
    mean = sum(numbers) / len(numbers)
    squared_deviation = [(num - mean) ** 2 for num in numbers]
    sum_of_squares= sum(squared_deviation)
    var = sum_of_squares/(len(numbers)-1)
    std_dev= var**(1/2)
    std_err= std_dev/((len(numbers))**(1/2))
    print(f"Standard Error = {std_err:.3f}")

## z-score: 
def z_score(numbers):
    observed_value= float(input("Enter a new observation to calculate z-score"))
    mean = sum(numbers) / len(numbers)
    squared_deviation = [(num - mean) ** 2 for num in numbers]
    sum_of_squares= sum(squared_deviation)
    var = sum_of_squares/(len(numbers)-1)
    std_dev= var**(1/2)
    z= (observed_value - mean)/std_dev
    print(f"Z-score = {z:.3f}")

## summary of descriptive stats: 
def summary(numbers): 
    observed_value= float(input("Enter a new observation to calculate z-score"))
    mean = sum(numbers) / len(numbers)
    squared_deviation = [(num - mean) ** 2 for num in numbers]
    sum_of_squares= sum(squared_deviation)
    var = sum_of_squares/(len(numbers)-1)
    std_dev= var**(1/2)
    std_err= std_dev/((len(numbers))**(1/2))
    z= (observed_value - mean)/std_dev
    #clean outputs
    print(f"Mean = {mean:.3f}")
    print(f"Variance = {var:.3f}")
    print(f"Standard Deviation = {std_dev:.3f}")
    print(f"Standard Error = {std_err:.3f}")
    print(f"Z-score = {z:.3f}")
    
    
