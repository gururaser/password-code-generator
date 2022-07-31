# password-code-generator
 A program who generates passwords/codes
 
 ![Screenshot](https://github.com/gururaser/password-code-generator/blob/main/Code%20Generator/screenshot.png)

## Getting Started

This project is sample to create randomly codes/password.

You can create passwords of different difficulties according to the difficulty you choose.

For example if you choose "Basic" level, you can create password only by lowercase and uppercase letters.
- It's like pODkR

If you choose "Medium" level, you can create password along with what the simple level brings, you also add numbers to the work.
- It's like x39kG

If you choose "Expert" level, it's combine of the previous two and special symbols. ( Note: Probably websites won't accept some of these symbols but they added to make password more complicated. It's just sample )
- It's like ^5X?m

Important note : Because of the logic, although you choose the most difficult option you can face with password/code like A90bM. It's maybe low possibility but it is possible. I Will try to fix it in next publish. ( SOLVED )

# UPDATE NOTES

With help of some research I've found solution to problem I mentioned in "Important note".

I also added two different code blocs to react what if user enters fewer data than we expect
- First one completes with as many random characters as you left blank.
![Screenshot](https://github.com/gururaser/password-code-generator/blob/main/Code%20Generator/screenshot2.png)
- Second one wants user to enter the right number
![Screenshot](https://github.com/gururaser/password-code-generator/blob/main/Code%20Generator/screenshot3.png)
