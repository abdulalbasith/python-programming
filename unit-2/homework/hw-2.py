# Full time: Works 40 hours per week; $50/hour. Overtime: $60/Hour
# Part time: Works 20 hours per week: $65/hour. Overtime: $70/Hour
# Contract : $120/Hour; 25% Tax

worker_type = ""
hours_worked = 0
weekly_wage = 0

#Weekly wage of full time worker
worker_type = input ("What kind of worker are you? ")
hours_worked = int (input ("How many hours did you work this week? "))

#if worked less than or equal to 40 hours
if worker_type == "full time" and hours_worked <= 40:
    weekly_wage = hours_worked * 50 
    print (f"This week your wage is ${weekly_wage}")

#full time worker overtime 
elif worker_type == "full time" and hours_worked >= 40:
    over_time = hours_worked - 40
    not_over_time = hours_worked - over_time
    weekly_wage = ((not_over_time * 50) + (over_time * 60))
    print (f"This week your wage is ${weekly_wage}")

#part time worker wage without over time
elif worker_type == "part time" and hours_worked <= 20:
    weekly_wage = hours_worked * 65 
    print (f"This week your wage is ${weekly_wage}")

#part time worker wage with overtime

elif worker_type == "part time" and hours_worked >= 20:
    over_time = hours_worked - 20
    not_over_time = hours_worked - over_time
    weekly_wage = ((not_over_time * 65) + (over_time * 70))
    print (f"This week your wage is ${weekly_wage}")

#contract worker
elif worker_type == "contract":
    weekly_wage = ((hours_worked * 120) * 0.75)
    print (f"This week your wage is ${weekly_wage}")
    