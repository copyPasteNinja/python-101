# Session 1

## Variables

- containers
- variables in python can start with letter (a-z, A-Z), it can start with underscroes(\_)
- cannot start with numbers, non-alphateical characters (, . - ..)
- cannot have the same name as keywards

## Data Types (Numeric Data Types)

- Integers (whole numbers) (1,2,3,4)
- Hexidecimal (1x123)
- Floats (decimals point numbers) (1.3, 1.5, 16, ...)
- Octal Numbers (0o123)

############### int data type ###############

```
var1 = 123
print(var1)
```

############### float data type ###############

```
var2 = 12.4
print(var2)
```

### Octal Numbers

- 0o or 0O
- represents the numbers 0 to 7 -- cannot be 0o189
- linux uses octal numbers in `chmod` command

```
var3 = 0o123
print(0o123)

var4 = 83
print(oct(var4))
```

### Hexideimal Number

- 0x or 0X
- 16 elements -- represents 0 to 9, a to f

```
print(0x123)
```

### Mathematical Operations in Python

- Power
- Devision
- Integer Devision ## only gives whole numbers
- Modules
- Multipilcation
- Addition
- Subscration

```
# simple Maths
print(5 + 5)   # regular addition
print(10 - 5)  # regular subscration
print(20 / 5)  # regular division
print(20 // 5) # integer division
```

```
# Modules division
# 19 - 15 = 4
print(19 % 5)
```

```
# power
# 2 * 2 * 2
print(2 ** 3)

print( 2 ** 3 ** 2) # it starts from left to right
```
