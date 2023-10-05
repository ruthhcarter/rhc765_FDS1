# Operations: 

## mean: 
def mean(x):
    mean=sum(x)/len(x)
    print(f"Mean = {mean:.3f}")
    
## variance: 
def variance(x):
    mean = sum(x) / len(x)
    squared_deviation = [(num - mean) ** 2 for num in x]
    sum_of_squares= sum(squared_deviation)
    var = sum_of_squares/(len(x)-1)
    print(f"Variance = {var:.3f}")

## std dev: 
def st_dev(x):
    mean = sum(x) / len(x)
    squared_deviation = [(num - mean) ** 2 for num in x]
    sum_of_squares= sum(squared_deviation)
    var = sum_of_squares/(len(x)-1)
    std_dev= var**(1/2)
    print(f"Standard Deviation = {std_dev:.3f}")
    
## std error: 
def std_err(x):
    mean = sum(x) / len(x)
    squared_deviation = [(num - mean) ** 2 for num in x]
    sum_of_squares= sum(squared_deviation)
    var = sum_of_squares/(len(x)-1)
    std_dev= var**(1/2)
    std_err= std_dev/((len(x))**(1/2))
    print(f"Standard Error = {std_err:.3f}")

## z-score: 
def z_score(x):
    #ask user for observation to base z-score on:
    observed_value= float(input("Enter a new observation to calculate z-score"))
    mean = sum(x) / len(x)
    squared_deviation = [(num - mean) ** 2 for num in x]
    sum_of_squares= sum(squared_deviation)
    var = sum_of_squares/(len(x)-1)
    std_dev= var**(1/2)
    z= (observed_value - mean)/std_dev
    print(f"Z-score = {z:.3f}")

## summary of descriptive stats: 
def summary(x): 
    observed_value= float(input("Enter a new observation to calculate z-score"))
    mean = sum(x) / len(x)
    squared_deviation = [(num - mean) ** 2 for num in x]
    sum_of_squares= sum(squared_deviation)
    var = sum_of_squares/(len(x)-1)
    std_dev= var**(1/2)
    std_err= std_dev/((len(x))**(1/2))
    z= (observed_value - mean)/std_dev
    
    #clean outputs
    print(f"Mean = {mean:.3f}")
    print(f"Variance = {var:.3f}")
    print(f"Standard Deviation = {std_dev:.3f}")
    print(f"Standard Error = {std_err:.3f}")
    print(f"Z-score = {z:.3f}")
    
    
