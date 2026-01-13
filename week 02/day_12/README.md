<h1 align="center">Day 12 Progress – Object-Oriented Programming</h1>
<h3 align="center"><b>Date: 13/01/2026</b></h3>

---

## 1️ The Constructor
**What we did:**  
Created a `User` class where every new user starts with `is_active = True`.

**What we learned:**  
Constructors (`__init__`) allow initializing default state for every instance of a class.

---

## 2️ The Self Reference
**What we did:**  
Explained why instance methods require `self` as the first parameter.

**What we learned:**  
`self` allows a method to access and modify the instance’s attributes. Calling `obj.method()` automatically passes the object as `self`.

---

## 3️ The String Representation
**What we did:**  
Customized `__str__` and `__repr__` so printing objects shows meaningful information.

**What we learned:**  
- `__str__` is for human-readable output.  
- `__repr__` is for developer-friendly representation, useful in lists or debugging.

---

## 4️ Private Variables
**What we did:**  
Used double underscores (`__password`) to prevent external modification of a variable.

**What we learned:**  
Python uses name mangling to protect private attributes from being accessed directly outside the class.

---

## 5️ The Property Decorator
**What we did:**  
Created a `user.age` property that calculates age dynamically without storing it.

**What we learned:**  
`@property` allows methods to behave like attributes, providing computed or read-only values.

---

## 6️ Class Variables vs Instance Variables
**What we did:**  
Explored the difference between a class variable (`species`) and instance variables (`name`).

**What we learned:**  
- Class variables are shared across all instances.  
- Changing the class variable affects all instances without their own attribute.  
- Assigning a value to an instance creates an instance-level variable that shadows the class variable.

---

## 7️ Inheritance
**What we did:**  
Created an `Admin` class inheriting from `User` and added `delete_db()` method only for `Admin`.

**What we learned:**  
Inheritance allows reusing and extending functionality from a parent class.

---

## 8️ The Super Proxy
**What we did:**  
Overrode `__init__` in `Admin` while still calling `User`’s `__init__` using `super()`.

**What we learned:**  
`super()` ensures proper initialization of the parent class when overriding constructors in subclasses.

---

## 9️ Operator Overloading
**What we did:**  
Allowed adding two `Wallet` objects using `+` by defining `__add__`.

## 10 Equality

**What we did:**
Defined __eq__ in the User class so that two User objects with the same user_id are considered equal.

What we learned:

__eq__ allows customizing equality checks for objects.

Without it, Python compares objects by memory address, not by their content.

Defining __eq__ enables logical equality based on attributes rather than instance identity.

**What we learned:**  
Special methods like `__add__` allow customizing standard operators for user-defined classes.

