'''Scenario:
Restrict access to certain functions.
Task:
● Create a decorator to check user role
● Use condition inside decorator
● Apply decorator to multiple functions
● Store roles in a dictionary'''

#  Store user roles in a dictionary
users = {
    "Hemanth": "admin",
    "Rajesh": "user",
    "Ajay": "manager"
}

# Current logged-in user
current_user = "Hemanth"


#  Create a decorator to check user role
def check_role(required_role):
    def decorator(func):
        def wrapper():
            user_role = users[current_user]

            #  Check access using condition
            if user_role == required_role:
                print("Access Granted!")
                func()
            else:
                print("Access Denied! You don't have permission.")

        return wrapper
    return decorator


#  Apply decorator to multiple functions
@check_role("admin")
def delete_data():
    print("Data deleted successfully!")


@check_role("manager")
def view_reports():
    print("Viewing reports...")


@check_role("user")
def view_profile():
    print("Viewing user profile...")


#  Call functions
delete_data()
view_reports()
view_profile()