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
		windows_daily = data["avg_windows"] * data["houses_per_day"]

		projections = {
			"estimated_workload": {
				"days_per_week": data["days_per_week"],
				"houses_per_day": data["houses_per_day"]
				"est_windows_daily": windows_daily,
				"est_windows_weekly": (windows_daily * data["days_per_week"]),
				"est_windows_monthly": ((windows_daily * data["days_per_week"]) * 4),
				"est_yearly_windows": ((windows_daily * data["days_per_week"] * 4) * 12),
			},	
			"gross_income_proj": {},
			"expenses": {},
		}
		# calculate gross income projections based off of rates and estimated number of windows 
		for x in data["rates"]:
			projections["gross_income_proj"][f"${x}_windows_daily"] = (projections["windows_per_day"] * float(x))
			projections["gross_income_proj"][f"${x}_windows_weekly"] = (projections["gross_income_proj"][f"${x}_windows_daily"] * data["days_per_week"])
			projections["gross_income_proj"][f"${x}_windows_monthly"] = (projections["gross_income_proj"][f"${x}_windows_weekly"] * 4)
			projections["gross_income_proj"][f"${x}_windows_yearly"] = (projections["gross_income_proj"][f"${x}_windows_monthly"] * 12)  

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


