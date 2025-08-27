def example_w_plus_mode():
    with open("example_a+.txt", "w+") as file:
        file.seek(0)
        content = file.read()
        print("Content after writing:")
        print(content)

        file.write("Appending a new line atthe end\n")
        file.write("Appending another line at the end\n")
        file.seek(0)
        updated_content = file.read()
        print("update after writing:")
        print(updated_content)

example_w_plus_mode()