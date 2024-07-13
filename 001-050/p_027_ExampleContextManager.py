class ExampleContextManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        if exc_type:
            print(f"Exception: {exc_value}")
        return False  # Allow the exception to propagate


def generator_function():
    with ExampleContextManager() as cm:
        try:
            yield cm
        except Exception as e:
            print(f"Exception caught: {e}")
        finally:
            print("Cleanup code")


gen = generator_function()
cm = next(gen)  # Enter the `with` block
gen.throw(Exception("Test exception"))  # Raise an exception within the `with` block
