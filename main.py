import sys

def main():
    print("Hello from GitHub Actions caching & artifacts demo!")
    with open("output.txt", "w") as f:
        f.write("This is a build artifact. New Chnage!!\n")

if __name__ == "__main__":
    main()
