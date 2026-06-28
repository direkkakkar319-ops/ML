# %%
def demonstrate_exec():
    code = """def greet(name):
                return f"Hello, {name}!\""""
    
    # Execute the code string
    local_scope = {}
    exec(
        code,
        {},
        local_scope
        )
    print(local_scope["greet"], ("Alice"))
demonstrate_exec()

# %%
def demonstrate_eval():
    # Evaluate the expression
    expression = input("Type an expression:  ")
    result = eval(expression)

    print(f"Result of eval: {result}\n")
demonstrate_eval()

# %%
def demonstrate_safe_eval():
    # Evaluate Expression
    expression = input("Type an expression that uses a,b and c:   ")

    # Defining the variable for expression
    variables = {"a": 2, "b": 3, "c": 4}

    # Evaluate the expression in the context of the provided variables
    result = eval(
        source=expression,
        globals={"__builtins__": None}, # python builtins will not be allowed
        locals=variables
    )

    print(f"Result of safe eval: {result}\n")
demonstrate_safe_eval()

# %%
