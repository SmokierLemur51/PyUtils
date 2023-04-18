def Gather_Data():
	data = {
		"rates": [],
		"avg_windows": 0,
		"houses_per_day": 0,
		"days_per_week": 0,
	}
	while True:
		rate_prompt = input("Enter rates or leave empty:\n\t]>  ")
		if rate_prompt == '' or rate_prompt.lower() == 'x':
			print()
			break
		else:
			data['rates'].append(float(rate_prompt))
	data["avg_windows"] = int(input("\nEnter Average # of Windows:\n\t]>  "))
	data["houses_per_day"] = int(input("\nEnter average number of houses per day:\n\t]>  "))
	data["days_per_week"] = int(input("\nEnter the amount of days you want to work a week:\n\t]>  "))

	return data



def Pretax_Projections(data):
	if type(data) == dict:
		window_day = data["avg_windows"] * data["houses_per_day"]
		window_week = window_day * data["days_per_week"]
		window_month = window_week * 4
		window_year = window_month * 12
		projections = {
			"windows_per_day": window_day,
			"windows_per_week": window_week,
			"windows_per_month": window_month,
			"windows_per_year": window_year,
		}
		# set other keys that rely on the initialized ones 
		projections["income_daily"] = (projections["windows_per_day"] * data["rate"]), 
		projections["income_weekly"] = (projections["income_daily"] * data["days_per_week"])
		projections["income_monthly"] = (projections["income_weekly"] * 4)
		projections["income_yearly"] = (projections["income_monthly"] * 12)
		
		return projections
	else:
		print("Paramter must be dictionary for this to properly function.")
		return



def Calculate_Taxes(data):	
	''' returns taxed projections '''
	return post_tax_projections



def Calculate_Expenses(expenses)
	''' what kind of expenses does a window cleaning company have  '''
	return expenses



class Inventory:
	pass 


