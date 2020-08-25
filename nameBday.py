from datetime import datetime

name = input("Enter your name: ")
bday_month = input("In what month were you born? ")
if bday_month.lower() == 'august':
    print(f'Happy birthday {name.title()}!.  Your name is {len(name)} characters long.')
else:
    print(f'Hello {name.title()}!  Your name is {len(name)} characters long.')


# def main():
#     name = input("Enter your name: ")
#     bday_month = input("In what month were you born? ")
#     current_month = get_current_month #calling function below and returning
#     #if compare_case_insensitive(bday_month, current_month):
#         print(f'Happy Birthday month {name}!')

# def get_current_month():
#     today = datetime.today()
#     month_text = today.strftime('%B') #format month to print out month word
    
#     return month_text

# def compare_case_insensitive(st1, st2):
#     return str(st1).lower() == str(st2).lower()

# main() #calling the main function
