
f = open("TimesTableOutput.txt", "w+")

dims = int(input("What number should your times table goto?"))


# -------------Times Table-----------------
with f:
    for i in range(1, dims + 1):
        if i < 10:
            f.write(f'  {i} ')
        else:
            f.write(f" {i} ")
    f.write(f"\n  {(dims  * 4 - 3) * '-'}\n")

    for col in range(1, dims + 1):
        for row in range(1, dims + 1):
            prod = row * col

            if prod < 10:
                f.write(f"  {prod} ")
            elif prod < 100:
                f.write(f" {prod} ")
            else:
                f.write(f"{prod} ")
        f.write("\n")
