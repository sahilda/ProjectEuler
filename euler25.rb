a = 1
b = 1
digits = 1000
idx = 2
not_found = true
answer = 0

while not_found
    idx += 1
    a = a + b

    if a.to_s.length >= digits
        answer = a
        break
    end

    idx += 1
    b = a + b

    if b.to_s.length >= digits
        answer = b
        break
    end
end

puts answer
puts idx
