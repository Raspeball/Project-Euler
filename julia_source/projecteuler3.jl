################################################
# Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
###############################################

function largest_prime_factor(n)
    f = n
    factor = 0
     if mod(f,2)==0  # if i divides n
         f = f/2
         factor = 2
     end
    i = 3
    while f > 1 && i <= floor(n/2)
        if mod(f,i)==0    # if i divides n
            f = f/i
            factor = i
        end
        i=i+2
    end
    return Int(factor)
end

k = 600851475143

print("The largest prime factor of ", k, " is ", largest_prime_factor(k))
