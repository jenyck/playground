-- factorial function
function factorial(n)
    if n == 0 then
        return 1
    else
        return n * factorial(n - 1)
    end
end

-- i-o
print("enter a number:")
a = io.read("*n") -- reads a number from standard input
print(factorial(a))
