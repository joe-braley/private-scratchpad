import os

def main(env_var_name, env_value):
    github_env = os.getenv("GITHUB_ENV")

    with open(github_env, 'w') as file:
        file.write(f"{ env_var_name }={ env_value }")

if __name__ == "__main__":
    main("TEST1", "A")
    main("TEST2", "B")
    main("TEST3", "C")
    main("TEST4", "D")
    main("TEST5", "E")