# operator and
def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"
    if (gpa >= 2.0) and (credits < 120):
        return "You do not have enough credits to graduate."
    if (gpa < 2.0) and (credits >= 120):
        return "Your GPA is not high enough to graduate."
    if (gpa < 2.0) and (credits < 120):
        return "You do not meet either requirement to graduate!"


print(graduation_reqs(2.1, 130))
print(graduation_reqs(2.0, 110))
print(graduation_reqs(1.8, 140))
print(graduation_reqs(1.5, 100))
print(graduation_reqs(120, 2.0))

# operator or


def graduation_mailer(gpa, credits):
    if(credits >= 120) or (gpa >= 2.0):
        return True


print(graduation_mailer(2.0, 120))

# if else statements


def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"
    else:
        return "You do not meet the GPA or the credit requirement for graduation."


print(graduation_reqs(1.8, 100))

# elif statements


def thank_you(donation):
    if donation >= 1000:
        print("Thank you for your donation! You have achieved platinum donation status!")
    elif donation >= 500:
        print("Thank you for your donation! You have achieved gold donation status!")
    elif donation >= 100:
        print("Thank you for your donation! You have achieved silver donation status!")
    else:
        print("Thank you for your donation! You have achieved bronze donation status!")


print(thank_you(100))

# elif statement 2 with grade as variable  and F if below 1.0


def grade_converter(gpa):
    grade = "F"

    if gpa >= 4.0:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.0:
        grade = "C"
    elif gpa >= 1.0:
        grade = "D"

    return grade


print(grade_converter(0.9))

# college admissions

def applicant_selector(gpa,ps_score,ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    return "This applicant should be accepted."
  elif (gpa >= 3.0) and (ps_score >= 90) and (ec_count < 3):
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."

  
print(applicant_selector(3.0,90,3))
print(applicant_selector(3.0,90,2))
print(applicant_selector(1.0,70,2))