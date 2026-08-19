# Clean Code Summary 

# Before you practice, remember:

# Clean Python code is modular: break logic into small functions/classes/modules so each piece does one thing and can be tested or changed independently.
# Maintainability and readability hinge on clear structure and naming: use descriptive function/variable names, consistent formatting, and keep functions/classes focused.
# Favor simplicity: choose straightforward, explicit solutions over clever or deeply nested logic; if a function is hard to explain, it’s probably too complex.
# Single Responsibility Principle (SRP): each class (or function) should have one reason to change; keep unrelated concerns in separate components.
# Open/Closed Principle (OCP): design so you can add behavior by extending (new classes, new methods) rather than editing existing, working code.
# Dependency Inversion Principle (DIP): depend on abstractions (e.g., interfaces/protocols, base classes, or injected callables) instead of concrete implementations to make code easier to swap and test.
# Liskov Substitution Principle (LSP): any subclass should be usable wherever its base class is expected without breaking behavior (no surprising pre/post-condition changes).
# Refactoring is changing internal structure without changing external behavior; use it to reduce technical debt and improve clarity (e.g., extract functions, rename variables, remove duplication).
# Pythonic code follows the Zen of Python (import this): prioritize readability, simplicity, and explicitness; use idioms like list comprehensions, context managers, and enumerate where they clarify intent.
# Code review is a structured, collaborative check of code for correctness, style, and design; be ready to both give and receive specific, constructive feedback.

# Common mistakes to watch out for:

# Letting functions/classes grow too large and mixed-purpose, violating SRP; instead, split responsibilities into smaller units.
# Extending behavior by editing many existing classes/functions (breaking OCP) instead of adding new ones that plug into existing extension points (e.g., via inheritance or composition).
# Creating subclasses that change expected behavior (violating LSP), such as throwing new errors or ignoring base-class guarantees; ensure overrides respect the base contract.
# Hard-coding dependencies inside classes (e.g., directly instantiating concrete services) instead of injecting them or depending on abstractions, which breaks DIP and makes testing harder.
# Treating refactoring as optional “cleanup later” and mixing it with feature changes; instead, refactor in small, behavior-preserving steps with tests to guard against regressions.
# Writing “clever” or overly compact Python (dense comprehensions, chained expressions) that hurts readability and goes against Pythonic principles; prefer clear, explicit code that reviewers can understand quickly.