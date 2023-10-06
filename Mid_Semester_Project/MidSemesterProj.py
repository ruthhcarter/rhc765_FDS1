numbers = []

while True: 
    #tie functions to menu 
    import rhc_stats_module
    #menu display
    print("Option 1: Input Numbers")
    print("Option 2: Calculate Mean") 
    print("Option 3: Calculate Variance")
    print("Option 4: Calculate Standard Deviation")
    print("Option 5: Calculate Standard Error")
    print("Option 6: Calculate Z-score")
    print("Option 7: Print Summary")
    print("Option 8: Quit :-) ")
    
    choice = input("Enter your choice (number):")
    
    if choice == '1': #loop for inputting numbers
        global numbers 
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
        
#operational functions 
    elif choice == '2':
        rhc_stats_module.mean(numbers) 
    elif choice == '3':
        rhc_stats_module.variance(numbers)
    elif choice == '4': 
        rhc_stats_module.st_dev(numbers)
    elif choice =='5': 
        rhc_stats_module.std_err(numbers)
    elif choice == '6': 
        rhc_stats_module.z_score(numbers)
    elif choice == '7': 
        rhc_stats_module.summary(numbers)
    elif choice == '8': 
        break 
        
#done with menu
    else:
        print("Invalid input. Please try a different number") 
        
