def retry(max_retries, exc):

    def decorator(func):

        def inner(*args, **kwargs):
            retries = 1
            while retries <= max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except ValueError:
                    if retries == max_retries:
                        return exc
                    print("Input is not a number.")
                    retries += 1
        return inner
    return decorator


@retry(max_retries=3, exc="Try everything")
def age():
    num = input("Enter your age: ")
    result = int(num) + 10
    return result


print(age())
