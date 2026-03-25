# Classes_and_objects

# Class Constructor=
class Person:
    def __init__(self, firstname = 'luka', lastname = 'marinkovic', age = 21, country = 'Croatia', city = 'Osijek'): #if we dont give object any info he will use default values
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []
# Object Methods
    def personal_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'
    def add_skill(self, skill):
        self.skills.append(skill)

p = Person('luka', 'marinkovic', 21, 'Croatia', 'Osijek')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

p1 = Person()
print(p1.personal_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.personal_info())
print(p1.skills)
print(p2.skills)

# Overriding parent method
class Student(Person): # Inheritance 
    def __init__(self, firstname = 'luka', lastname = 'marinkovic', age = 21, country = 'Croatia', city = 'Osijek',gender = 'male'): #if we dont give object any info he will use default values
        self.gender = gender
        super().__init__(firstname,lastname,country,city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.personal_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.personal_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

# Exercises: Day 21

# 1
import statistics
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
class Statistics():
    def __init__(self, ages):
        self.ages = ages
    def count(self):
        return len(self.ages)
    def sum(self):
        summed_age = sum(self.ages)
        return summed_age
    def min(self):
        min_age = min(self.ages)
        return min_age
    def max(self):
        max_age = max(self.ages)
        return max_age
    def range(self):
        ranges = max(self.ages) - min(self.ages)
        return ranges
    def mean(self):
        mean_age = statistics.mean(self.ages)
        return mean_age
    def median(self):
        median_age = statistics.median(self.ages)
        return median_age
    def mode(self):
        new_dict = {}
        for age in self.ages:
            if age not in new_dict:
                new_dict[age] = 1
            else:
                new_dict[age] += 1
        sorted_dict = sorted(new_dict.items(),key=lambda x:x[1], reverse=True)
        result = sorted_dict[0]
        return result
    def std(self):
        std_age = statistics.stdev(self.ages)
        return std_age
    def var(self):
        var_ages = statistics.variance(self.ages)
        return var_ages
    def freq_dist(self):
        new_dict = {}
        for age in self.ages:
            if age not in new_dict:
                new_dict[age] = 1
            else:
                new_dict[age] += 1
        total = len(self.ages)
        pairs = [((count / total) * 100, age) for age, count in new_dict.items()]
        pairs.sort(reverse=True)
        return pairs
    def describe(self):
        print('Count:', data.count()) # 25
        print('Sum: ', data.sum()) # 744
        print('Min: ', data.min()) # 24
        print('Max: ', data.max()) # 38
        print('Range: ', data.range()) # 14
        print('Mean: ', data.mean()) # 30
        print('Median: ', data.median()) # 29
        print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
        print('Standard Deviation: ', data.std()) # 4.2
        print('Variance: ', data.var()) # 17.5
        print('Frequency Distribution: ', data.freq_dist())

data = Statistics(ages)
print(data.describe())

# 2 we will assume incomes and exenses are in a set 
incomes = {("salary", 2000), ("freelance", 500)}
expenses = {("rent", 800), ("food", 300)}


class PersonAccount():
    def __init__(self,  firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        total = 0
        for income in self.incomes:
            total += income[1]
        return total
    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense[1]
        return total
    def account_info(self):
        return f'{self.firstname} {self.lastname} : Total incomes :{self.total_income()}, Total expenses: {self.total_expense()}'
    def add_income(self):
        description = input('Enter description: ')
        amount = float(input('Enter amount: '))
        self.incomes.add((description, amount))
    def add_expense(self):
        description = input('Enter description: ')
        amount = float(input('Enter amount: '))
        self.expenses.add((description, amount))
    def account_balance(self):
        return self.total_income() - self.total_expense()
    
account = PersonAccount("Luka", "Marinkovic", incomes, expenses)
print(account.account_info())         
account.add_income()                  
account.add_expense()                 
print(account.account_balance())