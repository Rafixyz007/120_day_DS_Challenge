<h1 align="center">Day 10 Progress – Decorators (Deep Dive)</h1>
<h3 align="center"><b>Date: 11/01/2026</b></h3>

---

## 1️⃣ Manual Wrapper
**What we did:**  
Manually wrapped a function to execute logic before and after the original function call.

**What we learned:**  
Functions are first-class objects and can be wrapped, replaced, and extended without modifying their original implementation.

---

## 2️⃣ Decorator Syntax Sugar
**What we did:**  
Applied the same wrapper logic using the `@decorator` syntax.

**What we learned:**  
The `@decorator` syntax is just a cleaner way to reassign a function to its wrapped version.

---

## 3️⃣ The Args Problem
**What we did:**  
Tried decorating a function that requires parameters using a wrapper that accepts none.

**What we learned:**  
Decorators must accept `*args` and `**kwargs` to work with functions of varying signatures.

---

## 4️⃣ The Return Value Thief
**What we did:**  
Created a decorator that calls a function but forgets to return its result.

**What we learned:**  
If a decorator does not explicitly return the wrapped function’s result, the decorated function returns `None`.

---

## 5️⃣ Performance Timer
**What we did:**  
Built a timing decorator to measure function execution duration.

**What we learned:**  
Decorators are useful for cross-cutting concerns like performance measurement without polluting business logic.

---

## 6️⃣ Authentication Guard
**What we did:**  
Restricted function execution based on user role using a decorator.

**What we learned:**  
Decorators are effective for enforcing access control and guard conditions consistently.

---

## 7️⃣ Memoization (Caching)
**What we did:**  
Implemented a caching decorator to store and reuse results of function calls.

**What we learned:**  
Decorators can significantly improve performance by avoiding repeated expensive computations.

---

## 8️⃣ Metadata Preservation
**What we did:**  
Observed how decorators overwrite function metadata and fixed it using `functools.wraps`.

**What we learned:**  
Without `@wraps`, decorators hide the original function’s name and docstring.

---

## 9️⃣ Stacked Decorators
**What we did:**  
Applied multiple decorators to a single function to observe execution order.

**What we learned:**  
Decorators execute from the inside out — the decorator closest to the function runs first.

---

## 🔟 Decorators With Arguments
**What we did:**  
Created a decorator factory that accepts parameters and modifies behavior accordingly.

**What we learned:**  
Decorators with arguments add an extra layer of function nesting and enable highly configurable behavior.

---

## 🧠 Key Takeaways
- Decorators extend behavior without modifying existing code
- Argument forwarding and return values are critical
- Metadata preservation matters in real applications
- Decorators enable logging, caching, authorization, and performance monitoring
- Understanding execution order prevents subtle bugs

